file=open("fruits.txt", 'r')
content=file.readlines()
file.close()
content=[i.rstrip("\n") for i in content]
for fruit in content:
    print(len(fruit))
