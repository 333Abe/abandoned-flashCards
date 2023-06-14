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
    # New subtopic page
    path('topics/<int:topic_id>/new_subtopic/', views.new_subtopic, name='new_subtopic'),
    # Quiz page
    path('quiz/', views.start_quiz, name='start_quiz'),
    # Results page
    path('results/', views.results, name='results')
]