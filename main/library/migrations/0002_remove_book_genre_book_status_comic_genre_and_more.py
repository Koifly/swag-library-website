# Generated by Django 5.0.1 on 2024-01-31 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='genre',
        ),
        migrations.AddField(
            model_name='book',
            name='status',
            field=models.CharField(choices=[('Y', 'Available'), ('H', 'Borrowed'), ('N', 'Unavailable')], default='Available', max_length=1),
        ),
        migrations.AddField(
            model_name='comic',
            name='genre',
            field=models.CharField(choices=[('OTH', 'Other'), ('BAT', 'Batman')], default='Other', max_length=3),
        ),
        migrations.AddField(
            model_name='manga',
            name='genre',
            field=models.CharField(choices=[('OTH', 'Other'), ('ADV', 'Adventure'), ('CRI', 'Crime'), ('FAN', 'Fantasy'), ('HOR', 'Horror'), ('ROM', 'Romance'), ('SCI', 'Science-Fiction'), ('SHJ', 'Shoujo'), ('SHN', 'Shounen'), ('THR', 'Thriller')], default='Other', max_length=3),
        ),
        migrations.AddField(
            model_name='nonfiction',
            name='genre',
            field=models.CharField(choices=[('OTH', 'Other'), ('ART', 'Art'), ('ARC', 'Architecture'), ('BOT', 'Botany'), ('CLI', 'Climate'), ('FIN', 'Finance'), ('HIS', 'History'), ('HIT', 'Historical text'), ('MAT', 'Maths'), ('PHI', 'Philosophy'), ('PHY', 'Physics'), ('POL', 'Politics'), ('SOC', 'Sociology'), ('TEC', 'Technology')], default='Other', max_length=3),
        ),
        migrations.AddField(
            model_name='novel',
            name='genre',
            field=models.CharField(choices=[('OTH', 'Other'), ('ADV', 'Adventure'), ('CRI', 'Crime'), ('FAN', 'Fantasy'), ('FOL', 'Folklore'), ('HOR', 'Horror'), ('ROM', 'Romance'), ('SAT', 'Satire'), ('SCI', 'Science-Fiction'), ('THR', 'Thriller'), ('YA', 'Y/A')], default='Other', max_length=3),
        ),
        migrations.AlterField(
            model_name='book',
            name='blurb',
            field=models.CharField(blank=True, default='', max_length=1000),
        ),
    ]
