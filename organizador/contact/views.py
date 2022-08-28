from django.shortcuts import render
from .models import Contact
from .forms import ContactForm

def index(request):
    contacts = Contact.objects.filter(name__contains=request.GET.get('search', ''))
    context = {
        'contacts': contacts
        }
    return render(request,'contact/index.html', context)


def view(request, id):
    contact = Contact.objects.get(id=id)
    context = {
        'contact': contact
        }
    return render(request,'contact/detail.html', context)


def edit(request, id):

    contact = Contact.objects.get(id=id)
    if (request.method == 'GET'):
        form = ContactForm(instance=contact)
        context = {
            'form': form,
            'id': id
        }
        return render(request,'contact/create.html', context)

    if (request.method == 'POST'):
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return render(request,'contact/detail.html', {'contact': contact})
        else:
            context = {
                'form': form,
                'id': id
            }
            return render(request,'contact/create.html', context)