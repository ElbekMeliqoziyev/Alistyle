from django.urls import path

from .views import *

urlpatterns = [
    path("", HomeView.as_view(), name='home'),
    path("detail/", ProductDetail.as_view(), name="detail"),
    path('<str:category_slug>/large/', ProductListLargeView.as_view(), name='product-large'),
    path("<str:category_slug>/grid/", ProductListGridView.as_view(), name='product-grid'),
]