
from django.urls import path
from .views import UserAPI,RegisterUserAPIView, LoginAPI
from knox import views as knox_views

urlpatterns = [
  path("", UserAPI.as_view()),
  path('register/', RegisterUserAPIView.as_view()),
  path('login/', LoginAPI.as_view()),
  path('logout/', knox_views.LogoutView.as_view()),
]