import string
import os
from bs4 import BeautifulSoup

def extract_links(filepath):
    """Find all the page links in a WebMD index page.

    Args:
        filepath: a WebMD index html file

    Returns:
        list of links

    """

    FINISH YOUR CODE HERE



folder = "../HW1/index_pages"
letters = string.ascii_lowercase + "0"
out_all = []
for letter in letters:
    filename = letter + ".html"
    filepath = folder + "/" + filename
    out = extract_links(filepath)
    print(f'letter: {letter}  => count: {len(out)}')
    out_all += out
print(f'\ntotal ingredients: {len(out_all)}')

print('\na sample of first 10 links:\n')
print(out_all[:10])
