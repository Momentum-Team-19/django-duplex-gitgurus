from django import forms
from .models import Flashcard, Deck


class FlashcardForm(forms.ModelForm):
    class Meta:
        model = Flashcard
        fields = ('question', 'answer', 'deck')


class DeckForm(forms.ModelForm):
    class Meta:
        model = Deck
        fields = ('category',)