#7.1

import math

import math as m

def mysqrt(Apple):  # Normal square root calculation using inbuilt function
    x = Apple / 2
    while True:
        FunctionValue = (x + Apple / x) / 2
        if FunctionValue == x:
            return FunctionValue
            break
        x = FunctionValue

def test_square_root(Apple_Values): # Calculating using math.sqrt function
    """Displays outcomes of calculating square root of a using different methods;
    list_of_a - list of positive digit.
    """
    l1a = "a";l2a = "-"
    l1b = "mysqrt(a)"; l2b = "---------"
    l1c = "math.sqrt(a)"; l2c = "------------"
    l1d = "diff"; l2d = "----"
    s1 = " "; s2 = " " * 3;s3 = ""

    print(l1a, s1, l1b, s2, l1c, s3, l1d)
    print(l2a, s1, l2b, s2, l2c, s3, l2d)
    
    for a in Apple_Values: # Sorting lines and columns together for structural ouput
        c1 = float(a) ; c2 = mysqrt(a);c3 = math.sqrt(a);c4 = abs(mysqrt(a) - math.sqrt(a))
        print(c1, "{:<17f}".format(c2), "{:<17f}".format(c3), c4)


test_square_root(range(1,17))  #  This will be calling the function with the given range as argument, which i have given 17
