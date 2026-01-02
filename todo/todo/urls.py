from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.signup, name='home'),
    path('loginn/', views.login_view, name='login'),
    path('todo/', views.todo, name='todo'),
    path('edit_todo/<int:srno>', views.edit_todo, name='edit_todo'),
    
]
