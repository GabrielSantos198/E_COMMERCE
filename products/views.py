from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Category, Product
from cart.cart import Cart

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
       return Product.objects.filter(category__slug=self.kwargs['slug'], is_available=True).order_by('-modified')


# Cart
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("products:cart_detail")


def cart_detail(request):
    return render(request, 'cart/cart_detail.html')


def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("products:cart_detail")


def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("products:cart_detail")


def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("products:cart_detail")


def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("products:cart_detail")
