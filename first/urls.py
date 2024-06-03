
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_first, name='all_first'),
    path('<int:first_id>/', views.first_detail, name='first_detail'),
    path('first_stores/', views.first_store_review, name='first_stores'),

    
]
