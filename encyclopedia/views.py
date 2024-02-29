from django.shortcuts import render , HttpResponse , redirect
from django.urls import reverse
from fuzzywuzzy import fuzz , process
from . import util
from .forms import NewPageForm
import markdown2

# ... this function retuns list of all the entries to the index.html for it to be rendered
def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
# this will check will compare the input by the user to all the entries on the disk by fuzzywuzzy
# and grade them with a score and show all the entrires in the decending order of the score
# incase there is 100% mathc this will redirect them to that addrress  
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

    # this take in the tilte of the article form the url and render the content of the article on the 
    # the article page.html template 
def title(request, title):
    artical_name = util.get_entry(title)
    if artical_name == None:
        error="#This page doesn't seem to exist"
        return render(request, "encyclopedia/Error_page.html",{"error": markdown2.markdown(error)})
    return render(request, "encyclopedia/articel_page.html",{"data_from_entry": markdown2.markdown(artical_name), "title":title})
    
    # this will create a new entry on the disk if the entry with that same name exist it will redirec the user
    # to the the edit page of that articl
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
# this render the edit page and pre-populate the forms whicha are form the forms.py with the title and content
# of  the article respectively
def edit_page(request):
    if request.method == "POST":
        title = request.POST["article_name"]
        content_of_the_article= util.get_entry(title)
        form = NewPageForm(initial={'title': title, 'content': content_of_the_article})
        return render(request,"encyclopedia/edit_page.html",{"form":form})

#  this saved the eided aticles althought I wnated edit/new to be the same function but it was too complex for me right now
def save_edited_entries(request):
    if request.method =="POST":
        title = request.POST["title"]
        content = request.POST["content"]
        util.save_entry(title,content)
        return redirect(f"wiki/{title}")
    