from django.shortcuts import render, redirect, get_object_or_404
from .models import Flashcard, Deck
from .forms import FlashcardForm, DeckForm
from django.contrib.auth.decorators import login_required


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
            return redirect('deck_list')
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


def deck_new(request):
    if request.method == "POST":
        form = DeckForm(request.POST)
        if form.is_valid():
            deck = form.save()
            return redirect('deck_list')
    else:
        form = DeckForm()
        return render(request, 'deck_new.html', {'form': form})


def deck_detail(request, pk):
    deck = get_object_or_404(Deck, pk=pk)
    right = deck.get_score[0]
    wrong = deck.get_score[1]
    not_answered = deck.get_score[2]
    context = {
        'deck': deck,
        'right': right,
        'wrong': wrong,
        'not_answered': not_answered
    }
    return render(request, 'deck_detail.html', context)


@login_required
def deck_list(request):
    decks = Deck.objects.all()
    return render(request, 'deck_list.html', {'decks': decks})


def mark_right_answer(request, flashcard_pk):
    flashcard = get_object_or_404(Flashcard, pk=flashcard_pk)
    flashcard.correct = True 
    flashcard.save()
    return redirect('deck_detail', pk=flashcard.deck.pk)


def mark_wrong_answer(request, flashcard_pk):
    flashcard = get_object_or_404(Flashcard, pk=flashcard_pk)
    flashcard.correct = False
    flashcard.save()
    return redirect('deck_detail', pk=flashcard.deck.pk)


