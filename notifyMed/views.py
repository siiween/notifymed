from django.shortcuts import render,render_to_response

from django.http import HttpResponse

from .forms import ContactForm


def index(request):
    return render(request,'notifyMed/base.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
    else:
        form = ContactForm()
    return render_to_response('contact.html', {'form': form})

def detail(request, Persona_id):
    return HttpResponse("You're looking at question %s." % Persona_id)


# Create your views here.
