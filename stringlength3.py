def string_length(mystring):
    if type(mystring) == int:
        return "Sorry, integers don't have length"
    if type(mystring) == float:
        return "Sorry, float don't have length"
    else:
        return len(mystring)

print(string_length(2))
print(string_length(3.14))
print(string_length("Orion"))
