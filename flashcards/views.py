from django.shortcuts import render, redirect, get_object_or_404
from .models import Flashcard
from .forms import FlashcardForm

# Create your views here.
def flashcard_list(request):
    flashcards = Flashcard.objects.all()
    return render(request, 'flashcard_list.html', {'flashcards': flashcards})


def flashcard_answer(request, pk):
    flashcard = Flashcard.objects.get(pk=pk)
    return render(request, 'flashcard_answer.html', {'flashcard': flashcard})


def flashcard_new(request):
    if request.method == "POST":
        form = FlashcardForm(request.POST)
        if form.is_valid():
            flashcard = form.save()
            return redirect('flashcard_list')
    else:
        form = FlashcardForm()
        return render(request, 'flashcard_new.html', {'form': form})
    

def flashcard_edit(request, pk):
    flashcard = get_object_or_404(Flashcard, pk=pk)
    if request.method == "POST":
        form = FlashcardForm(request.POST, instance=flashcard)
        if form.is_valid():
            flashcard = form.save()
            return redirect('flashcard_list')
    else:
        form = FlashcardForm(instance=flashcard)
    return render(request, 'flashcard_edit.html', {'form': form})
