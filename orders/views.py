from django.shortcuts import render, redirect, reverse
from django.views.generic.edit import CreateView
from django.shortcuts import get_object_or_404

from cart.cart import Cart

from .models import Order, Item

# Create your views here.
class OrderCreateView(CreateView):
    model = Order
    fields = ('cpf', 'name', 'email', 'postal_code', 'address', 'number',
              'complement', 'district', 'state', 'city')

    def get_success_url(self):
        return reverse('orders:salvar')


def salvar(request):
    total = Order.objects.all()
    id = 1
    for c in total:
        id = c.id
    obj = Order.objects.get(pk=id)
    for item in Cart(request).session['cart'].values():
        Item.objects.create(order=obj, product=item['product_id'], quantity=item['quantity'])
    del Cart(request).session['cart']
    return redirect('pages:home')

