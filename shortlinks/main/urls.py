from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.ContactFormView.as_view(), name='contact'),
    path('about/', views.about, name='about'),
    path('links/', views.LinksView.as_view(), name='links'),
]
