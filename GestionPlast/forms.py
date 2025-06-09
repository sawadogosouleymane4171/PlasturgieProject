from django import forms
from .models import Production, Qualite, Client, Fournisseur, Achat, Commande, Machine  # noqa: F401

class MachineForm(forms.ModelForm):
    class Meta:
        model = Machine
        fields = ['machine_code', 'nom', 'type_machine', 'date_mise_en_service', 'etat']
        labels = {
            'machine_code': 'Code machine',
            'nom': 'Nom',
            'type_machine': 'Type de machine',
            'date_mise_en_service': 'Date de mise en service',
            'etat': 'État',
        }
        widgets = {
            'machine_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'M001'}),
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Extrudeuse'}),
            'type_machine': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Injection'}),
            'date_mise_en_service': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'etat': forms.Select(attrs={'class': 'form-select'}),
        }


class ProductionForm(forms.ModelForm):
    class Meta:
        model = Production
        fields = ['lot_code', 'date_production', 'quantite_kg', 'type_plastique', 'machines']
        labels = {
            'lot_code': "Code du lot",
            'date_production': "Date de production",
            'quantite_kg': "Quantité produite (kg)",
            'type_plastique': "Type de plastique",
            'machines': "Machines utilisées",
        }
        widgets = {
            'lot_code': forms.TextInput(attrs={'class':'form-control','placeholder':'Lot#124'}),
            'date_production': forms.DateInput(attrs={'type':'date','class':'form-control'}),
            'quantite_kg': forms.NumberInput(attrs={'class':'form-control','placeholder':'500.000'}),
            'type_plastique': forms.Select(attrs={'class':'form-select'}),
            'machines': forms.SelectMultiple(attrs={'class':'form-select','size':5}),
        }
        help_texts = {
            'lot_code': "Identifiant unique du lot, ex. 'Lot#124'",
            'machines': "Sélectionnez les machines ayant participé à la production",
        }

class QualiteForm(forms.ModelForm):
    lot_code = forms.CharField(
        max_length=20,
        required=True,
        label='Lot Code',
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Lot#124'})
    )
    class Meta:
        model = Qualite
        fields = ['test_code','lot_code','taux_defauts_pct','type_test','resultat','observation']
        labels = {
            'test_code':'Code du test',
            'taux_defauts_pct':'Taux de défauts (%)',
            'type_test':'Type de test',
            'resultat':'Résultat du test',
            'observation':'Observation'
        }
        widgets = {
            'test_code': forms.TextInput(attrs={'class':'form-control','placeholder':'Q123'}),
            'taux_defauts_pct': forms.NumberInput(attrs={'class':'form-control','step':'0.01','placeholder':'1.23'}),
            'type_test': forms.Select(attrs={'class':'form-select'}),
            'resultat': forms.Select(attrs={'class':'form-select'}),
            'observation': forms.Textarea(attrs={'class':'form-control','rows':2,'placeholder':'Remarques...'}),
        }
    def save(self, commit=True):
        qual = super().save(commit=False)
        code = self.cleaned_data['lot_code']
        lot = Production.objects.get(lot_code=code)
        qual.lot = lot
        if commit: qual.save()
        return qual

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['client_code','nom','prenom','contact_email','contact_tel','adresse']
        labels = {
            'client_code':'Code client',
            'nom':'Nom ',
            'prenom':'Prénom',
            'contact_email':'Email',
            'contact_tel':'Téléphone',
            'adresse':'Adresse'
        }
        widgets = {
            'client_code': forms.TextInput(attrs={'class':'form-control','placeholder':'C001'}),
            'nom': forms.TextInput(attrs={'class':'form-control','placeholder':'Entreprise XYZ'}),
            'prenom': forms.TextInput(attrs={'class':'form-control','placeholder':'Jean'}),
            'contact_email': forms.EmailInput(attrs={'class':'form-control','placeholder':'contact@xyz.com'}),
            'contact_tel': forms.TextInput(attrs={'class':'form-control','placeholder':'0123456789'}),
            'adresse': forms.Textarea(attrs={'class':'form-control','rows':2,'placeholder':'Adresse complète'}),
        }

class FournisseurForm(forms.ModelForm):
    class Meta:
        model = Fournisseur
        fields = ['fournisseur_code','nom','prenom','contact_email','contact_tel','adresse']
        labels = {
            'fournisseur_code':'Code fournisseur',
            'nom':'Nom',
            'prenom':'Prénom',
            'contact_email':'Email',
            'contact_tel':'Téléphone',
            'adresse':'Adresse'
        }
        widgets = {
            'fournisseur_code': forms.TextInput(attrs={'class':'form-control','placeholder':'F001'}),
            'nom': forms.TextInput(attrs={'class':'form-control','placeholder':'Fournisseur ABC'}),
            'prenom': forms.TextInput(attrs={'class':'form-control','placeholder':'Jean'}),
            'contact_email': forms.EmailInput(attrs={'class':'form-control','placeholder':'fournisseur@abc.com'}),
            'contact_tel': forms.TextInput(attrs={'class':'form-control','placeholder':'0987654321'}),
            'adresse': forms.Textarea(attrs={'class':'form-control','rows':2,'placeholder':'Adresse complète'}),
        }

class AchatForm(forms.ModelForm):
    nom = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Dupont'}))
    prenom = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Jean'}))
    
    class Meta:
        model = Achat
        fields = ['achat_code','type_matiere','quantite_achetee_kg','cout_unitaire_eur','date_achat']
        labels = {
            'achat_code':'Code achat',
            'type_matiere':'Type de matière',
            'quantite_achetee_kg':'Quantité achetée (kg)',
            'cout_unitaire_eur':'Coût unitaire (€ / kg)',
            'date_achat':'Date d\'achat'
        }
        widgets = {
            'achat_code': forms.TextInput(attrs={'class':'form-control','placeholder':'A123'}),
            'type_matiere': forms.Select(attrs={'class':'form-select'}),
            'quantite_achetee_kg': forms.NumberInput(attrs={'class':'form-control','step':'0.001'}),
            'cout_unitaire_eur': forms.NumberInput(attrs={'class':'form-control','step':'0.001'}),
            'date_achat': forms.DateInput(attrs={'type':'date','class':'form-control'}),
        }
    def save(self, commit=True):
        achat = super().save(commit=False)
        fournisseur = Fournisseur.objects.get(
            nom=self.cleaned_data['nom'], 
            prenom=self.cleaned_data['prenom']
        )
        achat.fournisseur = fournisseur
        if commit:
            achat.save()
        return achat


class CommandeForm(forms.ModelForm):
    nom = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Dupont'}))
    prenom = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Jean'}))
    lot_code = forms.CharField(
        max_length=20,
        required=True,
        label='Code du lot',
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Lot#124'})
    )
    class Meta:
        model = Commande
        fields = ['numero','lot_code','date_commande','statut','quantite_vendue_kg','prix_unitaire_eur','date_livraison']
        labels = {
            'numero':'Numéro de commande',
            'date_commande':'Date de commande',
            'statut':'Statut',
            'quantite_vendue_kg':'Quantité vendue (kg)',
            'prix_unitaire_eur':'Prix unitaire (€ / kg)',
            'date_livraison':'Date de livraison'
        }
        widgets = {
            'numero': forms.TextInput(attrs={'class':'form-control','placeholder':'CMD001'}),
            'date_commande': forms.DateInput(attrs={'type':'date','class':'form-control'}),
            'statut': forms.Select(attrs={'class':'form-select'}),
            'quantite_vendue_kg': forms.NumberInput(attrs={'class':'form-control','step':'0.001'}),
            'prix_unitaire_eur': forms.NumberInput(attrs={'class':'form-control','step':'0.001'}),
            'date_livraison': forms.DateInput(attrs={'type':'date','class':'form-control'}),
        }
    
def save(self, commit=True):
        cmd = super().save(commit=False)
        cmd.client = Client.objects.get(nom=self.cleaned_data['nom'], prenom=self.cleaned_data['prenom'])
        cmd.lot = Production.objects.get(lot_code=self.cleaned_data['lot_code'])
        if commit:
            cmd.save()
        return cmd