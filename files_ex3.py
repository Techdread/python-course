numbers = [1, 2, 3]
numbers=[str(i) + "\n" for i in numbers]
file=open("files_ex3_sol.txt", 'w')
file.writelines(numbers)
file.close()
