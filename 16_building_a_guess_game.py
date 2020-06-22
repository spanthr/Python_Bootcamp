"""Game on"""
print("help:animal")
secret_word ="tiger"
guess=""

c=1
while(guess != secret_word and c<=3):
    guess=input("Enter a Guess:")
    c=c+1

if(c<=3):
    print(("You Win"))
else:
    print("Loser")

print("help:animal")
secret_word ="giraffe"
guess=""
while(guess != secret_word):
    guess=input("Enter a Guess:")
print(("You Win"))



