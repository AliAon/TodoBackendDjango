from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from app import views

urlpatterns = [
    path('todos', views.TodoList.as_view()),
    path('todos/<int:id>', views.TodoDetail.as_view())
]
