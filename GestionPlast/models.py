from django.db import models, transaction
from django.core.exceptions import ValidationError

# Create your models here.
class Machine(models.Model):
    """
    Machines utilisées dans l'usine.
    """
    machine_code = models.CharField(
        primary_key=True,
        max_length=20,
        verbose_name="Code machine",
        help_text="Identifiant unique de la machine, ex. 'M001'"
    )
    nom = models.CharField(
        max_length=100,
        verbose_name="Nom de la machine",
        help_text="Désignation de la machine, ex. 'Extrudeuse'"
    )
    type_machine = models.CharField(
        max_length=50,
        verbose_name="Type de machine",
        help_text="Fonction ou catégorie, ex. 'Injection'"
    )
    date_mise_en_service = models.DateField(
        verbose_name="Date de mise en service",
        help_text="Date de démarrage de la machine"
    )
    ETAT_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('maintenance', 'Maintenance')
    ]
    etat = models.CharField(
        max_length=20,
        choices=ETAT_CHOICES,
        verbose_name="État",
        help_text="Statut opérationnel de la machine"
    )

    class Meta:
        verbose_name = "Machine"
        verbose_name_plural = "Machines"

    def __str__(self):
        return f"{self.machine_code} – {self.nom} ({self.get_etat_display()})"

   



class Production(models.Model):
    """
    Journal de production des lots de plastique.
    """
    lot_code = models.CharField(
        primary_key=True,
        max_length=20,
        verbose_name="Code du lot",
        help_text="Identifiant unique du lot, ex. 'Lot#124'"
    )
    PLASTIQUE_CHOICES = [
        ('PET', 'PET'),
        ('PVC', 'PVC'),
        ('PEHD', 'PEHD'),
    ]
    date_production = models.DateField(verbose_name="Date de production")
    quantite_kg = models.DecimalField(
        max_digits=10, decimal_places=3,
        verbose_name="Quantité produite (kg)"
    )
    type_plastique = models.CharField(
        max_length=10, choices=PLASTIQUE_CHOICES,
        verbose_name="Type de plastique"
    )
    machines = models.ManyToManyField(
        Machine,
        related_name="productions",
        verbose_name="Machines utilisées",
    help_text="Sélectionnez les machines ayant participé à la production")
    
    
    class Meta:
        
        ordering = ['-date_production']
        verbose_name = "Lot de production"
        verbose_name_plural = "Lots de production"

    def __str__(self):
        return f"{self.lot_code} – {self.type_plastique} ({self.date_production})"


class Qualite(models.Model):
    """
    Résultats de tests qualité associés à un lot de production.
    """
    test_code = models.CharField(
        primary_key=True,
        max_length=20,
        verbose_name="Code du test",
        help_text="Identifiant unique du test qualité"
    )
    TEST_CHOICES = [
        ('resistance', 'Résistance mécanique'),
        ('transparence', 'Transparence optique'),
    ]
    RESULTAT_CHOICES = [
        ('conforme', 'Conforme'),
        ('non_conforme', 'Non conforme'),
    ]
    lot = models.ForeignKey(
        Production,
        to_field='lot_code',
        on_delete=models.CASCADE,
        related_name='tests_qualite',
        verbose_name="Lot de production",
        help_text="Sélectionnez le code du lot de production"
    )
    taux_defauts_pct = models.DecimalField(
        max_digits=5, decimal_places=2,
        verbose_name="Taux de défauts (%)"
    )
    type_test = models.CharField(
        max_length=20, choices=TEST_CHOICES,
        verbose_name="Type de test"
    )
    resultat = models.CharField(
        max_length=20, choices=RESULTAT_CHOICES,
        verbose_name="Résultat du test"
    )
    observation = models.TextField(
        blank=True,
        verbose_name="Observation"
    )

    class Meta:
        verbose_name = "Test qualité"
        verbose_name_plural = "Tests qualité"

    def __str__(self):
        return f"{self.test_code} – {self.get_type_test_display()} – Lot {self.lot.lot_code}"


class Client(models.Model):
    """
    Informations sur les clients.
    """
    client_code = models.CharField(
        primary_key=True,
        max_length=20,
        verbose_name="Code client",
        help_text="Identifiant unique du client"
    )
    nom = models.CharField(
        max_length=100, verbose_name="Nom"
    )
    prenom = models.CharField(
        max_length=50, verbose_name="Prénom"
    )
    contact_email = models.EmailField(
        blank=True, verbose_name="Email"
    )
    contact_tel = models.CharField(
        max_length=20, blank=True, verbose_name="Téléphone"
    )
    adresse = models.TextField(
        blank=True, verbose_name="Adresse"
    )

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"

    def __str__(self):
        return f"{self.client_code} – {self.nom}"


class Fournisseur(models.Model):
    """
    Informations sur les fournisseurs.
    """
    fournisseur_code = models.CharField(
        primary_key=True,
        max_length=20,
        verbose_name="Code fournisseur",
        help_text="Identifiant unique du fournisseur"
    )
    nom = models.CharField(
        max_length=100, verbose_name="Nom"
    )
    prenom = models.CharField(
        max_length=50, verbose_name="Prénom"
    )
    contact_email = models.EmailField(
        blank=True, verbose_name="Email"
    )
    contact_tel = models.CharField(
        max_length=20, blank=True, verbose_name="Téléphone"
    )
    adresse = models.TextField(
        blank=True, verbose_name="Adresse"
    )

    class Meta:
        verbose_name = "Fournisseur"
        verbose_name_plural = "Fournisseurs"

    def __str__(self):
        return f"{self.fournisseur_code} – {self.nom}"


class Achat(models.Model):
    """
    Achats de matières premières.
    """
    achat_code = models.CharField(
        primary_key=True,
        max_length=20,
        verbose_name="Code achat",
        help_text="Identifiant unique de l'achat"
    )
    MATIERE_CHOICES = [
        ('resine_pet', 'Résine PET'),
        ('additif', 'Additif'),
    ]
    fournisseur = models.ForeignKey(
        Fournisseur,
        to_field='fournisseur_code',
        on_delete=models.PROTECT,
        related_name='achats',
        verbose_name="Fournisseur"
    )
    type_matiere = models.CharField(
        max_length=20, choices=MATIERE_CHOICES,
        verbose_name="Type de matière"
    )
    quantite_achetee_kg = models.DecimalField(
        max_digits=10, decimal_places=3,
        verbose_name="Quantité achetée (kg)"
    )
    cout_unitaire_eur = models.DecimalField(
        max_digits=8, decimal_places=3,
        verbose_name="Coût unitaire (€ / kg)"
    )
    date_achat = models.DateField(verbose_name="Date d'achat")

    class Meta:
        ordering = ['-date_achat']
        verbose_name = "Achat"
        verbose_name_plural = "Achats"

    def __str__(self):
        return f"{self.achat_code} – {self.quantite_achetee_kg} kg de {self.get_type_matiere_display()}"




# ...existing code...

class Commande(models.Model):
    """
    Suivi des commandes clients lié aux lots produits.
    """
    numero = models.CharField(
        primary_key=True,
        max_length=50,
        verbose_name="Numéro de commande",
        help_text="Identifiant unique de la commande"
    )
    client = models.ForeignKey(
        Client,
        to_field='client_code',
        on_delete=models.PROTECT,
        related_name='commandes',
        verbose_name="Client"
    )
    lot = models.ForeignKey(
        Production,
        to_field='lot_code',
        on_delete=models.PROTECT,
        related_name='commandes',
        verbose_name="Lot commandé",
        help_text="Sélectionnez le code du lot (jusqu'à la quantité disponible)"
    )
    date_commande = models.DateField(verbose_name="Date de commande")
    statut = models.CharField(
        max_length=20, choices=[
            ('en_attente', 'En attente'),
            ('livree', 'Livrée'),
            ('annulee', 'Annulée'),
        ],
        verbose_name="Statut"
    )
    quantite_vendue_kg = models.DecimalField(
        max_digits=10, decimal_places=3,
        verbose_name="Quantité vendue (kg)",
        help_text="Quantité prélevée sur le lot"
    )
    prix_unitaire_eur = models.DecimalField(
        max_digits=8, decimal_places=3,
        verbose_name="Prix unitaire (€ / kg)"
    )
    date_livraison = models.DateField(verbose_name="Date de livraison")

    class Meta:
        ordering = ['-date_commande']
        verbose_name = "Commande"
        verbose_name_plural = "Commandes"

    def __str__(self):
        return f"{self.numero} – Lot {self.lot.lot_code} – {self.get_statut_display()}"

    def clean(self):
        # Vérification de la quantité disponible dans le lot
        if self.pk:
            # Si modification, restituer l'ancienne quantité avant de vérifier
            old = Commande.objects.get(pk=self.pk)
            quantite_disponible = self.lot.quantite_kg + old.quantite_vendue_kg
        else:
            quantite_disponible = self.lot.quantite_kg
        if self.quantite_vendue_kg > quantite_disponible:
            raise ValidationError("Quantité vendue supérieure à la quantité disponible dans le lot.")

    def save(self, *args, **kwargs):
        with transaction.atomic():
            self.clean()
            if self.pk:
                # Modification : restituer l'ancienne quantité avant de décrémenter la nouvelle
                old = Commande.objects.get(pk=self.pk)
                self.lot.quantite_kg += old.quantite_vendue_kg
            # Décrémenter la quantité du lot
            self.lot.quantite_kg -= self.quantite_vendue_kg
            self.lot.save()
            super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        with transaction.atomic():
            # Restituer la quantité au lot lors de la suppression
            self.lot.quantite_kg += self.quantite_vendue_kg
            self.lot.save()
            super().delete(*args, **kwargs)