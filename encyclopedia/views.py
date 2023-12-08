from django.shortcuts import render , HttpResponse , redirect
from django.urls import reverse
from fuzzywuzzy import fuzz , process

from . import util

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
def search(request):
    if request.method =="POST":
        dict_to_store_entries = {}
        search_query = request.POST.get('q', '')
        search_query = search_query.lower()
        All_entries = util.list_entries()
        for entries in All_entries:
            dict_to_store_entries[entries.lower()] = entries
        redirect_url = dict_to_store_entries[search_query]
        try:
            return redirect(f"wiki/{redirect_url}")
        except KeyError:
            return HttpResponse("not found")
                



        #for entry in util.list_entries():
            #if search_query == entry:
               # return redirect(f"wiki/{search_query}")
            #else:
               # return HttpResponse("not found")
        
        
    

def title(request, title):
    artical_name = util.get_entry(title)
    if artical_name == None:
        return HttpResponse("sorry this artical dose not exist yet")
    return HttpResponse(f"{artical_name}")
    
def experiment(request):
    return HttpResponse("could be")
