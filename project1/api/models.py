from django.db import models

import random
from hashlib import md5

# a function to generate a new random api token
def new_api_token(n=8):
    digest = ''

    for i in range(n):
        s = f'{random.random():.32f}'
        s = s.encode()

        digest += md5(s).hexdigest()

    return digest

# the class containing a portfolio of stocks
class PortfolioModel(models.Model):
    class Meta:
        app_label = 'api'
    
    cash = models.IntegerField(default=100000)

# the class containing your user information (including their api token and password, etc)
class UserModel(models.Model):
    class Meta:
        app_label = 'api'

    first_name = models.CharField(max_length=128, null=True)
    last_name = models.CharField(max_length=128, null=True)
    api_token = models.CharField(max_length=256, default=new_api_token())
    password = models.CharField(max_length=256, null=True)
    username = models.CharField(max_length=256, null=True)

    portfolio = models.OneToOneField(PortfolioModel, on_delete=models.CASCADE, )

# a class containing what happened in a purchase (who made it, when it was made, what it traded)
class PurchaseModel(models.Model):
    class Meta:
        app_label = 'api'

    timestamp = models.DateTimeField(auto_now_add=True, null=True)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True)
    symbol = models.CharField(max_length=8, null=True)
    price = models.FloatField(null=True)
    quantity = models.IntegerField(null=True)

# a class containing a simple set of data on a stock within a portfolio
class StockModel(models.Model):
    class Meta:
        app_label = 'api'
    
    portfolio = models.ForeignKey(PortfolioModel, on_delete=models.CASCADE, null=True)
    symbol = models.CharField(max_length=8, null=True)
    quantity = models.IntegerField(null=True)