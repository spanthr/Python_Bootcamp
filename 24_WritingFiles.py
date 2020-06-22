

emply_file=open("employees.txt","a")    # a stands for appending the file
emply_file.write("\n")
emply_file.write("New Sales Employees\n")
emply_file.write("Neil - Intern\n")
emply_file.write("Nitin - Intern Summer\n")
emply_file.close()

emply_file=open("employees.html","w")    # w stands for writing the file that is a new file is created
emply_file.write("<p>New company in HTML</p")
