def passs(a):

    if(a>2):
        print(a)
        print("aaa")
    else:
        print(2)

passs(3)
passs(2)



is_male=False
is_tall=False
if(is_male==True) or is_tall==True:
    print("MALE or TALL")
else:
    print("FEMALE or SHORT")

if(is_male==False and is_tall==False):
    print("SHORT AND FEMALE")
elif(is_male==True and is_tall==False):
    print("Male but short")
elif(is_male==False and is_tall==True):
    print("Not Male but not short")
else:
    print("Male and Tall")


def maximum_of_three(a,b,c):
    if(a>=b and a>=c):
        print(("Largest is:"+str(a)))
    elif(b>a and b>c):
        print(("Largest is:" + str(b)))
    else:
        print("Largest is:" + str(c))

maximum_of_three(2,3,4)

print(a!=)