def multiplication_by_2(x):
    return x * 2

multiplication_by_2(2)

def division_by_2(x):
    return float(x/2)

division_by_2(2)


def exponentiation_exp_2(x):
    result = x ** 2
    print("Raised to the power of 2:")
    return result

exponentiation_exp_2(5)


def plus_five(x):
    return x + 5
    
def m_by_3(x):
    return plus_five(x) * 3


m_by_3(5)

def compare_the_two(x,y):
    if x > y:
        print("Greater")
    elif y > x:
        print("Less")
    else:
        print("Equal")