# Generated by Django 4.0.1 on 2023-10-07 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0002_book_opinion'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='describe',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
