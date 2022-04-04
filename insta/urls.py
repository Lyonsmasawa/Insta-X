from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('post/<str:pk>/', views.post, name="post"),
    path('create-post/', views.createPost, name="create-post"),
    path('update-post/<str:pk>/', views.updatePost, name="update-post"),
    path('delete-post/<str:pk>/', views.deletePost, name="delete-post"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),
    path('profile/<str:pk>', views.userProfile, name="profile"),
    path('delete-comment/<str:pk>/', views.deleteComment, name="delete-comment"),
    path('update-user/', views.updateUser, name="update-user"),   
    
]