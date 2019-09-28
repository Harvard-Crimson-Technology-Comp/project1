from django.shortcuts import render

from django.http import HttpResponseNotFound

"""
This is an example of how these might look! Eventually all of this will be done in React :)
"""

# the default page that your users would land on
def index(request):
    return HttpResponseNotFound('WEB: INDEX: MOVED')

# the registration page for your users
def register(request):
    return HttpResponseNotFound('WEB: REGISTER: MOVED')

# the login page for users
def login(request):
    return HttpResponseNotFound('WEB: LOGIN: MOVED')

# logs out the current user
def logout(request):
    return HttpResponseNotFound('WEB: LOGOUT: MOVED')

# displays a dashboard of the stocks the user owns
def dashboard(request):
    return HttpResponseNotFound('WEB: DASHBOARD: MOVED')

# allows the user to buy or sell stocks
def trade(request):
    return HttpResponseNotFound('WEB: TRADE: MOVED')