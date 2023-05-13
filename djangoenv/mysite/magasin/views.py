from django.http import HttpResponseRedirect
from .models import produit
from .forms import *
from django.shortcuts import redirect, render
from .forms import ProduitForm, FournisseurForm,UserRegistrationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.views import View
#from django.shortcuts import render  sessions
#from django.contrib.auth.decorators import login_required     sessions
#from django.contrib.auth import logout     sessions


#session
""" @login_required 

def index(request): 
    if request.user.is_authenticated:
        request.session['username'] = request.user.username
    return render(request, 'index.html')

    logout(request) """ #sessions




def index(request):
    list=produit.objects.all() 
    return render(request,'magasin/vitrine.html',{'list':list})



def AddProd(request):
    if request.method=="POST":
        form=ProduitForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/magasin/')#*-->
    else:
        form=ProduitForm()
    return render(request,'magasin/majProduits.html',{'form':form})


def produit_detail(request, product_id):
    # Récupérer le produit correspondant à l'identifiant unique donné
    product = get_object_or_404(produit, id=product_id)
    
    return render(request, 'product_detail.html', {'product': product})



def edit_product(request, id):
    post = get_object_or_404(produit, id=id)

    if request.method == 'GET':
        context = {'form': ProduitForm(instance=post), 'id': id}
        return render(request,'magasin/edit_produit.html',context)
    elif request.method == 'POST':
        form = ProduitForm(request.POST,request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/magasin/')
        else:
            messages.error(request, 'Please correct the following errors:')
            return render(request,'magasin/edit_produit.html',{'form':form})

def deleteProduit(request,pk):   
        produit.objects.filter(id=pk).delete()
        return HttpResponseRedirect('/magasin/')

 
class ProduitView(View):
    def get(self, request, id):
        produit_list = produit.objects.filter(id=id)
        return render(request, 'magasin/produitview.html', {'produit_list': produit_list})



def addFournisseur(request):
        if request.method == "POST":
            form = FournisseurForm(request.POST)
            if form.is_valid():
                form.save() 
                return redirect('affichefou')
        else:   form = FournisseurForm() 
        return  render(request,'magasin/nouveauFournisseur.html',{'form':form})


def edit_Fourni(request, id):
    post = get_object_or_404(fournisseur, id=id)

    if request.method == 'GET':
        context = {'form': FournisseurForm(instance=post), 'id': id}
        return render(request,'magasin/edit_fournisseur.html',context)
    elif request.method == 'POST':
        form = FournisseurForm(request.POST,request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('affichefou')
        else:
            messages.error(request, 'Please correct the following errors:')
            return render(request,'magasin/edit_fournisseur.html',{'form':form})



def deletefournisseur(request,pk):   
        fournisseur.objects.filter(id=pk).delete()
        return redirect('affichefou')



def affichefou(request):
    fou=fournisseur.objects.all()
    return render(request,'magasin/vitrine2.html',{'fou':fou})




def listcom(request):
    cmds=command.objects.all()
    context={'cmds':cmds}
    return render(request,'magasin/lsc.html',context) 
def addCommande(request):
	if request.method == "POST":
		form = CommandForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('listcom')
	else:
		form=CommandForm() 
	return  render(request,'magasin/addCommande.html',{'form':form})




def register(request):
    if request.method == 'POST' :
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request,user)
            messages.success(request, f'Coucou {username}, Votre compte a été créé avec succès !')
            return redirect('home')
    else :
        form = UserCreationForm()
    return render(request,'registration/register.html',{'form' : form})