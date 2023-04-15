from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from cart.forms import CartForm
from .models import Product, Category


class HomeView(ListView):
    model = Product
    template_name = 'product/index.html'

    def get_context_data(self, **kwargs):
        categories = Category.objects.all()
        context = super(HomeView, self).get_context_data()
        context['categories'] = categories
        return context


def product_detail(request, pk):
    product = get_object_or_404(Product,
                                id=pk,
                                available=True)
    categories = Category.objects.all()
    cart_product_form = CartForm()
    return render(request, 'product/detail.html', {'product': product,
                                                   'categories': categories,
                                                   'cart_product_form': cart_product_form})


def category_view(request, cat_id):
    products = Product.objects.filter(category_id=cat_id)
    categories = Category.objects.all()
    return render(request, 'product/categories.html', {'products': products,
                                                       'categories': categories})
