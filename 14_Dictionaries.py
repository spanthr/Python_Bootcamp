"""Dictionaries"""

monthConversion= {
    "Jan":"January",
    "Feb":"February",
    "Mar":"March",
    "Apr":"April",
    5:"May"


}


print(monthConversion["Apr"])
print(monthConversion["Mar"])
print(monthConversion.get("Jan"))
print(monthConversion.get("Dec"))
print(monthConversion.get(5))

print(monthConversion.get("Dec","Not a valid Key"))