# Generated by Django 3.1.5 on 2021-02-03 01:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_remove_book_language0'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='language',
        ),
    ]
