# Generated by Django 4.0.1 on 2023-10-09 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0003_book_describe'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='read_book',
            field=models.CharField(choices=[('Tak', 'Tak'), ('Nie', 'Nie')], max_length=3, null=True),
        ),
    ]
