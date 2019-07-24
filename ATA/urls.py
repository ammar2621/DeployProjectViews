from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('mentor/', views.listmentor, name='mentor'),
    path('mentee/', views.listmentee, name='mentee'),
    path('author/', views.Author, name='author'),
    path('blog/', views.listblog, name='blog'),
    path('mentor/input/', views.input_mentor, name='inputmentor'),
    path('mentee/input/', views.input_mentee, name='inputmentee'),
    path('blog/input/', views.input_blog, name='inputblog'),
    path('blog/<int:blog_id>/', views.blog_detail, name='blog_detail'),
]
