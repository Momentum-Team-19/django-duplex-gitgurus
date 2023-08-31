from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Deck(models.Model):
    category = models.CharField(max_length=250)
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="decks", blank=True, null=True)

    def __str__(self):
        return self.category

    @property
    def get_score(deck):
        right_answers = 0
        wrong_answers = 0
        not_answered = 0
        for card in deck.flashcards.all():
            if card.correct:
                right_answers += 1
            elif card.correct == False:
                wrong_answers += 1
            else:
                not_answered += 1
        return (right_answers, wrong_answers, not_answered)
 

class Flashcard(models.Model):
    question = models.TextField()
    answer = models.TextField()
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE, related_name="flashcards", blank=True, null=True)
    correct = models.BooleanField(blank=True, null=True)

    def __str__(self):
        return self.question


class User(AbstractUser):
    pass
