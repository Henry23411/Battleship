"""Battleship Functions"""

# Use these constants in your code
from typing import TextIO, List

MIN_SHIP_SIZE = 1
MAX_SHIP_SIZE = 10
MAX_GRID_SIZE = 10
UNKNOWN = "-"
EMPTY = "."
HIT = "X"
MISS = "M"


def read_ship_data(game_file: TextIO) -> List:
    """
    Return a list containing the ship characters in game_file as a list
    of strings at index 0, and ship sizes in game_file as a list of ints
    at index 1.
    """

    ship_characters = game_file.readline().split()

    ship_sizes = game_file.readline().split()

    for i in range(len(ship_sizes)):
        ship_sizes[i] = int(ship_sizes[i])

    return [ship_characters, ship_sizes]


##################################################
# Write the rest of the required functions here,
# following the function design recipe
##################################################

def has_ship(fleet_grid, row, col, ships, sizes):
    
    """
    This function returns True iff the ship appears with the correct size, 
    completely in a row or a completely in a column at the given starting cell.

    >>> has_ship([['.','b','.'], ['.','b','.'], ['a','a','a']], 2, 0, 'a', 3)
    True
    >>> has_ship([['.','b','.'], ['.','b','.'], ['a','b','a']], 0, 1, 'b', 2)
    False
    """
    
    # checking horizontal
    if fleet_grid[row][col:col + sizes].count(ships) == sizes:
        return True
    
    # checking vert
    boolean_num = 0
    if row + sizes <= len(fleet_grid):
        for i in range(len(fleet_grid)):
            if row + i < len(fleet_grid) and \
            fleet_grid[row + i][col] == ships:
                boolean_num = boolean_num + 1
        if boolean_num == sizes:
            return True
        
    return False

def validate_character_count(fleet_grid, ships, sizes):
    
    """
    This function returns True iff the grid contains the correct number of ship 
    characters for each ship, and the correct number of EMPTY characters.

    >>> fleet_grid = [['.','b','.'], ['.','b','.'], ['a','a','a']]
    >>> ships = ['a', 'b'] 
    >>> sizes = [3, 2]
    >>> validate_character_count(fleet_grid, ships, sizes)
    True
    >>> fleet_grid = [['.','b','.'], ['.','b','.'], ['a','a','a']]
    >>> ships = ['a', 'b']
    >>> sizes = [2, 2]
    >>> validate_character_count(fleet_grid, ships, sizes)
    False
    """

    empty_num = 0
    total_num = 0
    char_num = 0
    ships_list = []

    # Count empty_num and total_num
    # Make ships_list containing every ship chars found in fleet_grid
    for inner in fleet_grid:
        empty_num += inner.count(EMPTY)
        total_num += len(inner)
        for i in inner:
            if i != EMPTY:
                ships_list.append(i)

    # Compare ships_list to sizes with ships
    # Count up char_num
    # Compare if fleet_grid has right numb of ship chars
    for i in range(len(ships)):
        char_num += sizes[i]
        if ships_list.count(ships[i]) != sizes[i]:
            return False

    # Does fleet_grid has correct amt of EMPTYs
    return total_num == empty_num + char_num 

def validate_ship_positions(fleet_grid, ships, sizes):
    
    """
    This function returns True iff the grid contains each ship aligned 
    completely in a row or column. That is, it should check that each ship is 
    contained completely in consecutive cells all in the same row, or all in 
    the same column, depending on if it is oriented horizontally or vertically 
    (no other orientation).

    >>> fleet_grid = [['.','b','.'], ['.','b','.'], ['a','a','a']]
    >>> validate_character_count(fleet_grid, ['a', 'b'], [3, 2])
    True
    >>> fleet_grid = [['.','.','b'], ['.','.','.'], ['a','a','a']]
    >>> validate_character_count(fleet_grid, ['a', 'b'], [3, 2])
    False
    """
    
    boolean_num = 0
    for ship in range(len(ships)):

        # Looking for first ship char
        for row in range(len(fleet_grid)):
            if boolean_num < len(ships):
                col = 0
                while fleet_grid[row][col] != ships[ship] and \
                col < len(fleet_grid[row]) - 1:
                    col = col + 1

                # Does starting cell contain ship
                if has_ship(fleet_grid, row, col, ships[ship], sizes[ship]):
                    boolean_num = boolean_num + 1
    return boolean_num == len(ships)
        
def validate_fleet_grid(fleet_grid, ships, sizes):
    
    """
    Return True iff the fleet_grid is a valid fleet grid for the game.
    
    >>> fleet_grid = [['.','b','.'], ['.','b','.'], ['a','a','a']]
    >>> ships = ['a', 'b'] 
    >>> sizes = [3, 2]
    >>> validate_fleet_grid(fleet_grid, ships, sizes)
    True
    >>> fleet_grid = [['.','b','.'], ['.','b','.'], ['a','a','a']]
    >>> ships = ['a', 'c']
    >>> sizes = [2, 2]
    >>> validate_character_count(fleet_grid, ships, sizes)
    False
    """
    
    # Is fleet_grid valid fleet grid for the game
    return validate_character_count(fleet_grid, ships, sizes) and \
           validate_ship_positions(fleet_grid, ships, sizes)

def is_valid_cell(row, col, grid_size):
    
    """
    This function returns True iff the cell specified by the row and the 
    column is a valid cell inside a square grid of that size.

    >>> valid_cell(1, 2, 3)
    True
    >>> valid_cell(3, 2, 1)
    False
    """
    
    # Is row and col in grid
    return 0 <= row < grid_size and 0 <= col < grid_size

def is_not_given_char(row, col, grid, character):
    
    """
    This function returns True iff the cell specified by the row and column is 
    not the given character.

    >>> is_not_given_char(2, 2, [['.','b','.'], ['.','b','.'], ['a','a','a']], \
    'b')
    True
    >>> is_not_given_char(0, 1, [['.','b','.'], ['.','b','.'], ['a','a','a']], \
    'b')
    False
    """
    
    # If cell given by row and col are diff as char
    return grid[row][col] != character

def update_fleet_grid(row, col, fleet_grid, ships, sizes, hits_list):
    
    """
    This function updates the fleet grid (by converting the ship character in 
    the cell to upper-case), and also the hits list to indicate that there has 
    been a hit.

    >>> fleet_grid = [['.', 'b', '.'], ['.', 'b', '.'], ['a', 'a', 'a']]
    >>> ships = ['a', 'b']
    >>> sizes = [3, 2]
    >>> hits_list = [0, 0]
    >>> update_fleet_grid(2, 2, fleet_grid, ships, sizes, hits_list)
    >>> fleet_grid
    [['.', 'b', '.'], ['.', 'b', '.'], ['a', 'a', 'A']]
    >>> hits_list
    [1, 0]
    >>> update_fleet_grid(0, 1, fleet_grid, ships, sizes, hits_list)
    >>> fleet_grid
    [['.', 'B', '.'], ['.', 'b', '.'], ['a', 'a', 'A']]
    >>> hits_list
    [1, 1]
    """
    
    ship_index = ships.index(fleet_grid[row][col])
    hits_list[ship_index] = hits_list[ship_index] + 1
    fleet_grid[row][col] = fleet_grid[row][col].upper()

    # For if ship sinks
    if hits_list[ship_index] == sizes[ship_index]:
        print_sunk_message(sizes[ship_index], ships[ship_index])
    
def update_target_grid(row, col, target_grid, fleet_grid):
    
    """
    This function sets the element of the specified cell in the target grid to 
    HIT or MISS using the information from the corresponding cell from the 
    fleet grid.
    
    >>> fleet_grid = [['.','b','.'], ['.','b','.'], ['a','a','a']]
    >>> target_grid = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
    >>> update_target_grid(2, 2, target_grid, fleet_grid)
    >>> target_grid
    [['-', '-', '-'], ['-', '-', '-'], ['-', '-', 'X']]
    >>> update_target_grid(0, 0, target_grid, fleet_grid)
    >>> target_grid
    [['M', '-', '-'], ['-', '-', '-'], ['-', '-', 'X']]
    """
    
    # Check if cell in fleet_grid has ship
    if fleet_grid[row][col] == EMPTY:
        target_grid[row][col] = MISS
        
    else:
        target_grid[row][col] = HIT
        
def is_win(sizes, hits_list):
    
    """
    This function returns True iff the number of hits for each ship in the hits 
    list is the same as the size of each ship, i.e., if each ship has been sunk.

    >>> is_win([2, 3, 4], [2, 3, 4])
    True
    >>> is_win([2, 3, 4], [2, 2, 2])
    False
    """
    
    # If the numbers in sizes are the same as the numbers corresponding in
    # hits_list, the game is won
    return sizes == hits_list


##################################################
# Helper function to call in update_fleet_grid
# Do not change!
##################################################


def print_sunk_message(ship_size: int, ship_character: str) -> None:
    """
    Print a message telling player that a ship_size ship with ship_character
    has been sunk.
    """

    print("The size {0} {1} ship has been sunk!".format(ship_size, ship_character))


if __name__ == "__main__":
    import doctest

    # uncomment the line below to run the docstring examples
    doctest.testmod()
