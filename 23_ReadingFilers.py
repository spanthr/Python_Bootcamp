
emply_file=open("employees.txt","r")


"""Functions that can be used"""
print(emply_file.readable()) # tells if the content is readable
print(emply_file.read())

print("First two lines")
print(emply_file.readline())
print(emply_file.readline())


emply_file1=open("employees.txt","r")

print("all the lines as an array")
for emply in emply_file1.readlines():
    print(emply)

emply_file.close()