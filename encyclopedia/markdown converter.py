import re
from util import get_entry

title = input("enter title name: ")

def markdown_converter(title_name):
    data_form_article = get_entry(title_name)
    complied_str = re.compile('#')
    print(complied_str.sub('<h1>', data_form_article))
    
markdown_converter(title)