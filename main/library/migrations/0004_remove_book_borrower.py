# Generated by Django 5.0.2 on 2024-02-15 19:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_alter_book_borrower'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='borrower',
        ),
    ]
