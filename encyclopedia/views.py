from django.shortcuts import render , HttpResponse , redirect
from django.urls import reverse
from fuzzywuzzy import fuzz , process

from . import util

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
#def search(request):

  
def title(request, title):
    artical_name = util.get_entry(title)
    if artical_name == None:
        return HttpResponse("sorry this artical dose not exist yet")
    return HttpResponse(f"{artical_name}")
    
def experiment(request):
    return HttpResponse("could be")
