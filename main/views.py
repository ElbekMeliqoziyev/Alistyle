from django.shortcuts import render

from django.views.generic import DetailView

from .models import Category

class CategoryDetail(DetailView):
    template_name = 'main/index.html'
    model = Category
    context_object_name = 'category'
    slug_url_kwarg = 'slug'