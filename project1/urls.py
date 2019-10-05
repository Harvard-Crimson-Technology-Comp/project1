"""project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from graphene_django.views import GraphQLView

import project1.api.views as api_views
import project1.web.views as web_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphql', GraphQLView.as_view(graphiql=True)),

    ### this section redirects control flow to the API app in Django
    path('api/buy', api_views.buy), # should allow "buy"
    path('api/sell', api_views.sell), # should allow "sell"
    path('api/list', api_views.list), # should allow "list"
    path('api/register', api_views.register), # should allow "register"

    ### this section redirects control flow to the Web app in Django - will be deprecated!
    path('register', web_views.register),
    path('login', web_views.login),
    path('logout', web_views.logout),
    path('dashboard', web_views.dashboard),
    path('trade', web_views.trade),
    path('', web_views.index)
]
