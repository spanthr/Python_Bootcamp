print("Hi, This is Shaurya")
print("I am 23 years old")
print("Ich bin Shaurya")
print("Ich bin zwei-und-zwanzig jahre alt")


print("________________________________")

character_name="Shawrya"
character_age="54"

print("Hi, This is "+character_name+",")
print("I am "+character_age+" years old")
print("Ich bin "+character_name)
print("Ich bin zwei-und-zwanzig jahre alt :" +character_age)

"""Re-assigning values"""
print("________________________________")
character_name="Yash"
character_age="22"

print("Hi, This is "+character_name+",")
print("I am "+character_age+" years old")
print("Ich bin "+character_name)
print("Ich bin zwei-und-zwanzig jahre alt :" +character_age)

"""Different Type of Data type that is numbers"""

print("________________________________")

character_name="Yash"
character_age="22"
isMale=True
contact_number=8126611
character_hegiht=6.1

print("Hi, This is "+character_name+",")
print("I am "+character_age+" years old")
print("Ich bin "+character_name)
print("Ich bin zwei-und-zwanzig jahre alt :" +character_age)
print(character_name+"geneder is male"+str(isMale))
print("his contact number is"+str(contact_number))
print("His height is:"+str(character_hegiht))


"""Few more examples of formatted output"""
print("##############################################################")
print("###############################################################")
print("  Few      more            examples                      ")
print("###############################################################")
print("###############################################################" )
p=2
q=2.2
print(q, p, p * q)
print(q, p, p * q, sep=",")
print(q, p, p * q, sep=" :-) ")
print(str(q) + " " + str(p) + " " + str(p * q))