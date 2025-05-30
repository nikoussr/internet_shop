from django.urls import path, include
from . import views

app_name = 'orders'

urlpatterns = [

    path('create/', views.order_create, name='order_create'),
    path('success/<int:order_id>/', views.order_success, name='order_success'),
]