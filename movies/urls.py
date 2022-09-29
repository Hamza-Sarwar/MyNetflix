from django.urls import path
from .views import MovieAPIView, MovieDetailAPIView

urlpatterns = [
    path("", MovieAPIView.as_view()),
    path("<int:id>", MovieDetailAPIView.as_view()),
]