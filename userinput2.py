password=''
while password != 'python123':
    password = input("Enter password?: ")
    if password == 'python123':
        print("you are logged in!")
    else:
        print("Sorry, try again")