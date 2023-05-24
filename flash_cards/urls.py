"""flash_cards app urls defined below"""

from django.urls import path

from . import views

app_name = 'flash_cards'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
]