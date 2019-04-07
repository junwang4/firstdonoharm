### atom-runner, use python3 interpreter instead of python2
config (Under Preferences...)
first, check "package", click "atom-runner", scroll-down to config

add at the end (2 spaces indent for "runner"):
```
  "runner":
    "scopes":
      "python": "python3"
```
**NOTE:** make sure you open `atom` in the your working folder, for example,
```
cd ~/git_projects/firstdonoharm/hw5
open -a atom test.py
# if test.py doesn't exist, run
touch test.py
```

### Go over the homework of HW4
download the 1200+ WebMD ingredient pages to folder hw3/detail_pages

### Find out those UNSAFE ingredients
```
jupyter notebook detecting_safety.ipynb
```

### Homework
We've learned how to extract other names for one ingredient in HW3.
Suppose you've downloaded 1200+ pages to `hw3/detail_pages` as a result of HW4's homework.

This time, your task is to write a python script
to extract the other names for all those 1200+ ingredients,
and to save the result to a csv file (say, "ingredient_other_names.csv") in the format of:
```
ingredient,other_names
abscess-root,"American Greek Valerian, Blue Bells, False Jacob's Ladder, Polemoine Rampante, Polemonie Rampante, Polemonium reptans, Sweatroot, Valeriana Griega"
.
.
.
```

The csv file "ingredient_other_names.csv" will be used together with those UNSAFE ingredients obtained in the python notebook of this lesson.
