from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import *
from .forms import *

# [log in crap]
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created. You can log in now!')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'user/register.html', context)

def logout_view(request):
    logout(request)
    #return render(request, 'user/logout.html')
    return redirect('login')

# [home screen]
@login_required
def HomePage(request):
    context = {
        
    }
    template = loader.get_template("inventory/Home.html")
    return HttpResponse(template.render(context,request))

# control room [inventory]
@login_required
def Controlroom(request):
    Item_list = Item.objects.all()
    template = loader.get_template("inventory/Controlroom.html")
    context = {
        "Item_list": Item_list,
    }
    return HttpResponse(template.render(context,request))

# [specific item page]
@login_required
def Itemdetails(request, item_id):
    template = loader.get_template("inventory/Itemdetails.html")
    context = {
        "Item": Item.objects.get(id = item_id),
    }
    return HttpResponse(template.render(context,request))
    
# [hanalytics]
@login_required
def Analytics(request):
    context = {
        
    }
    template = loader.get_template("inventory/Analytics.html")
    return HttpResponse(template.render(context,request))
