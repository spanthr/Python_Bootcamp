
def hello_world(name):
    print("Hello World")
    print("Hello"+ name)
    print("\n")


name=input("Enter your name:")

print("TOP  \n")
hello_world(name)
print("Bottom")

def sum_of_two(a,b):
    return (a+b)

a=input("enter a num:")
a=int(a)

b=input("enter a number:")
b=int(b)

print("The sum is:"+ str(sum_of_two(a,b)))

def hello_world1(name,age):
    print("Hello World")
    print("Hello:"+ name)
    print("\n")
    print("You are "+ str(age))

hello_world1("Shaurya",22)



print("#######################################################")

print("#######################################################")

print("######               RETURN STATEMENT           ########")

print("#######################################################")

print("#######################################################")

def cube1(number4):
    cube=number4*number4*number4
    return cube
    print("code will not run")

print(cube1(3))

print(cube1(8))
result=cube1(4)

print("The resuult is:")
print(result)