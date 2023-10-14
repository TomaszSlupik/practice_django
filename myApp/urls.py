from django.urls import path, include
from . import views
from .views import Second, BookViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('books', BookViewSet)


urlpatterns = [
    path("", views.test_book),
    path('second', Second.as_view()),
    path('third', views.testTempate),
    path('dynamic', views.testDynamic),
    path("serializer", include(router.urls))
]
