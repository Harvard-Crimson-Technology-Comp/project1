# TODO! You'll need to add the GraphQL schema for your project here!
from graphene_django import DjangoObjectType
import graphene

from project1.api.models import UserModel, PortfolioModel, StockModel, PurchaseModel

class User(DjangoObjectType):
    class Meta:
        model = UserModel

class Portfolio(DjangoObjectType):
    class Meta:
        model = PortfolioModel

class Stock(DjangoObjectType):
    class Meta:
        model = StockModel

class Purchase(DjangoObjectType):
    class Meta:
        model = PurchaseModel

class Query(graphene.ObjectType):
    users = graphene.List(User)
    portfolios = graphene.List(Portfolio)
    purchases = graphene.List(Purchase)
    stocks = graphene.List(Stock)

    def resolve_users(self, info):
        return UserModel.objects.all()

    def resolve_portfolios(self, info):
        return PortfolioModel.objects.all()

    def resolve_purchases(self, info):
        return PurchaseModel.objects.all()

    def resolve_stocks(self, info):
        return StockModel.objects.all()
    

