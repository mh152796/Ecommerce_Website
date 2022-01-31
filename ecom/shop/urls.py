from django.urls import path, include
from . import views
from django.views.generic import TemplateView

from django.views.static import serve


urlpatterns = [
    path('', views.index, name='index'),
    path("test/", TemplateView.as_view(template_name="test.html"), name="test"),
    path("about/", TemplateView.as_view(template_name="about.html"), name="about"),
    path('detail/<str:pk>/',views.detail, name="detail"),
    path("add-item/",views.additem, name="add-item"),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('editItem/<str:pk>/', views.editItem, name='editItem'),
    path('delete-item/<str:pk>/', views.deleteItem, name='delete-item'),
    path('register/', views.registerUser, name='register'),
]