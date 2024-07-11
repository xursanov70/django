from django.urls import path
from .views import HomePageView
from .views import AboutPageView
from .views import BasePageView

urlpatterns =  [
    path('home', HomePageView.as_view(), name = 'home'),
    path('', BasePageView.as_view(), name = 'base'),
    path('about', AboutPageView.as_view(), name = 'about')
]

