from operator import index

LETTER_COMBIS = {
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"],
}

def letter_combinations(numbers_str: str) -> list | None:
    combinations = []

    if numbers_str == "":
        return combinations

    def attach_number(combi_string, letter_list_to_attach):
        original_string = combi_string
        result = []
        for alphabet in letter_list_to_attach:
            combi_string += alphabet
            result.append(combi_string)
            combi_string = original_string
        return result

    def check_the_index(string_to_add, current_index, total_length_of_str:int):
        if current_index < total_length_of_str - 1:
            # print(current_index)
            current_index += 1
            result_combis = attach_number(string_to_add, LETTER_COMBIS[numbers_str[current_index]])
            # print(result_combis)
            for combi in result_combis:
                if len(combi) == total_length_of_str:
                    combinations.append(combi)
                check_the_index(combi, current_index, total_length_of_str)
        elif current_index == 0:
            # for those cases where it is only one number, like "2"
            result_combis = string_to_add # its just 1 letter, like a.
            # print(result_combis)
            if len(result_combis) == total_length_of_str:
                combinations.append(result_combis)

    for letter in LETTER_COMBIS[numbers_str[0]]:
        # we will add the letters starting from a, so like ad, ae, af then bd, be, bf.
        # basically another recursion problem
        check_the_index(letter, 0, len(numbers_str))

    return combinations

print(letter_combinations("23"))
print(letter_combinations(""))
print(letter_combinations("2"))
print(letter_combinations("27"))
print(letter_combinations("234"))
print(letter_combinations("79"))
