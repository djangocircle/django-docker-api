from django.urls import path

from .views import UserDetailView

urlpatterns = [
    path('user-detail', UserDetailView.as_view(), name="user-detail"),
]
