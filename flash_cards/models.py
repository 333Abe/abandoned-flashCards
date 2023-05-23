from django.db import models

class Topic(models.Model):
    """cards are grouped by topic and subtopic"""
    text = models.CharField(max_length=200)
    
    def __str__(self):
        return self.text

class SubTopic(models.Model):
    topic = models.ForeignKey(Topic, related_name='subtopics', on_delete=models.CASCADE)
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text

class CardQuestion(models.Model):
    QUESTION_TYPES = [
        ('MC', 'Multiple Choice'),
    ]

    subtopic = models.ForeignKey(SubTopic, related_name='cards', on_delete=models.CASCADE)
    text = models.TextField()
    question_type = models.CharField(max_length=2, choices=QUESTION_TYPES, default='MC')

    def __str__(self):
        return self.text
    
class Choice(models.Model):
    question = models.ForeignKey(CardQuestion, related_name='choices', 
                                 on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)