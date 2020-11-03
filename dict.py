import json
data=json.load(open("data.json"))

def translate(word):
    if word in data:
        return data[word]
#words related to science
word=input(("enter the word u wanna search"))

output=translate(word)
print(output)