import sys
sys.path.insert(0, 'new_pyta')

import builtins
import battleship_functions as bf
import io
import python_ta

print('==================== Start: checking coding style ===================')

python_ta.check_all('battleship_functions.py', config='new_pyta/a2_pyta.txt')

print('=================== End: checking coding style ===================\n')

def is_grid(lst):
    """ (object) -> bool

    Return True iff lst is a list of list of str.

    >>> is_grid([['a', 'b', 'c']])
    True
    """

    if not isinstance(lst, list):
        return False

    for element in lst:
        if not isinstance(element, list):
            return False

        for s in element:
            if not isinstance(s, str):
                return False

    return True


# Get the initial value of the constants
constants_before = [1, 10, '-', '.', 'X', 'M']

print('============ Start: checking parameter and return types ============')
# Type check bf.read_ship_data

game_file = io.StringIO('t\n1\nt')
result = bf.read_ship_data(game_file)
print('Checking read_ship_data...')
assert isinstance(result, list), \
       '''bf.read_ship_data should return a list, but returned {0}
       .'''.format(type(result))
assert isinstance(result[0][0], str), \
       '''bf.read_ship_data should return a list where the first element
       is a list of str, but the first element is a list of {0}
       .'''.format(type(result[0][0]))
assert isinstance(result[1][0], int), \
       '''bf.read_ship_data should return a list where the second element
       is a list of int, but the second element is a list of {0}
       .'''.format(type(result[1][0]))
print('  check complete')

print('Checking has_ship...')
# Type check bf.has_ship
fleet_grid = [['a', 'a', 'a'], ['b', 'b', '.'], ['.', '.', '.']]
result = bf.has_ship(fleet_grid, 0, 0, 'a', 3)
assert isinstance(result, bool), \
       '''bf.has_ship should return a bool, but returned {0}
       .'''.format(type(result))
print('  check complete')


# Type check bf.validate_character_count
print('Checking validate_character_count...')
fleet_grid = [['a', 'a', 'a'], ['b', 'b', '.'], ['.', '.', '.']]
ships = ['a', 'b']
sizes = [3, 2]
result = bf.validate_character_count(fleet_grid, ships, sizes)

assert isinstance(result, bool), \
       '''bf.validate_character_count should return a bool, but returned {0}
       .'''.format(type(result))
print('  check complete')

# Type check bf.validate_ship_positions
print('Checking validate_ship_positions...')
fleet_grid = [['a', 'a', 'a'], ['b', 'b', '.'], ['.', '.', '.']]
ships = ['a', 'b']
sizes = [3, 2]
result = bf.validate_ship_positions(fleet_grid, ships, sizes)
assert isinstance(result, bool), \
       '''bf.validate_ship_positions should return a bool, but returned {0}
       .'''.format(type(result))
print('  check complete')

# Type check bf.validate_fleet_grid
print('Checking validate_fleet_grid...')
fleet_grid = [['a', 'a', 'a'], ['b', 'b', '.'], ['.', '.', '.']]
ships = ['a', 'b']
sizes = [3, 2]
result = bf.validate_fleet_grid(fleet_grid, ships, sizes)
assert isinstance(result, bool), \
       '''bf.validate_fleet_grid should return a bool, but returned {0}
       .'''.format(type(result))
print('  check complete')

# Type check bf.is_valid_cell
print('Checking is_valid_cell...')
result = bf.is_valid_cell(1, 1, 3)
assert isinstance(result, bool), \
       '''bf.is_valid_cell should return a bool, but returned {0}
       .'''.format(type(result))
print('  check complete')

# Type check bf.is_not_given_char
print('Checking is_not_given_char...')
result = bf.is_not_given_char(1, 1, [['a','-'], ['-','b']], '-')
assert isinstance(result, bool), \
       '''bf.is_not_given_char should return a bool, but returned {0}
       .'''.format(type(result))
print('  check complete')

# Type check bf.update_fleet_grid
print('Checking update_fleet_grid...')
result = bf.update_fleet_grid(0, 1, [['.', 'a'], ['.', 'a']], ['a'], [2], [0])
assert result is None, \
       '''bf.update_fleet_grid should return None, but returned {0}
       .'''.format(type(result))
print('  check complete')

# Type check bf.update_target_grid
print('Checking update_target_grid...')
target_grid = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
fleet_grid = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]
result = bf.update_target_grid(0, 0, target_grid, fleet_grid)
assert result is None, \
       '''bf.update_target_grid should return None, but returned {0}
       .'''.format(type(result))
print('  check complete')

# Type check bf.is_win
print('Checking is_win...')
result = bf.is_win([1, 2, 3], [1, 2, 3])
assert isinstance(result, bool), \
       '''bf.is_win should return a bool, but returned {0}
       .'''.format(type(result))
print('  check complete')

print('============= End: checking parameter and return types =============\n')

print('========== Start: checking whether constants are unchanged ==========')

# Get the final values of the constants
constants_after = [bf.MIN_SHIP_SIZE, bf.MAX_SHIP_SIZE, bf.UNKNOWN, bf.EMPTY, bf.HIT, bf.MISS]

print('Checking constants...')
# Check whether the constants are unchanged.
assert constants_before == constants_after, \
       '''Your function(s) modified the value of one or more constants.
       Edit your code so that the value of the constants are not
       changed by your functions.'''

print('  check complete')

print('=========== End: checking whether constants are unchanged ===========')
