from django.shortcuts import render
from .forms import ContactForm
from django.contrib.auth import get_user_model

User = get_user_model()

def home_page(request):
    return render(request, "home_page.html")

def contact_page(request):
    contact_form = ContactForm(request.POST or None)

    context = {
        'form': contact_form
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    return render(request, "contact/contact.html", context)

def updaterecord(request, id):
    newEmail = request.GET['email']
    newFirstName = request.GET['first_name']
    user = User.objects.get(id=id)
    user.email = newEmail
    user.first_name = newFirstName
    user.save()
    return redirect('list_user')

def update(request, id):
    user = User.objects.get(id=id)
    context = {
        'user': user
    }
    return render(request, 'auth/update.html', context)

def delete(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect('list_user')

def list_user(request):
    model = User.objects.filter(user_lvl='admin')
    # print(model)
    context = {
        'model' : model
    }
    return render(request, 'auth/list_user.html', context)