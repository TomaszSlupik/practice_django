from django.db import models

# Create your models here.
class Book (models.Model):

    title = models.CharField(max_length=20)
    describe = models.CharField(max_length=300, blank=True)

    OPINION_CHOICES = (
        ('bardzo_dobra', 'Bardzo dobra'),
        ('dobra', 'Dobra'),
        ('przecietna', 'Przeciętna'),
        ('słaba', 'Słaba'),
    )

    opinion = models.CharField(max_length=20, choices=OPINION_CHOICES, null=True)

    READ_BOOK = (
        ("Tak", "Tak"),
        ("Nie", "Nie")
    )

    read_book = models.CharField(max_length=3, choices=READ_BOOK, null=True)

    def __str__(self):
        return self.title
    

