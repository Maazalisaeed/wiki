from django.shortcuts import render , HttpResponse , redirect
from django.urls import reverse
from fuzzywuzzy import fuzz , process
from . import util
import markdown2


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
        return render(request, "encyclopedia/Error_page.html")
    return render(request, "encyclopedia/articel_page.html",{"data_from_entry": markdown2.markdown(artical_name), "title":title})
    
