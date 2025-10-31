def nom_nom(numbers_list: list):
    if numbers_list[0] > numbers_list[1]:
        numbers_list[1] += numbers_list[0]
        numbers_list = numbers_list[1:] # remove the first item from the list
        # print(numbers_list)
    else:
        # print(numbers_list)
        return numbers_list

    if len(numbers_list) > 1:
        return nom_nom(numbers_list) # add a return statement everytime recursive function is called so that the top level function has something to return.
    else:
        # print("duh")
        # print(numbers_list)
        return numbers_list

print(nom_nom([5, 3, 7]))
# output = [15]
#
print(nom_nom([5, 3, 9]))
# output = [8, 9]
#
print(nom_nom([1, 2, 3]))
# output = [1, 2, 3]
#
print(nom_nom([2, 1, 3]))
# output = [3, 3]
#
print(nom_nom([8, 5, 9]))
# output = [22]
#
print(nom_nom([6, 5, 6, 100]))
# output = [17, 100]