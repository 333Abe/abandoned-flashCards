from django.shortcuts import render, redirect

from .models import Topic, SubTopic, CardQuestion, Choice, Resource
from .forms import TopicForm

def index(request):
    """flashCards home page"""
    return render(request, 'flash_cards/index.html')

def topics(request):
    """Show all topics"""
    topics = Topic.objects.all()
    context = {'topics': topics}
    return render(request, 'flash_cards/topics.html', context)

def subtopics(request, topic_id):
    """Show all subtopics for a topic"""
    subtopics = SubTopic.objects.filter(topic__id=topic_id)
    context = {'subtopics': subtopics}
    return render(request, 'flash_cards/subtopics.html', context)

def new_topic(request):
    """Add a new topic"""
    if request.method != 'POST':
        # No data submitted; create a blank form
        form = TopicForm()
    else:
        # POST data submitted; process data
        if form.is_valid():
            form.save()
            return redirect('flash_cards:topics')
    
    # Display blank or invalid form
    context = {'form': form}
    return render(request, 'flash_cards/new_topic.html', context)

