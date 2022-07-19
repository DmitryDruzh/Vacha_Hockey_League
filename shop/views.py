from django.forms import BaseForm
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.decorators.http import require_POST
from django.views.generic import ListView, DetailView, FormView, CreateView

from shop.models import Product, OrderItem, Order
from .cart import Cart
from .forms import CartAddProductForm, OrderCreateForm
from .tasks import your_order_created


class AllProducts(ListView):
    model = Product
    template_name = 'shop/all_products.html'
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'All products'
        return context


class ProductDetail(DetailView):
    model = Product
    template_name = 'shop/product_detail.html'
    slug_url_kwarg = 'slug'
    context_object_name = 'product'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Информация по товару ' + str(Product.objects.get(slug=self.kwargs['slug']))
        context['cart_add_product_form'] = CartAddProductForm()
        return context


# def product_detail(request, slug):
#     product = Product.objects.get(slug=slug)
#     product_add_to_cart_form = CartAddProductForm()
#     return render(request, 'shop/product_detail.html', {'product': product,
#                                                         'form': product_add_to_cart_form})

@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart-detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart-detail')


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'shop/cart.html', {'cart': cart})


class ConfirmationView(DetailView):
    model = Order
    template_name = 'shop/confirmation.html'
    context_object_name = 'order'
    pk_url_kwarg = 'id'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orderitems'] = OrderItem.objects.filter(order_id=self.kwargs['id'])
        return context


class CreateOrder1(CreateView):
    model = Order
    form_class = OrderCreateForm
    template_name = 'shop/checkout.html'

    def form_valid(self, form):
        cart = Cart(self.request)
        order = form.save()
        for item in cart:
            OrderItem.objects.create(order=order,
                                     product=item['product'],
                                     price=item['price'],
                                     quantity=item['quantity'])
        cart.clear()
        your_order_created.delay(order.id)
        return super().form_valid(form)
