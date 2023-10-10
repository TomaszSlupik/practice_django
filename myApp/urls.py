from django.urls import path
from . import views
from .views import Second

urlpatterns = [
    path("", views.test_book),
    path('second', Second.as_view()),
    path('third', views.testTempate),
]