# Generated by Django 5.0.1 on 2024-02-04 19:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0007_booktype_genre_newbook'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='comic',
            name='book_ptr',
        ),
        migrations.RemoveField(
            model_name='manga',
            name='book_ptr',
        ),
        migrations.RemoveField(
            model_name='nonfiction',
            name='book_ptr',
        ),
        migrations.DeleteModel(
            name='Novel',
        ),
        migrations.DeleteModel(
            name='Comic',
        ),
        migrations.DeleteModel(
            name='Manga',
        ),
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.DeleteModel(
            name='NonFiction',
        ),
    ]