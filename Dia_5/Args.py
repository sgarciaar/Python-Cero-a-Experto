def suma(*args):
    total=0
    for arg in args:
        total+=arg
    return total

print(suma(5,6,7))

def suma2(*args):
    return sum(args)

print(suma2(5,6,7))


def suma3(*aviones):
    return sum(aviones)

print(suma3(5,6,7))