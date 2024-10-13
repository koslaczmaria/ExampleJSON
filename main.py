import urllib.request, json
import re

urlJson = "https://danepubliczne.imgw.pl/api/data/synop" # Aktualne dane ze stacji synoptycznych udostępniane przez IMGW

with urllib.request.urlopen(urlJson) as url:
    data = json.load(url)
    stacje = [n['stacja'] for n in data]
    print("Lista stacji:\n", stacje)
    searchWord = []
    for s in stacje:
        w = re.search("^K.*g$", s) # Nazwa zaczynająca się na "K" i kończąca na "g" (Kołobrzeg)
        if w:
            searchWord.append(s)
    print("Nazwa zaczynająca się na 'K' i kończąca na 'g':\n", searchWord)
    manyWords = []
    for s in stacje:
        w = re.search("\s", s) # Dwa lub więcej słów w nazwie
        if w:
            manyWords.append(s)
    print("Dwa lub więcej słów w nazwie:\n", manyWords)
