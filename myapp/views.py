from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

from .models import AppModel
from .forms import AppForm

def create_view(request):
    
    context = {}
    
    form = AppForm(request.POST or None)
    if form.is_valid():
        form.save()
        
    context['form'] = form
    
    return render(request, "create_view.html", context)

def list_view(request):
    # dictionary for initial data with 
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    context["dataset"] = AppModel.objects.all()
         
    return render(request, "list_view.html", context)

def detail_view(request, id):
    # dictionary for initial data with 
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    context["data"] = AppModel.objects.get(id = id)
    
def update_view(request, id):
    # dictionary for initial data with 
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(AppModel, id = id)
 
    # pass the object as instance in form
    form = AppForm(request.POST or None, instance = obj)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/"+id)
 
    # add form dictionary to context
    context["form"] = form
 
    return render(request, "update_view.html", context)

def delete_view(request, id):
    # dictionary for initial data with 
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(AppModel, id = id)
 
 
    if request.method =="POST":
        # delete object
        obj.delete()
        # after deleting redirect to 
        # home page
        return HttpResponseRedirect("/")
 
    return render(request, "delete_view.html", context)
         