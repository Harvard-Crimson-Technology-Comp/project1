from django.shortcuts import render

from django.http import HttpResponseNotFound, JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

import bcrypt

from project1.api.models import UserModel, PurchaseModel, StockModel, PortfolioModel

from alpha_vantage.timeseries import TimeSeries

from datetime import datetime
from time import sleep

# don't put this here in real code! you are welcome to use this key if you would like
av_api_key = "B6Z376P6CGR0XAL5"
ts = TimeSeries(key=av_api_key)

"""
You will create many 4 key views here: register, buy, sell, and list

register - allows a user to register and obtain an API token
buy - allows a user to buy some stocks by submitting a symbol and an amount
sell - allows a user to sell some stocks by submitting a symbol and an amount
list - allows a user to see their current portfolio, does not take arguments
"""

@require_http_methods(["POST"])
@csrf_exempt
def register(request):
    fields = ['first_name', 'last_name', 'username', 'password']

    # check they provided all the right data
    for field in fields:
        if not request.POST.get(field):
            return JsonResponse({'error': f'field - {field} - not found'})

    # check if the username already exists
    users = UserModel.objects.filter(username=request.POST.get('username'))
    if len(users) > 0:
        return JsonResponse({'error': f'username - {request.POST.get("username")} - already exists'})

    portfolio = PortfolioModel()
    portfolio.save()

    # create a new user and save them to the database
    user = UserModel(
        first_name=request.POST.get('first_name'),
        last_name=request.POST.get('last_name'),
        username=request.POST.get('username'),
        password=bcrypt.hashpw(request.POST.get('password').encode('utf-8'), bcrypt.gensalt()).decode(),
        portfolio=portfolio
    )
    user.save()

    return JsonResponse({'username': request.POST.get('username'), 'api_token': user.api_token})

@require_http_methods(["POST"])
@csrf_exempt
def buy(request):
    fields = ['api_token', 'symbol', 'quantity']

    # check they provided all the right data
    for field in fields:
        if not request.POST.get(field):
            return JsonResponse({'error': f'field - {field} - not found'})

    users = UserModel.objects.filter(api_token=request.POST.get('api_token'))

    # validate user
    if len(users) == 1:
        user = users[0]
    else:
        return JsonResponse({'error': 'No user found with that API token'})

    try:
        symbol, _ = ts.get_quote_endpoint(symbol=request.POST.get('symbol').upper())
    except ValueError:
        return JsonResponse({'error': f'symbol - {request.POST.get("symbol")} - not found'})

    # strip off AlphaVantage's annoying stuff:
    old_keys = [k for k in symbol]
    for k in old_keys:
        new_k = k.split('. ')[1]
        symbol[new_k] = symbol[k]

    cash = user.portfolio.cash

    if cash - int(request.POST.get('quantity')) * float(symbol['price']) < 0:
        return JsonResponse({'error': 'insufficient funds'})

    # update the amount of cash the user has
    user.portfolio.cash -= int(request.POST.get('quantity')) * float(symbol['price'])
    user.portfolio.save(update_fields=['cash'])

    # add a new purchase
    purchase = PurchaseModel(
        user=user,
        symbol=request.POST.get('symbol').upper(),
        price=symbol['price'],
        quantity=int(request.POST.get('quantity'))
    )
    purchase.save()

    stocks = StockModel.objects.filter(portfolio=user.portfolio, symbol=request.POST.get('symbol').upper())

    if stocks:
        stock = stocks[0]
        stock.quantity += int(request.POST.get('quantity'))
        stock.save(update_fields=['quantity'])
    else:
        stock = StockModel(
            portfolio=user.portfolio,
            symbol=request.POST.get('symbol').upper(),
            quantity=int(request.POST.get('quantity'))
        )
        stock.save()

    return JsonResponse({
        'symbol': request.POST.get('symbol').upper(),
        'quantity': int(request.POST.get('quantity')),
        'timestamp': purchase.timestamp,
        'cash_remaining': user.portfolio.cash
    })
    
@require_http_methods(["POST"])
@csrf_exempt
def sell(request):
    fields = ['api_token', 'symbol', 'quantity']

    # check they provided all the right data
    for field in fields:
        if not request.POST.get(field):
            return JsonResponse({'error': f'field - {field} - not found'})

    users = UserModel.objects.filter(api_token=request.POST.get('api_token'))

    # validate user
    if len(users) == 1:
        user = users[0]
    else:
        return JsonResponse({'error': 'No user found with that API token'})

    stocks = StockModel.objects.filter(portfolio=user.portfolio)

    for stock in stocks:
        if request.POST.get('symbol').upper() == stock.symbol.upper():
            if stock.quantity - int(request.POST.get('quantity')) < 0:
                return JsonResponse({'error': f'insufficient shares of {request.POST.get("symbol")}'})

            stock.quantity -= int(request.POST.get('quantity'))

            if stock.quantity == 0:
                stock.delete()
            else:
                stock.save(update_fields=['quantity'])

            try:
                symbol, _ = ts.get_quote_endpoint(symbol=request.POST.get('symbol').upper())
            except ValueError:
                return JsonResponse({'error': f'symbol - {request.POST.get("symbol")} - not found'})
            
            # strip off AlphaVantage's annoying stuff:
            old_keys = [k for k in symbol]
            for k in old_keys:
                new_k = k.split('. ')[1]
                symbol[new_k] = symbol[k]

            price = float(symbol['price'])

            user.portfolio.cash += float(price) * int(request.POST.get('quantity'))
            user.portfolio.save(update_fields=['cash'])

            purchase = PurchaseModel(
                user=user,
                symbol=request.POST.get('symbol').upper(),
                price=price,
                quantity=-int(request.POST.get('quantity'))
            )
            purchase.save()

            return JsonResponse({
                'symbol': request.POST.get('symbol').upper(),
                'quantity': -int(request.POST.get('quantity')),
                'timestamp': purchase.timestamp,
                'cash_remaining': user.portfolio.cash
            })

    return JsonResponse({'error': f'user does not own {request.POST.get("symbol")}'})

@require_http_methods(["GET"])
def api_list(request):
    fields = ['api_token']

    # check they provided all the right data
    for field in fields:
        if field not in request.GET:
            return JsonResponse({'error': f'field - {field} - not found'})

    users = UserModel.objects.filter(api_token=request.GET.get('api_token'))

    # validate user
    if len(users) == 1:
        user = users[0]
    else:
        return JsonResponse({'error': 'No user found with that API token'})

    return_dict = {
        'cash': float(user.portfolio.cash),
        'stocks': list()
    }

    for stock in StockModel.objects.filter(portfolio=user.portfolio):
        try:
            symbol, _ = ts.get_quote_endpoint(symbol=stock.symbol.upper())
        except ValueError:
            return JsonResponse({'error': f'symbol - {stock.symbol.upper()} - not found'})
    
        # strip off AlphaVantage's annoying stuff:
        old_keys = [k for k in symbol]
        for k in old_keys:
            new_k = k.split('. ')[1]
            symbol[new_k] = symbol[k]

        return_dict['stocks'].append({
            'symbol': symbol['symbol'].upper(),
            'quantity': stock.quantity,
            'price': symbol['price']
        })

        sleep(2)
    
    return_dict['timestamp'] = datetime.now().strftime('%m/%d/%Y-%H:%M:%S')

    return_dict['total_value'] = sum([x['quantity'] * float(x['price']) for x in return_dict['stocks']]) + return_dict['cash']

    return JsonResponse(return_dict)
