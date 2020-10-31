from django.urls import path
from todo_john import views

urlpatterns = [
    path('todo', views.todo, name='todo'),
    path('delete_todo/<int:id>/', views.delete_todo, name='delete_todo'),
    # path('myposts', views.myposts, name='myposts'),
    # path('edit_post/<int:id>/', views.edit_post, name='edit_post'),
    # path('about', views.about, name='about'),
    # path('contact', views.contact, name='contact'),
    # path('addpost', views.addpost, name='addpost'),
]
