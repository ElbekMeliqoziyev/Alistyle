from django.shortcuts import render
from django.db.models import Count, Q

from django.views.generic import ListView, TemplateView

from .models import *


class HomeView(ListView):
    template_name = 'main/index.html'
    model = Category
    context_object_name = 'categories'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        data['recomended'] = Product.objects.filter(recomended = True)
        data['discount'] = Product.objects.filter(discount__gt = 0)[:5]
        data['top_categories'] = Category.objects.order_by('-view')[:3]
        data['services'] = Service.objects.filter(is_active = True)[:4]
        data['countries'] = Country.objects.all()
        data['best_categories'] = Category.objects.annotate(product_count = Count("product_categories__products")).order_by("-product_count")[:2]

        return data
    
class ProductDetail(TemplateView):
    template_name = 'main/detail-product.html'

class ProductListLargeView(ListView):
    template_name = "main/listing-large.html"
    model = Product
    context_object_name = "products"
    paginate_by = 5

    def get_queryset(self):
        category_slug = self.kwargs.get("category_slug")
        products = Product.objects.filter(product_category__category__slug = category_slug)

        min_price = self.request.GET.get('min_price')
        max_price = self.request.GET.get('max_price')
        condition = self.request.GET.get('condition')
        brand = self.request.GET.getlist('brand')
        product_type = self.request.GET.getlist('product-type')

        if min_price:
            products = products.filter(price__gte = min_price)

        if max_price:
            products = products.filter(price__lte = max_price)

        if condition is not None and condition != "on":
            products = products.filter(condition = condition)

        if brand:
            products = products.filter(brand__in = brand)

        if product_type:
            products = products.filter(product_category__slug = product_type)

        return products

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        category_slug = self.kwargs.get("category_slug")

        data['product_categories'] = ProductCategory.objects.filter(category__slug = category_slug)
        data['category_slug'] = category_slug
        data['brands'] = ProductBrand.values
        data['conditions'] = ProductCondition.labels

        return data


class ProductListGridView(ListView):
    template_name = "main/listing-grid.html"
    model = Product
    context_object_name = "products"
    paginate_by = 5

    def get_queryset(self):
        category_slug = self.kwargs.get("category_slug")
        products = Product.objects.filter(product_category__category__slug = category_slug)

        min_price = self.request.GET.get('min_price')
        max_price = self.request.GET.get('max_price')
        condition = self.request.GET.get('condition')
        brand = self.request.GET.getlist('brand')
        product_type = self.request.GET.getlist('product-type')

        if min_price:
            products = products.filter(price__gte = min_price)

        if max_price:
            products = products.filter(price__lte = max_price)

        if condition is not None and condition != "on":
            products = products.filter(condition = condition)

        if brand:
            products = products.filter(brand__in = brand)

        if product_type:
            products = products.filter(product_category__slug = product_type)

        return products

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        category_slug = self.kwargs.get("category_slug")
        

        data['product_categories'] = ProductCategory.objects.filter(category__slug = category_slug)
        data['category_slug'] = category_slug
        data['many_size'] = ProductSize
        data['countries'] = Country.objects.all()
        data['many_color'] = ColorChoices

        return data
   




