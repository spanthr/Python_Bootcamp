"""This program returns the phrase the user eneters with vowels replaced by * character"""
def translator(phrase):
    translation=""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation=translation+"*"
        else:
            translation=translation+letter
    return translation
print("Tanslator function")

print(translator(input("Enter a phrase")))