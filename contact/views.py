from django.shortcuts import render, redirect
from contact.forms import ContactModelForm
from contact.models import Contact


def contact(request):
    form = ContactModelForm(request.POST or None)
    if form.is_valid():
        form.save()
        last_obj = Contact.objects.values('id').last()
        last_id = last_obj['id']
        return redirect('success', last_id)
    context = {
        "form": form,
    }
    return render(request, 'contact/contact.html', context)

def success(request, last_id):
    message = Contact.objects.get(id=last_id)
    context = {
        "message": message,
    }
    return render(request, 'contact/success.html', context)
