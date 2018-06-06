import datetime
"""
This script concatonates 3 files content1.txt, content2.txt, content3.txt and merges them in a file with the current timestamp
"""


filename=datetime.datetime.now()
files=["content1.txt","content2.txt", "content3.txt"]

#Create empty file
def write_list_to_file(my_list):
    """This function writes list to time stamped file"""
    with open(str(filename.strftime("%Y-%m-%d-%H-%M-%S-%f")) + ".txt", "w") as file:
        for line in my_list:
            file.write(str(line)+ "\n") #Writing line by line

def merge_files_to_list():
    """This function reads in all the files and strips carriage returns and reutrns thge lines in a single list"""
    content=[]
    for f in files:
        with open(f ,"r") as file:
            for line in file:
                content.append(line.rstrip("\n"))
    return content

write_list_to_file(merge_files_to_list())

#create_file()

