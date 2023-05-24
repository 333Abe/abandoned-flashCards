from django.shortcuts import render

from .models import Topic, SubTopic, CardQuestion, Choice, Resource

def index(request):
    """flashCards home page"""
    return render(request, 'flash_cards/index.html')

def topics(request):
    """Show all topics"""
    topics = Topic.objects.all()
    context = {'topics': topics}
    return render(request, 'flash_cards/topics.html', context)