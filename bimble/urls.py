from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('blog/', views.blog, name='blog'),
    path('jam_kerja/', views.jam_kerja, name='jam_kerja'),
    path('contact/', views.contact, name='contact'),
    path('children/', views.children_list, name='children_list'),
]