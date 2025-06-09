from django.urls import path
from .views import (
    machine_list, machine_create, machine_update, machine_delete,
    production_list, production_create, production_update, production_delete,
    qualite_list, qualite_create, qualite_update, qualite_delete,
    client_list, client_create, client_update, client_delete,
    fournisseur_list, fournisseur_create, fournisseur_update, fournisseur_delete,
    achat_list, achat_create, achat_update, achat_delete,
    commande_list, commande_create, commande_update, commande_delete
)

urlpatterns = [
    # Machines
    path('machines/', machine_list, name='machine_list'),
    path('machines/create/', machine_create, name='machine_create'),
    path('machines/<str:pk>/update/', machine_update, name='machine_update'),
    path('machines/<str:pk>/delete/', machine_delete, name='machine_delete'),

    # Productions
    path('productions/', production_list, name='production_list'),
    path('productions/create/', production_create, name='production_create'),
    path('productions/<str:pk>/update/', production_update, name='production_update'),
    path('productions/<str:pk>/delete/', production_delete, name='production_delete'),

    # Qualités
    path('qualites/', qualite_list, name='qualite_list'),
    path('qualites/create/', qualite_create, name='qualite_create'),
    path('qualites/<str:pk>/update/', qualite_update, name='qualite_update'),
    path('qualites/<str:pk>/delete/', qualite_delete, name='qualite_delete'),

    # Clients
    path('clients/', client_list, name='client_list'),
    path('clients/create/', client_create, name='client_create'),
    path('clients/<str:pk>/update/', client_update, name='client_update'),
    path('clients/<str:pk>/delete/', client_delete, name='client_delete'),

    # Fournisseurs
    path('fournisseurs/', fournisseur_list, name='fournisseur_list'),
    path('fournisseurs/create/', fournisseur_create, name='fournisseur_create'),
    path('fournisseurs/<str:pk>/update/', fournisseur_update, name='fournisseur_update'),
    path('fournisseurs/<str:pk>/delete/', fournisseur_delete, name='fournisseur_delete'),

    # Achats
    path('achats/', achat_list, name='achat_list'),
    path('achats/create/', achat_create, name='achat_create'),
    path('achats/<str:pk>/update/', achat_update, name='achat_update'),
    path('achats/<str:pk>/delete/', achat_delete, name='achat_delete'),

    # Commandes
    path('commandes/', commande_list, name='commande_list'),
    path('commandes/create/', commande_create, name='commande_create'),
    path('commandes/<str:pk>/update/', commande_update, name='commande_update'),
    path('commandes/<str:pk>/delete/', commande_delete, name='commande_delete'),
]

