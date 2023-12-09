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
        search_query = request.POST.get('q', '')
        all_entries = util.list_entries()
        for entry in all_entries:
            score = fuzz.WRatio(search_query,entry)
            if score == 100:
                return redirect(f"wiki/{entry}")
            else:
                continue
        artical_names_with_score = process.extract(search_query, all_entries)
        return render(request, "encyclopedia/search.html",{"entries": artical_names_with_score})    

    
def title(request, title):
    artical_name = util.get_entry(title)
    if artical_name == None:
        return HttpResponse("sorry this artical dose not exist yet")
    return HttpResponse(f"{artical_name}")
    
def experiment(request):
    return HttpResponse("could be")
