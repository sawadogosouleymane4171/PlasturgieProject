"""
URL configuration for Plastproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from GestionPlast import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('machines/', views.machine_list, name='machine_list'),
    path('productions/', views.production_list, name='production_list'),
    path('qualites/', views.qualite_list, name='qualite_list'),
    path('clients/', views.client_list, name='client_list'),
    path('fournisseurs/', views.fournisseur_list, name='fournisseur_list'),
    path('achats/', views.achat_list, name='achat_list'),
    path('commandes/', views.commande_list, name='commande_list'),
    path('machines/create/', views.machine_create, name='machine_create'),
    path('machines/update/<str:pk>/', views.machine_update, name='machine_update'),
    path('machines/delete/<str:pk>/', views.machine_delete, name='machine_delete'),
    path('productions/create/', views.production_create, name='production_create'),
    path('productions/update/<str:pk>/', views.production_update, name='production_update'),
    path('productions/delete/<str:pk>/', views.production_delete, name='production_delete'),
    path('qualites/create/', views.qualite_create, name='qualite_create'),
    path('qualites/update/<str:pk>/', views.qualite_update, name='qualite_update'),
    path('qualites/delete/<str:pk>/', views.qualite_delete, name='qualite_delete'),
    path('clients/create/', views.client_create, name='client_create'),
    path('clients/update/<str:pk>/', views.client_update, name='client_update'),
    path('clients/delete/<str:pk>/', views.client_delete, name='client_delete'),
    path('fournisseurs/create/', views.fournisseur_create, name='fournisseur_create'),
    path('fournisseurs/update/<str:pk>/', views.fournisseur_update, name='fournisseur_update'),
    path('fournisseurs/delete/<str:pk>/', views.fournisseur_delete, name='fournisseur_delete'),
    path('achats/create/', views.achat_create, name='achat_create'),
    path('achats/update/<str:pk>/', views.achat_update, name='achat_update'),
    path('achats/delete/<str:pk>/', views.achat_delete, name='achat_delete'),
    path('commandes/create/', views.commande_create, name='commande_create'),
    path('commandes/update/<str:pk>/', views.commande_update, name='commande_update'),
    path('commandes/delete/<str:pk>/', views.commande_delete, name='commande_delete'),
]
