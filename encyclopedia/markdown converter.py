import re
from util import get_entry

def markdown_converter(title):
    articel_name = get_entry(title)
    heading = re.compile('#')
    print(heading.sub('<h1>', articel_name))

