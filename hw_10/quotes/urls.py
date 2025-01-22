from django.urls import path
from . import views

app_name = 'quotes'

urlpatterns = [
    path("", views.main, name="root"),
    path("<int:page>", views.main, name="root_paginate"),
    path('add-author/', views.add_author_and_quote, name='add_author_and_quote'),
    path('author/<str:id_>/', views.about_author, name='about_author'),
]
