import json

data = json.load(open("dictionary.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    else:
        return("Word doesn't exist, Please double check")

word = input("Entre word: ")
print(translate(word))
