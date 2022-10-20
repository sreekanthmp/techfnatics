from ast import pattern
from django.urls import path

from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('admin_view', views.admin_view ,name='admin_view'),
    path('contacts',views.contacts,name='contacts' ),
    path('products',views.products,name='products' ),
    path('image',views.image,name='image' ),
    path('text',views.text,name='text' ),

    path('update_text/<id>',views.update_text,name='update_text' ),

    path('medias',views.medias,name='medias' ),
    path('update_media/<id>',views.update_media,name='update_media' ),

    path('update_contact/<id>',views.update_contact,name='update_contact' ),
    path('delete_contact/<id>',views.delete_contact,name='delete_contact' ),
    path('delete_product/<id>',views.delete_product,name='delete_product' ),
    path('update_product/<id>',views.update_product,name='update_product' ),
    path('update_image/<id>',views.update_image,name='update_image' ),
    path('delete_image/<id>',views.delete_image,name='delete_image' ),











]