# Generated by Django 4.2.4 on 2023-08-29 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flashcards', '0002_deck_flashcard_deck'),
    ]

    operations = [
        migrations.AddField(
            model_name='deck',
            name='category',
            field=models.CharField(default='test', max_length=250),
            preserve_default=False,
        ),
    ]
