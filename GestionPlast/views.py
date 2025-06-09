from django.shortcuts import render, redirect, get_object_or_404
from .models import Machine, Production, Qualite, Client, Fournisseur, Achat, Commande
from .forms import MachineForm, ProductionForm, QualiteForm, ClientForm, FournisseurForm, AchatForm, CommandeForm

def machine_list(request):
    search_query = request.GET.get('search')
    if search_query:
        machines = Machine.objects.filter(nom__icontains=search_query)
    else:
        machines = Machine.objects.all()
    return render(request, 'machine_list.html', {'machines': machines})

def machine_create(request):
    if request.method == 'POST':
        form = MachineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('machine_list')
    else:
        form = MachineForm()
    return render(request, 'machine_form.html', {'form': form})

def machine_update(request, pk):
    machine = get_object_or_404(Machine, pk=pk)
    if request.method == 'POST':
        form = MachineForm(request.POST, instance=machine)
        if form.is_valid():
            form.save()
            return redirect('machine_list')
    else:
        form = MachineForm(instance=machine)
    return render(request, 'machine_form.html', {'form': form})

def machine_delete(request, pk):
    machine = get_object_or_404(Machine, pk=pk)
    if request.method == 'POST':
        machine.delete()
        return redirect('machine_list')
    return render(request, 'machine_confirm_delete.html', {'machine': machine})

# Production CRUD views
def production_list(request):
    search_query = request.GET.get('search')
    if search_query:
        productions = Production.objects.filter(lot_code__icontains=search_query)
    else:
        productions = Production.objects.all()
    return render(request, 'production_list.html', {'productions': productions})

def production_create(request):
    if request.method == 'POST':
        form = ProductionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('production_list')
    else:
        form = ProductionForm()
    return render(request, 'production_form.html', {'form': form})

def production_update(request, pk):
    production = get_object_or_404(Production, pk=pk)
    if request.method == 'POST':
        form = ProductionForm(request.POST, instance=production)
        if form.is_valid():
            form.save()
            return redirect('production_list')
    else:
        form = ProductionForm(instance=production)
    return render(request, 'production_form.html', {'form': form})

def production_delete(request, pk):
    production = get_object_or_404(Production, pk=pk)
    if request.method == 'POST':
        production.delete()
        return redirect('production_list')
    return render(request, 'production_confirm_delete.html', {'production': production})

# Qualite CRUD views
def qualite_list(request):
    search_query = request.GET.get('search')
    if search_query:
        qualites = Qualite.objects.filter(test_code__icontains=search_query)
    else:
        qualites = Qualite.objects.all()
    return render(request, 'qualite_list.html', {'qualites': qualites})

def qualite_create(request):
    if request.method == 'POST':
        form = QualiteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('qualite_list')
    else:
        form = QualiteForm()
    return render(request, 'qualite_form.html', {'form': form})

def qualite_update(request, pk):
    qualite = get_object_or_404(Qualite, pk=pk)
    if request.method == 'POST':
        form = QualiteForm(request.POST, instance=qualite)
        if form.is_valid():
            form.save()
            return redirect('qualite_list')
    else:
        form = QualiteForm(instance=qualite)
    return render(request, 'qualite_form.html', {'form': form})

def qualite_delete(request, pk):
    qualite = get_object_or_404(Qualite, pk=pk)
    if request.method == 'POST':
        qualite.delete()
        return redirect('qualite_list')
    return render(request, 'qualite_confirm_delete.html', {'qualite': qualite})

# Client CRUD views
def client_list(request):
    search_query = request.GET.get('search')
    if search_query:
        clients = Client.objects.filter(nom__icontains=search_query)
    else:
        clients = Client.objects.all()
    return render(request, 'client_list.html', {'clients': clients})

def client_create(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm()
    return render(request, 'client_form.html', {'form': form})

def client_update(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm(instance=client)
    return render(request, 'client_form.html', {'form': form})

def client_delete(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        client.delete()
        return redirect('client_list')
    return render(request, 'client_confirm_delete.html', {'client': client})

# Fournisseur CRUD views
def fournisseur_list(request):
    search_query = request.GET.get('search')
    if search_query:
        fournisseurs = Fournisseur.objects.filter(nom__icontains=search_query)
    else:
        fournisseurs = Fournisseur.objects.all()
    return render(request, 'fournisseur_list.html', {'fournisseurs': fournisseurs})

def fournisseur_create(request):
    if request.method == 'POST':
        form = FournisseurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('fournisseur_list')
    else:
        form = FournisseurForm()
    return render(request, 'fournisseur_form.html', {'form': form})

def fournisseur_update(request, pk):
    fournisseur = get_object_or_404(Fournisseur, pk=pk)
    if request.method == 'POST':
        form = FournisseurForm(request.POST, instance=fournisseur)
        if form.is_valid():
            form.save()
            return redirect('fournisseur_list')
    else:
        form = FournisseurForm(instance=fournisseur)
    return render(request, 'fournisseur_form.html', {'form': form})

def fournisseur_delete(request, pk):
    fournisseur = get_object_or_404(Fournisseur, pk=pk)
    if request.method == 'POST':
        fournisseur.delete()
        return redirect('fournisseur_list')
    return render(request, 'fournisseur_confirm_delete.html', {'fournisseur': fournisseur})

# Achat CRUD views
def achat_list(request):
    search_query = request.GET.get('search')
    if search_query:
        achats = Achat.objects.filter(achat_code__icontains=search_query)
    else:
        achats = Achat.objects.all()
    return render(request, 'achat_list.html', {'achats': achats})

def achat_create(request):
    if request.method == 'POST':
        form = AchatForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('achat_list')
    else:
        form = AchatForm()
    return render(request, 'achat_form.html', {'form': form})

def achat_update(request, pk):
    achat = get_object_or_404(Achat, pk=pk)
    if request.method == 'POST':
        form = AchatForm(request.POST, instance=achat)
        if form.is_valid():
            form.save()
            return redirect('achat_list')
    else:
        form = AchatForm(instance=achat)
    return render(request, 'achat_form.html', {'form': form})

def achat_delete(request, pk):
    achat = get_object_or_404(Achat, pk=pk)
    if request.method == 'POST':
        achat.delete()
        return redirect('achat_list')
    return render(request, 'achat_confirm_delete.html', {'achat': achat})

# Commande CRUD views
def commande_list(request):
    search_query = request.GET.get('search')
    if search_query:
        commandes = Commande.objects.filter(numero__icontains=search_query)
    else:
        commandes = Commande.objects.all()
    return render(request, 'commande_list.html', {'commandes': commandes})

def commande_create(request):
    if request.method == 'POST':
        form = CommandeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('commande_list')
    else:
        form = CommandeForm()
    return render(request, 'commande_form.html', {'form': form})

def commande_update(request, pk):
    commande = get_object_or_404(Commande, pk=pk)
    if request.method == 'POST':
        form = CommandeForm(request.POST, instance=commande)
        if form.is_valid():
            form.save()
            return redirect('commande_list')
    else:
        form = CommandeForm(instance=commande)
    return render(request, 'commande_form.html', {'form': form})

def commande_delete(request, pk):
    commande = get_object_or_404(Commande, pk=pk)
    if request.method == 'POST':
        commande.delete()
        return redirect('commande_list')
    return render(request, 'commande_confirm_delete.html', {'commande': commande})
