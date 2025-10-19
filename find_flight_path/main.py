def find_path(flight_list, letter_to_find, flight_path):
    start_points = [flight for flight in flight_list if flight[0] == letter_to_find]

    if len(start_points) == 1:
        flight_list.remove(start_points[0])
        flight_path.append(start_points[0])
    elif len(start_points) == 2:
        chosen_flight = []
        for i in range(len(start_points) - 1):
            if start_points[i] < start_points[i + 1]:
                chosen_flight = start_points[i]
            else:
                chosen_flight = start_points[i + 1]
        # print(chosen_flight)
        flight_path.append(chosen_flight)
        flight_list.remove(chosen_flight)

    if start_points:
        find_path(flight_list, flight_path[-1][-1], flight_path)

    return flight_path

def parse_flights(final_path):
    final_output = [final_path[0][0]]
    for flight_route in final_path:
        final_output.append(flight_route[1])
    print(final_output)

parse_flights(find_path(flight_list=[["C", "F"], ["A", "C"], ["I", "Z"], ["F", "I"]], letter_to_find="A", flight_path=[]))
parse_flights(find_path([["A","C"],["A","B"],["C","B"],["B","A"],["B","C"]], "A", flight_path=[]))
parse_flights(find_path([["Y", "L"], ["D", "A"], ["A", "D"], ["R", "Y"], ["A", "R"]], "A", flight_path=[]))

# print(["A", "B"] > ["A", "C"]) # returns true if AB < AC, false if AB > AC aka the first one is the alphabetical one

