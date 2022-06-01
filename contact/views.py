from datetime import datetime, timezone
from django.shortcuts import get_object_or_404, redirect, render

# Create your views here.
from django.http import HttpResponse
import contact

from contact.models import Contact
from django.contrib.auth.decorators import login_required

# def index(request):
#     return HttpResponse("Hello world ")
def index(request):
    return render(request, 'pages/index.html')

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def about(request):
    return render(request, 'pages/about.html')

# fonction pour afficher la liste des contacts créés par l'utilisateur
@login_required(login_url="/login/")
def contact_list(request):
    user = request.user
    contacts = Contact.objects.filter(auteur=user, archive=False)
    return render(request, 'contacts/contact_list.html', {"contacts": contacts})

# fonction pour afficher les details d'un utilisateur
@login_required(login_url="/login/")
def contact_details(request, id):
    contact = get_object_or_404(Contact, id=id)
    return render(request, 'contacts/contact_details.html', {"contact": contact})

# fonction pour ajouter un utilisateur
@login_required(login_url="/login/")
def new_contact(request):
    if request.method == "POST":
        auteur = request.user
        nom = request.POST['nom']
        prenom = request.POST['prenom']
        numero = request.POST['numero']
        email = request.POST['email']
        contact = Contact.objects.create(
            auteur=auteur, 
            nom=nom, 
            prenom=prenom,
            numero=numero, 
            email=email,
            pub_date = datetime.now()
        )
        contact.save()
        return redirect("/contacts/")

    return render(request, "contacts/new_contact.html")


# fonction pour modifier un contact
@login_required(login_url="/login/")
def edit_contact(request, id):
    contact = get_object_or_404(Contact, id=id)
    if request.method == "POST":
        auteur = request.user
        nom = request.POST['nom']
        prenom = request.POST['prenom']
        numero = request.POST['numero']
        email = request.POST['email']
        edit_contact = Contact.objects.filter(pk=contact.id)
        edit_contact .update(
            nom=nom, 
            prenom=prenom,
            numero=numero, 
            email=email
        )
        return redirect("/contacts/")
    return render(request, "contacts/edit_contact.html", {"contact": contact})

# fonction pour supprimer un contact
@login_required(login_url="/login/")
def delete_contact(request, id):
    contact = get_object_or_404(Contact, id=id)
    if request.method == "POST":
        # contact.delete()
        delete_contact = Contact.objects.filter(pk=contact.id)
        delete_contact.update(
            archive=True
        )
        return redirect("/contacts/")
    return render(request, "contacts/delete_contact.html", {"contact": contact})