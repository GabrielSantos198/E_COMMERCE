from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Category, Product

# Create your views here.
class ProductListView(ListView):
    paginate_by = 9
    queryset = Product.objects.filter(is_available=True).order_by('-modified')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class ProductDetailView(DetailView):
    model = Product


class CategoriesListView(ListView):
    paginate_by = 9

    def get_queryset(self):
       return Product.objects.filter(category__slug=self.kwargs['slug']).order_by('-modified')
