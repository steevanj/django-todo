from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.signup, name='default'),                  
    path('signup/', views.signup, name='signup'),            
    path('admin/', admin.site.urls),
    path('login/', views.login_view, name='login'),
    path('todo/', views.todoapp, name='todoapp'),
    path('edit_todo/<int:srno>', views.edit_todo, name='edit_todo'),
    path('delete_todo/<int:srno>', views.delete_todo, name='delete_todo'),
    path('signout/', views.signout, name='signout'),
]
