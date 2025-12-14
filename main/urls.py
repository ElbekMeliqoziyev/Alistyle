from django.urls import path

from .views import *

urlpatterns = [
    path("detail<str:slug>/", CategoryDetail.as_view(), name='detail'),
]