from django.db import models
from django.conf import settings
from django.utils import timezone


# Create your models here.

class Deck(models.Model):
    category = models.CharField(max_length=250)

    def __str__(self):
        return self.category
    

class Flashcard(models.Model):
    question = models.TextField()
    answer = models.TextField()
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE, related_name="flashcards", blank=True, null=True)

    def __str__(self):
        return self.question