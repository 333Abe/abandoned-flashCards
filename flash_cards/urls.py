"""flash_cards app urls defined below"""

from django.urls import path

from . import views

app_name = 'flash_cards'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Topics page
    path('topics/', views.topics, name='topics'),
    # Subtopics page
    path('topics/<int:topic_id>/subtopics/', views.subtopics, name='subtopics'),
    # New topic page
    path('new_topic/', views.new_topic, name='new_topic'),
]