def string_length(mystring):
    try:
        return len(mystring)
    except TypeError: 
        return print("Sorry integers don't have length")
        
string_length(4)
print(string_length("Natalie"))