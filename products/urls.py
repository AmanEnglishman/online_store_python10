from django.urls import path

from .views import index, contacts, product_detail

urlpatterns = [
    path('', index, name='index'),
    path('contacts/', contacts, name='contacts'),
    path('<int:pk>/', product_detail, name='product_detail'),

]