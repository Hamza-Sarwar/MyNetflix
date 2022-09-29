from django.urls import path
from .views import CategoryAPIView, CategoryDetailAPIView

urlpatterns = [
    path("",CategoryAPIView.as_view()),
    path("<int:id>",CategoryDetailAPIView.as_view()),
]