from django.shortcuts import render , HttpResponse , redirect
from django.urls import reverse
from fuzzywuzzy import fuzz , process
from . import util
from .forms import NewPageForm
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
        error="#This page doesn't seem to exist"
        return render(request, "encyclopedia/Error_page.html",{"error": markdown2.markdown(error)})
    return render(request, "encyclopedia/articel_page.html",{"data_from_entry": markdown2.markdown(artical_name), "title":title})
    
def new_page(request):
    if request.method == "GET":      
        return render(request,"encyclopedia/new_page.html",{"form":NewPageForm()})
    
    if request.method =="POST":
        title = request.POST["title"]
        content = request.POST["content"]
        all_entries = util.list_entries()
        match_found= False
        for entry in all_entries:
            score = fuzz.WRatio(title,entry)
            if score == 100:
                error = "## Article with this title already exist you can edit the page in the edit tab"
                match_found= True
                return render(request,"encyclopedia/Error_page.html",{"error": markdown2.markdown(error), "context_of_the_error":True, "title":title})
            else:
                continue                              
        if match_found == False:
             util.save_entry(title,content)            
    return render(request,"encyclopedia/new_page.html",{"form":NewPageForm()})

def edit_page(request):
    if request.method == "POST":
        title = request.POST["article_name"]
        content_of_the_article= util.get_entry(title)
        form = NewPageForm(initial={'title': title, 'content': content_of_the_article})
        return render(request,"encyclopedia/edit_page.html",{"form":form})

def save_edited_entries(request):
    if request.method =="POST":
        title = request.POST["title"]
        content = request.POST["content"]
        util.save_entry(title,content)
        return redirect(f"wiki/{title}")
    