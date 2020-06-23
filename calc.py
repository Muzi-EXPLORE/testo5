print("hello world")

def adder(a, b):
    """Returns the sum of a and b"""
    if type(a)==str or type(b)==str:
        raise ValueError("Numbers only, no strings")
    return a+b

def subt(a, b):
    """returns difference of a and b"""
    return a-b