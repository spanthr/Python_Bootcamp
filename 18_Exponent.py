print(2**3)


def powerful(power,base):
    result=1
    for i in range(power):
        result=base*result
    return result

a=powerful(3,3)
print(a)
a=powerful(4,3)
print(a)


a=powerful(3,2)
print(a)