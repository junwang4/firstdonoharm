In HW1, we have downloaded 27 index pages from webmd.com. As mentioned in the tutorial of HW1, there are 1214 page links distributed in the 27 index pages.  

In the case of the first index page (`index_pages/a.html`), there are 101 page links.
```
https://www.webmd.com/vitamins/ai/ingredientmono-266/abscess-root
https://www.webmd.com/vitamins/ai/ingredientmono-267/abuta
https://www.webmd.com/vitamins/ai/ingredientmono-268/acacia
...
https://www.webmd.com/vitamins-supplements/ingredientmono-1550-AYAHUASCA.aspx?activeIngredientId=1550&activeIngredientName=AYAHUASCA&source=0
```
(Note that the last link has a different format than the others.)

Since these links are embedded in the file of `index_pages/a.html`, we need to parse the html file to find them.
To help us extract the links, we will use a python package `Beautiful Soup` that is designed to pull data from HTML and XML files.

**STEP 1:** Install `Beautiful Soup` (will be called `bs4` for convenience; 4 means BS version 4. Only bs4 works with Python version 3)

I suppose you have already installed Anaconda Python version 3.7 on your MacOS (as mentioned in the HW1 tutorial). If not, go to https://www.anaconda.com/distribution/ to install the version 3.7. Anaconda Python makes it really easy to use python, and it has integrated many useful packages that we will use later in this and other HWs.

If you already installed Anaconda Python 3.7, you are done -- the `Beautiful Soup` is part of it, so you don't need to install it.

**STEP 2:** Play with `Beautiful Soup` or `bs4`

There are two ways to tinker with bs4:
- ipython -- as seen in HW1
- python notebook

In this HW, we will learn how to use python notebook to do trial-and-error.
Python notebooks are human-readable documents that allow one to program in the browser and to put code, instructions, and output together to form a story.

If you already installed Anaconda Python 3.7, you are ready to use a python notebook tool `Jupyter Notebook`.

Open a terminal in your Mac, go to your HW2 folder, then type
```
jupyter notebook bs4.ipynb
```
This will initiate a notebook server, and open your web browser with URL like
```
http://localhost:8888/notebooks/bs4.ipynb
```
Note that `bs4.ipynb` is the file name of the python notebook (ipynb means: interactive python notebook).
Please follow the instructions given in the notebook to proceed.

For how to use Jupyter Notebook, search YouTube tutorial or the following document: `https://jupyter-notebook.readthedocs.io/en/stable/notebook.html`

**STEP 3:** Write a python script to parse all those 27 index pages

You just need to finish the code for function `extract_href()` in `solution_template.py`, based on what you've learned in the `bs4.ipynb`.
