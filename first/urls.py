from django.contrib import admin
from django.urls import path
from myApp.views import test_book

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', test_book)
]
