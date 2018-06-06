import datetime
"""
This script creates an empty file.
"""


filename=datetime.datetime.now()

#Create empty file
def create_file():
    """This function creates an empty file"""
    with open(str(filename.strftime("%Y-%m-%d-%H-%M-%S")) + ".txt", "w") as file:
        file.write("") #Writing empty string

create_file()