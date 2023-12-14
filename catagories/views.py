from django.shortcuts import render, redirect
from . import forms

# Create your views here.
def add_catagory(request):
    if request.method == 'POST':
        catagory_form = forms.CatagoryForm(request.POST)
        if catagory_form.is_valid():
            catagory_form.save()
            return redirect('add_catagory')
    else:
        catagory_form = forms.CatagoryForm()
    return render(request,'add_catagory.html', {'catagory_form': catagory_form})