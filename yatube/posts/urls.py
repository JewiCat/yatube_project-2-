from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name = 'prime'),
    path('group/', views.group_posts, name ='group')
]