from knox import views as knox_views
from .views import LoginAPI, RegisterAPI, UserAPI, ChangePasswordView, PostAPI
from django.urls import path
from . import views

urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('api/user/', UserAPI.as_view(), name='user'),
    path('api/change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('users-list', views.usersList, name="users-list"),
    path('api/create-post/', PostAPI.as_view(), name="create-post"),
    # path('api/get-list-posts/', views.postList, name="get-list-posts"),
    path('api/get-list-posts/', PostAPI.as_view(), name="create-post"),
]
