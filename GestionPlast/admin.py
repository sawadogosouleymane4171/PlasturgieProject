from django.contrib import admin
from .models import Production, Qualite, Client, Fournisseur, Achat, Commande, Machine

# Register your models here
@admin.register(Machine)
class MachineAdmin(admin.ModelAdmin):
    list_display = ['machine_code', 'nom', 'type_machine', 'etat']
    search_fields = ['machine_code', 'nom']
    list_filter = ['type_machine', 'etat']

@admin.register(Production)
class ProductionAdmin(admin.ModelAdmin):
    list_display = ('lot_code', 'type_plastique', 'date_production', 'quantite_kg', 'machines_list')
    search_fields = ('lot_code', 'type_plastique', 'machines__nom')
    list_filter = ('type_plastique', 'date_production')

    def machines_list(self, obj):
        return ", ".join([m.nom for m in obj.machines.all()])
    machines_list.short_description = "Machines utilisées"

@admin.register(Qualite)
class QualiteAdmin(admin.ModelAdmin):
    list_display = ('test_code', 'lot', 'type_test', 'resultat', 'taux_defauts_pct')
    search_fields = ('test_code', 'lot__lot_code')
    list_filter = ('type_test', 'resultat')

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('client_code', 'nom', 'contact_email', 'contact_tel')
    search_fields = ('client_code', 'nom')

@admin.register(Fournisseur)
class FournisseurAdmin(admin.ModelAdmin):
    list_display = ('fournisseur_code', 'nom', 'contact_email', 'contact_tel')
    search_fields = ('fournisseur_code', 'nom')

@admin.register(Achat)
class AchatAdmin(admin.ModelAdmin):
    list_display = ('achat_code', 'fournisseur', 'type_matiere', 'quantite_achetee_kg', 'date_achat')
    search_fields = ('achat_code', 'fournisseur__nom')
    list_filter = ('type_matiere', 'date_achat')

@admin.register(Commande)
class CommandeAdmin(admin.ModelAdmin):
    list_display = ('numero', 'client', 'lot', 'date_commande', 'statut', 'quantite_vendue_kg', 'date_livraison')
    search_fields = ('numero', 'client__nom', 'lot__lot_code')
    list_filter = ('statut', 'date_commande', 'date_livraison')