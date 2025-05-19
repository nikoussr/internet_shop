from django.urls import path
from .views import HomePageView, CategoriesListView, ProductListView, CustomersListView


urlpatterns = [
    path('', HomePageView.as_view(), name = 'index'),
    path('categories', CategoriesListView.as_view(), name='categories'),
    path('customers', CustomersListView.as_view(), name='customers'),
    path('products', ProductListView.as_view(), name='products'),
]