from django import forms

from .models import Topic, SubTopic

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}

class SubtopicForm(forms.ModelForm):
    class Meta:
        model = SubTopic
        fields = ['topic', 'text']