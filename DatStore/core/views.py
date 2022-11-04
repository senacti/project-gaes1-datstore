from unicodedata import category
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.db.models import Q
from core.models import Product, DetOrder


class ProductListView(ListView):
    template_name = 'TAseo.html'
    queryset = Product.objects.all().order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Listado de productos'

        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'productos/producto.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        print(context)

        return context


class ProductSearchListView(ListView):
    template_name = 'productos/search.html'

    def get_queryset(self):
        filters = Q(name__icontains=self.query()) | Q(
            category__name__icontains=self.query())
        return Product.objects.filter(filters)

    def query(self):
        return self.request.GET.get('q')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.query()
        context['count'] = context['product_list'].count()

        return context

