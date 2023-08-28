from django.db import models
from django.conf import settings
from django.utils import timezone


# Create your models here.
class Flashcard(models.Model):
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return self.question