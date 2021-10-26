"""CSC108/A08: Fall 2021 -- Assignment 1: unscramble

This code is provided solely for the personal and private use of
students taking the CSC108/CSCA08 course at the University of
Toronto. Copying for purposes other than this use is expressly
prohibited. All forms of distribution of this code, whether as given
or with any changes, are expressly prohibited.

All of the files in this directory and all subdirectories are:
Copyright (c) 2021 Michelle Craig, Anya Tafliovich.

"""

# Valid moves in the game.
SHIFT = 'S'
SWAP = 'W'
CHECK = 'C'


# We provide a full solution to this function as an example.
def is_valid_move(move: str) -> bool:
    """Return True if and only if move is a valid move. Valid moves are
    SHIFT, SWAP, and CHECK.

    >>> is_valid_move('C')
    True
    >>> is_valid_move('S')
    True
    >>> is_valid_move('W')
    True
    >>> is_valid_move('R')
    False
    >>> is_valid_move('')
    False
    >>> is_valid_move('NOT')
    False

    """

    return move == CHECK or move == SHIFT or move == SWAP

# Your turn! Provide full solutions to the rest of the required functions.
def get_section_start(section_num: int, section_length: int) -> int:
    """This function should return the index of the first character in the
    chosen section with section number section_num and section length
    section_length.

    >>> get_section_start(1, 4)
    0
    >>> get_section_start(2, 4)
    4
    >>> get_section_start(3, 4)
    8
    >>> get_section_start(1, 3)
    0
    >>> get_section_start(2, 3)
    3
    >>> get_section_start(3, 3)
    6

    Assume both arguments >= 1

    """

    return section_num * section_length - section_length

def get_section(game_state: str, section_num: int, section_length: int) -> str:
    """This function should return the section of the game state game_state that
    corresponds to the given section number section_num and section length
    section_length.

    >>> get_section('csca08fun', 2, 3)
    'a08'
    >>> get_section('computer', 1, 4)
    'comp'
    >>> get_section('sciences', 4, 2)
    'es'

    Assume both section num and section length are valid.

    """

    return game_state[get_section_start(section_num, section_length):
                      get_section_start(section_num, section_length)
                      + section_length]

def is_valid_section(game_state: str, section_num: int,
                     section_length: int) -> bool:
    """This function should return True if anf only if it is possible to divide
    the game state game_state into sections of the given section_length and the
    given section number section_num.

    >>> is_valid_section('csca08fall2021', 2, 3)
    False
    >>> is_valid_section('csca08fall2021', 4, 2)
    True
    >>> is_valid_section('csca08fall2021', 8, 2)
    False

    """

    if len(game_state) % section_length == 0:
        if section_num <= len(game_state) / section_length:
            return True
    return False

def swap(game_state: str, start: int, end: int) -> str:
    """The function should return a string which is the result of applying Swap
    operation to the section of the given game state game_state string between
    index start: start and index end: end.

    >>> swap('computerscience', 0, 8)
    'romputecscience'
    >>> swap('computerscience', 6, 10)
    'computcrseience'
    >>> swap('computer', 4, 8)
    'comprteu'

    Assume that both start and end indexes are valid for given game state and
    start < end - 1

    """

    return (game_state[:start] + game_state[end - 1] +
            game_state[start + 1:end - 1] + game_state[start] +
            game_state[end:])

def shift(game_state: str, start: int, end: int) -> str:
    """The function should return a string which is the result of applying shift
    operation to the section of the given game state game_state string between
    index start: start and index end: end.

    >>> shift('computerscience', 0, 8)
    'omputercscience'
    >>> shift('computerscience', 6, 10)
    'computrsceience'
    >>> shift('sciences', 4, 8)
    'sciecesn'

    Assume that both start and end indexes are valid for given game state and
    start < end - 1

    """

    return (game_state[:start] + game_state[start + 1:end] + game_state[start] +
            game_state[end:])

def check(game_state: str, start: int, end: int, correct_state: str) -> bool:
    """The function should return True if and only if the part of the game state
    game_state string between the start index: start and end index: end is
    correct.

    >>> check('ccsa80fun', 6, 9, 'csca08fun')
    True
    >>> check('ccsa80fun', 0, 3, 'csca08fun')
    False
    >>> check('computre', 4, 8, 'computer')
    False

    """

    return game_state[start:end] == correct_state[start:end]

def check_section(game_state: str, section_num: int, section_length: int,
                  correct_state: str) -> bool:
    """The function should return True if and only if the section with the
    specified section number section_num and section length section_length is
    unscrambled correctly.

    >>> check_section('ccsa80fun', 3, 3, 'csca80fun')
    True
    >>> check_section('ccsa80fun', 1, 3, 'csca80fun')
    False
    >>> check_section('ccsa80fun', 2, 3, 'csca80fun')
    True

    Assume that section num and length are valid for given game state and
    correct state is valid answer for the game state.

    """

    return (get_section(game_state, section_num, section_length) ==
            get_section(correct_state, section_num, section_length))

def change_section(game_state: str, valid_move: str, section_num: int,
                   section_length: int) -> str:
    """The function should return a new game state game_state which results from
    applying the given game move on the section with section number section_num
    and section length section_length.

    >>> change_section('computerscience', 'W', 2, 5)
    'compucerstience'
    >>> change_section('computerscience', 'S', 2, 5)
    'compuersctience'

    Assume that section num and length are valid for game state string and
    valid move specifies either a Swap or Shift operation.

    """

    if valid_move == SWAP:
        return (swap(game_state, get_section_start(section_num, section_length),
                     get_section_start(section_num, section_length) +
                     section_length))
    return (shift(game_state, get_section_start(section_num, section_length),
                  get_section_start(section_num, section_length) +
                  section_length))

def get_move_hint(game_state: str, section_num: int, section_length: int,
                  correct_state: str) -> str:
    """The function should return a suggestion for which game move to perform
    next. If selected section of game state game_state can be unscrambled in two
    shift operations, return True, otherwise, return False.

    >>> get_move_hint('TCADOGFOXEMU', 1, 3, 'CATDGOXOFEMU')
    'S'
    >>> get_move_hint('TACDOGFOXEMU', 1, 3, 'CATDOGXOFEMU')
    'W'
    >>> get_move_hint('ATCDOGFOXEMU', 1, 3, 'CATDGOXOFEMU')
    'S'

    Assume that section num and length are valid for game state and correct
    state is the correct answer for game state.

    """

    start = get_section_start(section_num, section_length)
    end = get_section_start(section_num, section_length) + section_length
    game_state = shift(game_state, start, end)
    if game_state[start:end] != correct_state[start:end]:
        game_state = shift(game_state, start, end)
        if game_state[start:end] != correct_state[start:end]:
            return SWAP
    return SHIFT

if __name__ == '__main__':
    import doctest
    doctest.testmod()
