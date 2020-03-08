from django.shortcuts import render,render_to_response, redirect

from django.http import HttpResponse

from .forms import ContactForm

def index(request):
    context = {
        'ContactForm' : ContactForm,
    }

    return render(request,'notifyMed/base.html', context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
    else:
        form = ContactForm()
    return redirect('index')



def detail(request, Persona_id):
    return HttpResponse("You're looking at question %s." % Persona_id)


# Create your views here.
