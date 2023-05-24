from django.contrib import admin

from .models import Topic, SubTopic, CardQuestion, Choice, Resource

admin.site.register(Topic)
admin.site.register(SubTopic)
admin.site.register(CardQuestion)
admin.site.register(Choice)
admin.site.register(Resource)