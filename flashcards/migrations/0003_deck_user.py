# Generated by Django 4.2.4 on 2023-08-31 15:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flashcards', '0002_remove_flashcard_right_answers_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='deck',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='decks', to=settings.AUTH_USER_MODEL),
        ),
    ]
