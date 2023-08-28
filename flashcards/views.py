from django.shortcuts import render
from .models import Flashcard


# Create your views here.
def flashcard_list(request):
    flashcards = Flashcard.objects.all()
    return render(request, 'flashcard_list.html', {'flashcards': flashcards})