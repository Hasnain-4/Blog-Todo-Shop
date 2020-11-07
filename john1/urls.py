from django.urls import path
from john1 import views

urlpatterns = [
    path('', views.home, name='home'),
    path('myposts', views.myposts, name='myposts'),
    path('edit_post/<int:id>/', views.edit_post, name='edit_post'),
    path('delete_post/<int:id>/', views.delete_post, name='delete_post'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('addpost', views.addpost, name='addpost'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin')
]
