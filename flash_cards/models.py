from django.db import models

class Topic(models.Model):
    """cards are grouped by topic and subtopic"""
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text

class SubTopic(models.Model):
    topic = models.ForeignKey(Topic, 
                              related_name='subtopics', 
                              on_delete=models.CASCADE)
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text

class CardQuestion(models.Model):
    QUESTION_TYPES = [
        ('MC', 'Multiple Choice'),
        # ('FB', 'Fill in the Blanks'),
    ]

    subtopic = models.ForeignKey(SubTopic, 
                                 related_name='cards', 
                                 on_delete=models.CASCADE)
    text = models.TextField()
    question_type = models.CharField(max_length=2, 
                                     choices=QUESTION_TYPES, 
                                     default='MC')
    resource = models.ForeignKey('Resource', 
                                 related_name='questions', 
                                 null=True, blank=True, 
                                 on_delete=models.SET_NULL)

    def __str__(self):
        return (f"{self.subtopic.topic.text} > "
                f"{self.subtopic.text} > {self.text}")

class Choice(models.Model):
    question = models.ForeignKey(CardQuestion, 
                                 related_name='choices', 
                                 on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return (f"{self.question.subtopic.topic.text} > "
                f"{self.question.subtopic.text} > {self.question.text} > "
                f"{self.text} > "
                f"{'Correct' if self.is_correct else 'Incorrect'}")

class Resource(models.Model):
    subtopic = models.ForeignKey(SubTopic, 
                                 related_name='resources', 
                                 null=True, 
                                 on_delete=models.SET_NULL)
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return f"{self.title}"