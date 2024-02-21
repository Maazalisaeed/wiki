import markdown2
from . import util
from django.shortcuts import HttpResponse

def markdown2html(title):
    data_from_entry = util.get_entry(title)
    data_from_entry = markdown2.markdown(data_from_entry)
    return HttpResponse(f"{data_from_entry}")