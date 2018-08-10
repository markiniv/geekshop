from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
from django.views.generic import TemplateView, DetailView, ListView

from .models import Product, Category
from basketapp.models import Basket


CONTENT = {}


def menu():
    return [
            {'name': 'главная', 'href': '/'},
            {'name': 'каталог', 'href': '/catalog/'},
            {'name': 'контакты', 'href': '/contacts/'},
            {'name': 'корзина', 'href': '/basket/'}
        ]


def products():
    return Product.objects.all()


def product(pk):
    return get_object_or_404(Product, pk=pk)


class IndexView(TemplateView):
    template_name = 'mainapp/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['title'] = 'Главная'
        context['menu'] = menu()
        context['products'] = products()
        return context


class ContactView(TemplateView):
    template_name = 'mainapp/contacts.html'

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        context['title'] = 'админка/пользователи'
        context['menu'] = menu()
        return context


class ProductView(DetailView):
    model = Product
    template_name = 'mainapp/product.html'

    def get_context_data(self, **kwargs):
        context = super(ProductView, self).get_context_data(**kwargs)
        print('print pk ' + self.pk_url_kwarg)
        context['title'] = 'админка/пользователи'
        context['menu'] = menu()
        return context


class CatalogView(ListView):
    model = Basket
    template_name = 'mainapp/catalog.html'
    def get_context_data(self, **kwargs):
        context = super(CatalogView, self).get_context_data(**kwargs)
        context['title'] = 'Каталог'
        context['menu'] = menu()
        context['products'] = products()
        return context


def getBasket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    else:
        return []


def add_menu():
    CONTENT['menu'] = [
        {'name': 'главная', 'href': '/'},
        {'name': 'каталог', 'href': '/catalog/'},
        {'name': 'контакты', 'href': '/contacts/'},
        {'name': 'корзина', 'href': '/basket/'}
    ]


def add_products():
    CONTENT['products'] = Product.objects.all()


def catalog_view(request, pk=None, page=1):
    title = 'Продукты'
    add_menu()

    links_menu = Category.object.filter(is_active=True)
    basket = getBasket(request.user)

    if pk:
        if pk == '0':
            category = {
                'pk': 0,
                'name': 'все'
            }
            products = Product.object.filter(is_active=True, category__is_active=True).order_by('price')
        else:
            category = get_object_or_404(Category, pk=pk)
            products = Product.object.filter(category__pk=pk, is_active=True, category__is_active=True).order_by(
                'price')

        paginator = Paginator(products, 2)
        try:
            products_paginator = paginator.page(page)
        except PageNotAnInteger:
            products_paginator = paginator.page(1)
        except EmptyPage:
            products_paginator = paginator.page(paginator.num_pages)

        CONTENT = {
            'title': title,
            'links_menu': links_menu,
            'category': category,
            'products': products_paginator,
            'basket': basket,
        }
        return render(request, 'mainapp/catalog.html', CONTENT)
