from django.urls import path, include
from .views import HomePageView, CategoriesListView, ProductListView, CustomersListView, SearchView, AllProducts
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('categories', CategoriesListView.as_view(), name='categories'),
    path('customers', CustomersListView.as_view(), name='customers'),
    path('search', SearchView.as_view(), name='search'),
    path('cart/', include('cart.urls', namespace='cart')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('products', AllProducts.as_view(), name='products'),

]


urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)