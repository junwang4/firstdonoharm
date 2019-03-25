# Purpose: extract OTHER NAMES from one detailed HTML page
# NOTE: make sure that you need to be in folder "hw3" to run this code

import os
import sys
import unidecode
import pprint
from bs4 import BeautifulSoup

html_folder = "./detail_pages"

def extract_other_names_from_html(ingredient_name):
    """Extract the other names of an ingredient from the html page of the ingredient
    Args:
        ingredient_name: a string (for example, "aconite")
    Returns:
        the other names of the ingredient (which is a string)
    """

    FINISH YOUR CODE HERE


data = []
for ingredient_name in ["abscess-root", "aconite"]:
    other_names = extract_other_names_from_html(ingredient_name)
    item = {'ingredient':ingredient_name, 'other_names':other_names}
    data.append(item)

pprint.pprint(data)
