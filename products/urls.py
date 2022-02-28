from django.urls import path
from .views import ProductDetailView, ProductListView, CategoriesListView

app_name = 'products'

urlpatterns = [
    path('', ProductListView.as_view(), name='list'),
    path('<slug:slug>/', ProductDetailView.as_view(), name='detail'),
    path('category/<slug:slug>/', CategoriesListView.as_view(), name='categories'),
]
