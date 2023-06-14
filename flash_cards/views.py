from django.shortcuts import render, redirect, get_object_or_404

from .models import Topic, SubTopic, CardQuestion, Choice, Resource
from .forms import TopicForm, SubtopicForm

import random

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
    topic = get_object_or_404(Topic, id=topic_id)
    subtopics = SubTopic.objects.filter(topic__id=topic_id)
    context = {'subtopics': subtopics, 'topic': topic}
    return render(request, 'flash_cards/subtopics.html', context)

def new_topic(request):
    """Add a new topic"""
    if request.method != 'POST':
        # No data submitted; create a blank form
        form = TopicForm()
    else:
        # POST data submitted; process data
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('flash_cards:topics')
    
    # Display blank or invalid form
    context = {'form': form}
    return render(request, 'flash_cards/new_topic.html', context)

def new_subtopic(request, topic_id):
    """Add a new topic"""
    topic = get_object_or_404(Topic, id=topic_id)
    if request.method != 'POST':
        # No data submitted; create a blank form
        form = SubtopicForm(initial={'topic': topic})
    else:
        # POST data submitted; process data
        form = SubtopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('flash_cards:subtopics', topic.id)
    
    # Display blank or invalid form
    context = {'topic': topic, 'form': form}
    return render(request, 'flash_cards/new_subtopic.html', context)

def start_quiz(request):
    """select 10 questions from the selected topics and start the quiz"""
    selected_subtopics = request.POST.getlist('subtopics')
    questions = CardQuestion.objects.filter(subtopic__id__in=selected_subtopics)
    questions = random.sample(list(questions), 10)
    questions_list = []
    for question in questions:
        questions_list.append(question.id)
    request.session['question_ids'] = questions_list
    context = {'questions': questions}
    return render(request, 'flash_cards/quiz.html', context)

def results(request):
    """show the results of the quiz"""
    quiz_answers = {}
    for key in request.POST:
        if key.startswith('answers_'):
            question_id = key.split('_')[1]
            quiz_answers[question_id] = request.POST.getlist(key)
    question_ids = request.session['question_ids']
    questions = CardQuestion.objects.filter(id__in=question_ids)
    total_score = 0
    max_possible_score = 0

    results = []
    for question in questions:
        all_choices = list(question.choices.all())
        user_answers = quiz_answers.get(str(question.id), [])
        correct_answers = list(question.choices.filter(is_correct=True))
        
        result = {
            'question_text': question.text,
            'choices': [],
        }

        for choice in all_choices:
            if choice.is_correct:
                max_possible_score += 1
            if choice.text in user_answers:
                if choice.is_correct:
                    marking = "correct"
                    total_score += 1
                else:
                    marking = "incorrect"
            elif choice.text not in user_answers:
                if choice.is_correct:
                    marking = "not selected: incorrect"
                else:
                    marking = "not selected: correct"
            result['choices'].append({
                'text': choice.text,
                'marking': marking
            })
        results.append(result)

    context = {
        'results': results,
        'total_score': total_score,
        'max_possible_score': max_possible_score
        }
    return render(request, 'flash_cards/results.html', context)