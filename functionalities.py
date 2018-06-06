"""
This script creates an empty file.
"""

filename="sample1.txt"

#Create empty file
def create_file():
    """This function creates an empty file"""
    with open(filename, "w") as file:
        file.write("") #Writing empty string