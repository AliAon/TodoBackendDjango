from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from app import views
# router=DefaultRouter()
# router.register('todo', views.TodoViewset,basename="todo")
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('app.urls')),
]
