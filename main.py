def eval_algebra(equation):
    mul_by_neg = False

    # find the equal sign and split
    sides = {
        "lhs" : equation.split("=")[0].strip(),
        "rhs" : equation.split("=")[1].strip(),
    }

    # x is always on the left side, and the rhs is always a number
    for key, value in sides.items():
        characters = value.split(' ')
        sides[key] = characters

    # todo 2: SHIFT ALL THE NUMBERS OVER TO RHS. need to check if that element is a number or just a string.

    # check if x is the last character of lhs, if yes, what is the operator in front of x.
    if sides['lhs'][-1] == 'x':
        final_answer = int(sides['rhs'][0]) - int(sides['lhs'][0])
        if sides['lhs'][-2] == '-':
            mul_by_neg = True
    else:
        # x is the first on lhs (there's no -x in the examples)
        if sides['lhs'][-2] == '-':
            final_answer = int(sides['rhs'][0]) + int(sides['lhs'][-1])
        else:
            final_answer = int(sides['rhs'][0]) - int(sides['lhs'][-1])

    if mul_by_neg:
        final_answer *= -1

    # todo 3: check what's the operator before x if any, this will determine if we need to multiply by -1

    # todo 4: perform the operation on the rhs and get x!

    # print(sides)
    return final_answer

print(eval_algebra("2 + x = 19"))
print(eval_algebra("4 - x = 1"))
print(eval_algebra("x + 10 = 53"))
print(eval_algebra("-23 + x = -20"))
print(eval_algebra("10 + x = 5"))
print(eval_algebra("-49 - x = -180"))
print(eval_algebra("x - 22 = -56"))