from django.urls import path, re_path
from . import views
from .views import LoginView, RegisterView, ProfilePage

urlpatterns = [
    re_path(r'^accounts/register/$', RegisterView.as_view(), name='register'),
    re_path(r'^accounts/login/$', LoginView.as_view(), name='login'),
    re_path(r'^accounts/profile/$', ProfilePage.as_view(), name='profile'),
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]
