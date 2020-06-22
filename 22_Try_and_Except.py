
try:
    num=int(input("Enter a number"))
    #num=10/0                                                       # uncomment this to view different result
    print(num)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid Input: Please enter an integer with base 10!")

 