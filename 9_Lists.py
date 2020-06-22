
friends= ["Neil","Mitin","Mukesh","yoyo honey"]
print(friends)
print("Access the elements of the list")
print(friends[0])
print(friends[(len(friends)-1)])

print(friends[1:])
friends[1]="Nitin"
print(friends)


"""LIST FUNCTIONS"""
print("###############################################")
print("###############################################")
print("###       LIST FUNCTIONS                    ###")
print("###############################################")
print("###############################################")


numbers=[2,3,5,6,7,8,11]
friends.extend(numbers)
print(friends)
friends.append("Wooohooo")
print(friends)
friends.insert(5,"I am here")
print(friends)

friends.remove("Neil")
print(friends)

a=friends.pop()
print(friends)
print(a)

print(friends.index("Mukesh"))
#print(friends.index("Messi"))
#friends.sort()
print(friends)
numbers.sort()
print(numbers)
print(numbers.reverse())

numbers2=numbers.copy()
print(numbers2)

friends.clear()
print(friends)