from django.shortcuts import get_object_or_404, render

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

@login_required(login_url="/login/")
def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'contacts/contact_list.html', {"contacts": contacts})

@login_required(login_url="/login/")
def contact_details(request, id):
    contact = get_object_or_404(Contact, id=id)
    return render(request, 'contacts/contact_details.html', {"contact": contact})