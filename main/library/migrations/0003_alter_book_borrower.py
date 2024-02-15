# Generated by Django 5.0.2 on 2024-02-15 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_alter_book_borrower'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='borrower',
            field=models.CharField(blank=True, choices=[('R', 'Rayen'), ('D', 'Don'), ('C', 'Charlie'), ('S', 'Sam'), ('H', 'Honey'), ('A', 'Ash'), ('O', 'Soph'), ('N', 'None')], default='None', max_length=1, null=True),
        ),
    ]
