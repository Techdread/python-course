import json

"""
This script imports a json with a dictionary of words
"""

word_dict = json.load(open("data.json"))

#Create empty file
def get_definition(word):
    """This function takes a word and returns its defnition"""
    word = word.lower()
    if word in word_dict:
        return word_dict[word] 
    else:
        return "Word is not in dictionary!"

word = input("What word do you want to look up?")
print(get_definition(word))