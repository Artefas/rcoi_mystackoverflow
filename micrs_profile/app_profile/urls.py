from django.urls import path

from .views import ProfileListCreateAPIView, ProfileDetailAPIView, ProfileUpdateAPIView
# from .view import

urlpatterns = [
    path('profile', ProfileListCreateAPIView.as_view(), name='profile-list-create'),
    path('profile/<int:pk>', ProfileDetailAPIView.as_view(), name='profile-detail'),
    path('profile/<int:pk>/edit', ProfileUpdateAPIView.as_view(), name='profile-detail'),
    # path('login', )
]