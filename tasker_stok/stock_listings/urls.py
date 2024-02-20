from django.urls import path
from . import views

urlpatterns = [
    path('listings/create/', views.listing_create, name='listing_create'),
    path('listings/', views.listing_list, name='listing_list'),
    path('listings/<int:pk>/', views.listing_detail, name='listing_detail'),
]