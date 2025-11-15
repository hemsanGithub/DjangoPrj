
from django.urls import path
from .import views

urlpatterns = [
    
    path('', views.djapp, name='django_app_home'),
    path('<int:chai_id>/', views.chai_detail, name='django_chai_detail'),
    path('chai_stores/', views.chai_stores_view, name='django_chai_stores'),
]