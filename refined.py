# a more efficient approach after thinking through it
def parse_side(tokens):
    # left hand side is essentially just ax + b, b is the constant and a is the coefficient of x
    a = 1
    b = 0
    sign = 1
    for t in tokens:
        # moving from left to right in left hand side
        if t == "+":
            # we hit the sign before we hit x
            continue # the sign remains at the value of 1
        elif t == "-":
            sign = -1
        elif t == "x":
            a *= sign
        else:
            b = int(t) * sign # you will only multiply by the sign it's like  +4 or -4

    return [a, b]

def eval_algebra(equation):
    lhs = parse_side(equation.split('=')[0].strip().split(" "))
    rhs = parse_side(equation.split('=')[1].strip().split(" "))
    # split the equation & strip
    # lhs shift to rhs
    # get x
    # rhs has no x value so we get the value of the constant only
    value_of_x = (rhs[1] - lhs[1]) / lhs[0]
    print(value_of_x)
    return

eval_algebra("-49 - x = 5")