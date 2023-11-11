from django.urls import path

from apps.user import views

urlpatterns = [
    path("login", views.Login.as_view(), name="login"),
]
