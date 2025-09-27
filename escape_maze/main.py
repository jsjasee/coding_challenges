DIRECTIONS = [(+1, 0), (-1, 0), (0, +1), (0, -1)]

def can_exit(maze):

    visited = []
    num_rows = len(maze)
    num_columns = len(maze[0])

    def in_bounds(row, column):
        if 0 <= row < num_rows and 0 <= column < num_columns:
            return True
        return False

    def check_for_continuous_path(prev_row, prev_column, current_row, current_column):
        # this is to prevent 'diagonal' grids from being added in case a previous deadend is met and the previous grids leading to the deadend is still in the current path.
        if (current_row != prev_row) and (current_column != prev_column):
            return False
        elif (abs(current_row - prev_row) >= 1) and (abs(current_column - prev_column) >= 1):
            return False
        return True

    def check_for_neighbours(row_to_check, column_to_check):
        """Checks for all the neighbouring numbers surrounding that number we are checking."""
        neighbours_to_check = []
        for row_direction, column_direction in DIRECTIONS:
            new_row = row_to_check + row_direction
            new_column = column_to_check + column_direction
            if in_bounds(new_row, new_column):
                neighbours_to_check.append((new_row, new_column))
        return neighbours_to_check

    def find_path_out(list_of_neighbours, path):

        for row_to_find, column_to_find in list_of_neighbours:
            if not check_for_continuous_path(path[-1][0], path[-1][1], row_to_find, column_to_find):
                # print(path[-1])
                path.pop()

            if (row_to_find, column_to_find) in visited:
                continue

            if maze[row_to_find][column_to_find] == 0:
                if (row_to_find == num_rows - 1) and (column_to_find == num_columns - 1):
                    # print(path) # not required but added just for additional challenge lolz
                    return True

                if not check_for_continuous_path(path[-1][0], path[-1][1], row_to_find, column_to_find):
                    path.pop()
                    # check the path AGAIN. right before appending this grid to the path.
                path.append((row_to_find, column_to_find))
                visited.append((row_to_find, column_to_find))
                possible_neighbours = check_for_neighbours(row_to_find, column_to_find)
                result = find_path_out(possible_neighbours, path)
                if result:
                    return True

        return False

    # STEP 1: Check if botton right is 0
    if maze[num_rows - 1][num_columns - 1] != 0:
        print("Output = False")
        return False

    # STEP 2: Get all the neighbours starting from the top left grid
    visited.append((0, 0))
    neighbours = check_for_neighbours(row_to_check=0, column_to_check=0)

    # STEP 3: start checking the neighbours for 0s. The path should always contain the top left grid

    final_result = find_path_out(neighbours, [(0,0)])
    print("Output =", final_result)

can_exit([
  [0, 1, 1, 1, 1, 1, 1],
  [0, 0, 1, 1, 0, 1, 1],
  [1, 0, 0, 0, 0, 1, 1],
  [1, 1, 1, 1, 0, 0, 1],
  [1, 1, 1, 1, 1, 0, 0]
])

can_exit([
  [0, 1, 1, 1, 1, 1, 1],
  [0, 0, 1, 0, 0, 1, 1],
  [1, 0, 0, 0, 0, 1, 1],
  [1, 1, 0, 1, 0, 0, 1],
  [1, 1, 0, 0, 1, 1, 1]
])
# This maze only has dead ends!

can_exit([
  [0, 1, 1, 1, 1, 0, 0],
  [0, 0, 0, 0, 1, 0, 0],
  [1, 1, 1, 0, 0, 0, 0],
  [1, 1, 1, 1, 1, 1, 0],
  [1, 1, 1, 1, 1, 1, 1]
])
# Exit only one block away, but unreachable!

can_exit([
  [0, 1, 1, 1, 1, 0, 0],
  [0, 0, 0, 0, 1, 0, 0],
  [1, 1, 1, 0, 0, 0, 0],
  [1, 0, 0, 0, 1, 1, 0],
  [1, 1, 1, 1, 1, 1, 0]
])