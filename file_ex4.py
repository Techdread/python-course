temperatures=[10,-20,-289,100]
def c_to_f(c):
    if c< -273.15:
        return "That temperature doesn't make sense!"
    else:
        f=c*9/5+32
        return f

with open("file_ex4_sol.txt", "w") as file:
    for t in temperatures:
        f = c_to_f(t)
        if type(f) != str:
            file.write(str(f) + "\n")

#another stament end



