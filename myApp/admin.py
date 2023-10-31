from django.contrib import admin
from .models import Book, MoreInfoBook, Character

# Register your models here.
# admin.site.register(Book)

# Register your models here.
@admin.register(Book)
class BookAdmin (admin.ModelAdmin):
    list_display = ["title", "opinion"]
    search_fields=["title"]

@admin.register(MoreInfoBook)
class MoreInfoBookAdmin (admin.ModelAdmin):
    list_display = ["more_info"]


@admin.register(Character)
class CharacterAdmin (admin.ModelAdmin):
    list_display = ["name", "book"]