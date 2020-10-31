from django.urls import path
from ecommerce import views

urlpatterns = [
    path('shop', views.shop, name='shop'),
    # path('myposts', views.myposts, name='myposts'),
    # path('edit_post/<int:id>/', views.edit_post, name='edit_post'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('delete1/<int:id>/', views.delete1, name='delete1'),
    path('delete2/<int:id>/', views.delete2, name='delete2'),
    path('viewitem/<int:id>', views.viewitem, name='viewitem'),
    path('viewitem1/<int:id>', views.viewitem1, name='viewitem1'),
    path('viewitem2/<int:id>', views.viewitem2, name='viewitem2'),
    # path('contact', views.contact, name='contact'),
    # path('addpost', views.addpost, name='addpost'),
]
