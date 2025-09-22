DIRECTIONS = [(+1, 0), (-1, 0), (0, +1), (0, -1)]

def trace_word_path(word, grid):

    visited = []
    starting_positions = []
    num_rows = len(grid)
    num_columns = len(grid[0])

    def in_bounds(row, column):
        if 0 <= row < num_rows and 0 <= column < num_columns:
            return True
        return False

    def check_paths(row_to_check, column_to_check):
        neighbours_to_check = []
        for row_direction, column_direction in DIRECTIONS:
            new_row = row_to_check + row_direction
            new_column = column_to_check + column_direction
            if in_bounds(new_row, new_column):
                neighbours_to_check.append((new_row, new_column))
        return neighbours_to_check

    def find_matched_word(word_id:int, list_of_neighbours:list, path:list):
        if word_id >= len(word):
            print(f"Output = {path}")
            return True # 🟡-> the return doesn't stop the code from continuing printing statements after a path is found

        # print(f"Word to match: {word[word_id]}")

        for row_to_find, column_to_find in list_of_neighbours:

            if (row_to_find, column_to_find) in visited:
                continue

            if grid[row_to_find][column_to_find] == word[word_id]:
                path.append((row_to_find, column_to_find))
                # evaluate for neighbours and try 1 -> branch
                possible_neighbours = check_paths(row_to_find, column_to_find)
                # print(possible_neighbours)
                # print(path)
                visited.append((row_to_find, column_to_find))
                result = find_matched_word(word_id + 1, possible_neighbours, path)
                if result:
                    return True
                    # we capture the result of the return statement RIGHT HERE, not where the yellow emoji is or the other return statements (also with yellow emoji)

                # elif not result and word_id == len(word): 🔴 -> THIS print statement DOESN'T even run cos if there are NO matched neighbours, this if block will not even run.
                #     print("Not found")
                #     return False
                # THERE IS NO NEED TO BACKTRACK the path if the letter does NOT GIVE US any valid neighbours. this path is a dead one. also note the below 2 statements only run when there is no matched word / no valid neighbours. as the code breaks out of that recursion cycle.
                # print(f"Before pop: {path}")
                # path.pop() # WHY DO THIS?? USELESS! -> .pop removes the last element by default if no index is provided, whereas .remove() removes the FIRST MATCHED element in the list.
                # print(f"After pop: {path}")

        # return false at the end of the for loop to END this branch & recursion, when NO neighbours work
        # print("path is dead")
        return False # 🟡

            # go to the next starting position and reset word_id
            # restart whole process again

    # PHASE 1: GET ALL STARTING POSITIONS
    for row_in_grid in range(num_rows):
        for column_in_grid in range(num_columns):
            if grid[row_in_grid][column_in_grid] == word[0]:
                starting_positions.append((row_in_grid, column_in_grid))

    # PHASE 2: GET NEIGHBOURS OF ALL THE STARTING POSITIONS
    path_results = []
    for position in starting_positions:
        visited.append(position)
        neighbours = check_paths(row_to_check=position[0], column_to_check=position[1])

        # PHASE 3: CHOOSE 1 NEIGHBOUR AND START
        path_result = find_matched_word(word_id=1, list_of_neighbours=neighbours, path=[position])
        path_results.append(path_result)
    if True in path_results:
        return # we do this because the first path might give path_result True, the second one might give path_result False. but this means a completed path is found. only when all results are False, then we print 'Not found'
    else:
        print('Not present')



trace_word_path(word="BISCUIT", grid=
[ ["B", "I", "T", "R"],
  ["I", "U", "A", "S"],
  ["S", "C", "V", "W"],
  ["D", "O", "N", "E"]
])

trace_word_path("HELPFUL", [
  ["L","I","T","R"],
  ["U","U","A","S"],
  ["L","U","P","O"],
  ["E","F","E","H"]
])

trace_word_path("UKULELE", [
  ["N", "H", "B", "W"],
  ["E", "X", "A", "D"],
  ["L", "A", "U", "U"],
  ["E", "L", "U", "K"]
])

trace_word_path("SURVIVAL", [
  ["V", "L", "R", "L"],
  ["V", "A", "I", "V"],
  ["I", "O", "S", "C"],
  ["V", "R", "U", "F"]
])