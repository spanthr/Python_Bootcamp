print("Clemson University")
print("Shaurya \n Panthri")
print("My name is \" Shaurya \"")         # printing a quote or some symbol

university="Clemson University"
infor="university Name:::"
print(infor+university)
fullinfor=infor+university
print("\n \n \n")

print("Name::Shaurya \n"+fullinfor)

print("############FUNCTIONS####################")
print(fullinfor.lower())
print(fullinfor.upper())
print(fullinfor.islower())
print(fullinfor.isupper())
print(fullinfor.lower().islower())
print("\n")
print(len(fullinfor))
fullinfor=fullinfor+"."
print(len(fullinfor))

print("Access characters")

print(fullinfor[0])
print(fullinfor.index("m"))
print(fullinfor.index("Clemson"))
print(fullinfor.replace("Clemson","Michigan"))
fullinfor.replace("Clemson","Michigan")
print(fullinfor)
print("reassign ")
fullinfor=fullinfor.replace("Clemson","Michigan")
print(fullinfor)