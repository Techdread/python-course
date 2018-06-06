def length_of_string(string):
    return str(string).__len__() # should of used len() 

string = input("Enter a string: ")
print("The length of " + string +  " is " + str(length_of_string(string)) + " character(s)")