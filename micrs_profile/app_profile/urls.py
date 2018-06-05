from django.urls import path

from .views import ProfileDetail, ProfileList

urlpatterns = [
    path('profile/<int:pk>', ProfileDetail.as_view(), name='profile-detail'),
    path('profile', ProfileList.as_view(), name='profile-list'),
]