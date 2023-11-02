# contact_app/views.py
from django.shortcuts import render, redirect
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # If you want to save the data, you can create a Contact model and save it here
            return redirect('thanks')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def thanks_view(request):
    return render(request, 'thanks.html')

