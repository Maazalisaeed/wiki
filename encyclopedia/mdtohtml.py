import re
from . import util

def markdown_converter(title):
    articel_name = util.get_entry(title)
    heading = re.compile('#')
    print(heading.sub('<h1>', articel_name))