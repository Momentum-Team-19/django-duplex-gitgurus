"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from flashcards import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.deck_list, name="deck_list"),
    path('flashcards/<int:pk>', views.flashcard_answer, name='flashcard_answer'),
    path('flashcard/new', views.flashcard_new, name='flashcard_new'),
    path('flashcard/<int:pk>/edit', views.flashcard_edit, name='flashcard_edit'),
    path('deck/new', views.deck_new, name="deck_new"),
    path('deck/<int:pk>/detail', views.deck_detail, name='deck_detail'),
    path('flashcard/list', views.flashcard_list, name="flashcard_list"),
    path('flashcards/<int:flashcard_pk>/mark-right/', views.mark_right_answer, name="mark_right_answer"),
    path('flashcards/<int:flashcard_pk>/mark-wrong/', views.mark_wrong_answer, name='mark_wrong_answer'),
    path('accounts/', include('registration.backends.simple.urls')),
    path('deck/<int:pk>/reset', views.reset_deck, name='reset_deck'),
]
