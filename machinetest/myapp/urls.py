from django.urls import path,include
from .views import *
urlpatterns = [
    path('',index,name='index'),
    path('add_product',add_product,name='add_product'),
    path('edit_product/<int:pk>',edit_product,name='edit_product'),
    path('delete_product/<int:pk>',delete_product,name='delete_product'),
]
