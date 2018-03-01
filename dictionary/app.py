import json
import difflib
from difflib import get_close_matches
data = json.load(open("data.json"))

word = input("Enter a word: ").lower()

def check(word):
    if word in data:
        meaning = data[word]
        return meaning
    else:
        match = get_close_matches(word, data.keys(), cutoff = 0.8)  # default cutoff = 0.6
        if(match != []):
            flag = input("Did you mean " + match[0] + "? " + "If yes, press Y otherwise press N: ")
            if flag == "Y":
                meaning = data[match[0]]
                return meaning
            elif flag == "N":
                meaning = "No such word exists!"
                return meaning
            else:
                meaning = "Wrong key pressed -_-"
                return meaning
        else:
            meaning = "No such word exists!"
            return meaning

ans = check(word)
if type(ans) == list:
    for i in ans:
        print(i)
else:
    print(ans)
