import json
from difflib import get_close_matches
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
    elif word.title() in word_dict:
        return word_dict[word.title()] 
    elif len(get_close_matches(word, word_dict.keys())) > 0:
        close_word = get_close_matches(word, word_dict.keys())[0]
        question = input("Did you mean %s instead? Enter a Y (for Yes) or an N (for No) " % close_word)
        if question.lower() == 'y':
            return word_dict[close_word]
        else:
            return "We did not understand your entry"
    else:
        return "Word is not in dictionary!"

word = input("What word do you want to look up?")

output = get_definition(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)