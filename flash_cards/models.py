from django.db import models

class Topic(models.Model):
    """cards are grouped by topic and subtopic"""
    text = models.CharField(max_length=200)
    
    def __str__(self):
        return self.text