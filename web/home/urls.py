from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('index', index),
    # path('pricing', pricing),
    # path('about', about),
    # path('contacts', contacts),
    # path('feedback', feedback),
]