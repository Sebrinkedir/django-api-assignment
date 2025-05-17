from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile_view, name='profile'),
    path('profile/update/', views.profile_update, name='profile_update'),   
    path('register/', views.register, name='register'),
    path('', views.post_list, name='post_list'),  # age showing the list of posts
    path('<int:pk>/', views.post_detail, name='post_detail'),  
    path('add/', views.post_create, name='post_create'),  #  to add a new post
    path('<int:pk>/edit/', views.post_update, name='post_update'),  #  to edit an existing post
    path('<int:pk>/delete/', views.post_delete, name='post_delete'),  #  to delete a post
]


