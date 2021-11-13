"""CSC108/A08: Fall 2021 -- Assignment 2: voting

This code is provided solely for the personal and private use of
students taking the CSC108/CSCA08 course at the University of
Toronto. Copying for purposes other than this use is expressly
prohibited. All forms of distribution of this code, whether as given
or with any changes, are expressly prohibited.

All of the files in this directory and all subdirectories are:
Copyright (c) 2021 Michelle Craig, Sophia Huynh, Sadia Sharmin,
Elizabeth Patitsas, Anya Tafliovich.

"""

from typing import List

from constants import (COL_RIDING, COL_VOTER, COL_RANK, COL_RANGE,
                       COL_APPROVAL, APPROVAL_TRUE, APPROVAL_FALSE,
                       SEPARATOR)

# In the following docstrings, 'VoteData' refers to a list of 5
# elements of the following types:
#
# at index COL_RIDING: int         (this is the riding number)
# at index COL_VOTER: int         (this is the voter number)
# at index COL_RANK: List[str]   (this is the rank ballot)
# at index COL_RANGE: List[int]   (this is the range ballot)
# at index COL_APPROVAL: List[bool]  (this is the approval ballot)

###############################################################################
# Task 0: Creating example data
###############################################################################

SAMPLE_DATA_1 = [[0, 1, ['NDP', 'LIBERAL', 'GREEN', 'CPC'], [1, 4, 2, 3],
                  [False, True, False, False]],
                 [1, 2, ['LIBERAL', 'NDP', 'GREEN', 'CPC'], [2, 1, 4, 2],
                  [False, False, True, True]],
                 [1, 3, ['GREEN', 'NDP', 'CPC', 'LIBERAL'], [1, 5, 1, 2],
                  [False, True, False, True]],
                 [1, 4, ['LIBERAL', 'CPC', 'NDP', 'GREEN'], [3, 0, 5, 2],
                  [True, False, True, True]]]
SAMPLE_ORDER_1 = ['CPC', 'GREEN', 'LIBERAL', 'NDP']


SAMPLE_DATA_2 = [[117, 12, ['LIBERAL', 'CPC', 'NDP', 'GREEN'], [4, 0, 5, 0],
                  [True, False, True, False]],
                 [117, 21, ['GREEN', 'LIBERAL', 'NDP', 'CPC'], [4, 5, 5, 5],
                  [True, True, True, True]],
                 [72, 12, ['NDP', 'LIBERAL', 'GREEN', 'CPC'], [0, 1, 1, 5],
                  [False, True, True, True]]]
SAMPLE_ORDER_2 = ['CPC', 'GREEN', 'LIBERAL', 'NDP']


SAMPLE_DATA_3 = [[1, 6, ['PEANUT', 'BUTTER', 'JELLY'], [2, 3, 5],
                  [True, True, True]],
                 [7, 3, ['BUTTER', 'PEANUT', 'JELLY'], [4, 5, 0],
                  [True, True, False]],
                 [4, 7, ['JELLY', 'BUTTER', 'PEANUT'], [5, 0, 0],
                  [True, False, False]]]
SAMPLE_ORDER_3 = ['PEANUT', 'BUTTER', 'JELLY']


SAMPLE_DATA_4 = [[7, 5, ['MAYO', 'KETCHUP', 'MUSTARD', 'SANDWICH', 'GROSS'],
                  [2, 3, 1, 3, 5], [True, True, True, True, True]],
                 [7, 6, ['KETCHUP', 'MAYO', 'MUSTARD', 'SANDWICH', 'GROSS'],
                  [4, 0, 1, 5, 4], [True, False, True, True, True]],
                 [9, 3, ['SANDWICH', 'KETCHUP', 'MUSTARD', 'MAYO', 'GROSS'],
                  [0, 5, 1, 3, 0], [False, True, True, True, False]]]
SAMPLE_ORDER_4 = ['MAYO', 'KETCHUP', 'MUSTARD', 'SANDWICH', 'GROSS']


###############################################################################
# Task 1: Data cleaning
###############################################################################

def clean_data(data: List[List[str]]) -> None:
    """Modify data so that the applicable string values are converted to
    their appropriate type, making data of type List['VoteType'].

    Pre: Each item in data is in the format
     at index COL_RIDING: a str that can be converted to an integer (riding)
     at index COL_VOTER: a str that can be converted to an integer (voter ID)
     at index COL_RANK: a SEPARATOR-separated non-empty string (rank ballot)
     at index COL_RANGE: a SEPARATOR-separated non-empty string of ints
                         (range ballot)
     at index COL_APPROVAL: a SEPARATOR-separated non-empty string of
                         APPROVAL_TRUE's and APPROVAL_FALSE's (approval ballot)

    >>> data = [['0', '1', 'NDP;Liberal;Green;CPC', '1;4;2;3', 'NO;YES;NO;NO']]
    >>> expected = [[0, 1, ['NDP', 'Liberal', 'Green', 'CPC'], [1, 4, 2, 3],
    ...             [False, True, False, False]]]
    >>> clean_data(data)
    >>> data == expected
    True
    >>> data = [['0', '1', 'NDP;LIBERAL;GREEN;CPC', '1;4;2;3', 'NO;YES;NO;NO'],
    ...         ['1', '2', 'LIBERAL;NDP;GREEN;CPC', '2;1;4;2', 'NO;NO;YES;YES'],
    ...         ['1', '3', 'GREEN;NDP;CPC;LIBERAL', '1;5;1;2', 'NO;YES;NO;YES']]
    >>> expected = [[0, 1, ['NDP','LIBERAL','GREEN','CPC'], [1, 4, 2, 3],
    ...             [False, True, False, False]],
    ...             [1, 2, ['LIBERAL','NDP','GREEN','CPC'], [2, 1, 4, 2],
    ...             [False, False, True, True]],
    ...             [1, 3, ['GREEN','NDP','CPC','LIBERAL'], [1, 5, 1, 2],
    ...             [False, True, False, True]]]
    >>> clean_data(data)
    >>> data == expected
    True
    """

    for sublist in data:
        sublist[COL_RIDING] = int(sublist[COL_RIDING])
        sublist[COL_VOTER] = int(sublist[COL_VOTER])
        sublist[COL_RANK] = sublist[COL_RANK].split(SEPARATOR)
        sublist[COL_RANGE] = sublist[COL_RANGE].split(SEPARATOR)
        sublist[COL_APPROVAL] = sublist[COL_APPROVAL].split(SEPARATOR)
        for i in range(len(sublist[COL_RANGE])):
            sublist[COL_RANGE][i] = int(sublist[COL_RANGE][i])
            if sublist[COL_APPROVAL][i] == APPROVAL_TRUE:
                sublist[COL_APPROVAL][i] = True
            elif sublist[COL_APPROVAL][i] == APPROVAL_FALSE:
                sublist[COL_APPROVAL][i] = False


###############################################################################
# Task 2: Data extraction
###############################################################################

def extract_column(data: List[list], column: int) -> list:
    """Return a list containing only the elements at index column for each
    sublist in data.

    Pre: each sublist of data has an item at index column.

    >>> extract_column([[1, 2, 3], [4, 5, 6]], 2)
    [3, 6]
    >>> extract_column([[1], [2, 3]],  0)
    [1, 2]
    >>> extract_column([[1, 2, 3], [4, 2]], 1)
    [2, 2]
    """

    extracted = []
    for sublist in data:
        extracted.append(sublist[column])
    return extracted


def extract_single_ballots(data: List['VoteData']) -> List[str]:
    """Return a list containing only the highest ranked candidate from
    each rank ballot in voting data data.

    Pre: data is a list of valid 'VoteData's
         The rank ballot is at index COL_RANK for each voter.

    >>> extract_single_ballots(SAMPLE_DATA_1)
    ['NDP', 'LIBERAL', 'GREEN', 'LIBERAL']
    >>> extract_single_ballots(SAMPLE_DATA_2)
    ['LIBERAL', 'GREEN', 'NDP']
    >>> extract_single_ballots(SAMPLE_DATA_3)
    ['PEANUT', 'BUTTER', 'JELLY']
    """

    single_ballots = []
    for sublist in data:
        single_ballots.append(sublist[COL_RANK][0])
    return single_ballots


def get_votes_in_riding(data: List['VoteData'],
                        riding: int) -> List['VoteData']:
    """Return a list containing only voting data for riding riding from
    voting data data.

    Pre: data is a list of valid 'VoteData's

    >>> expected = [[1, 2, ['LIBERAL', 'NDP', 'GREEN', 'CPC'], [2, 1, 4, 2],
    ...              [False, False, True, True]],
    ...             [1, 3, ['GREEN', 'NDP', 'CPC', 'LIBERAL'], [1, 5, 1, 2],
    ...              [False, True, False, True]],
    ...             [1, 4, ['LIBERAL', 'CPC', 'NDP', 'GREEN'], [3, 0, 5, 2],
    ...              [True, False, True, True]]]
    >>> get_votes_in_riding(SAMPLE_DATA_1, 1) == expected
    True
    >>> expected = [[117, 12, ['LIBERAL', 'CPC', 'NDP', 'GREEN'], [4, 0, 5, 0],
    ...              [True, False, True, False]],
    ...             [117, 21, ['GREEN', 'LIBERAL', 'NDP', 'CPC'], [4, 5, 5, 5],
    ...              [True, True, True, True]]]
    >>> get_votes_in_riding(SAMPLE_DATA_2, 117) == expected
    True
    """

    votes_in_riding = []
    for sublist in data:
        if sublist[COL_RIDING] == riding:
            votes_in_riding.append(sublist)
    return votes_in_riding


###############################################################################
# Task 3.1: Plurality Voting System
###############################################################################

def voting_plurality(single_ballots: List[str],
                     party_order: List[str]) -> List[int]:
    """Return the total number of ballots cast for each party in
    single-candidate ballots single_ballots, in the order specified in
    party_order.

    Pre: each item in single_ballots appears in party_order

    >>> voting_plurality(['GREEN', 'GREEN', 'NDP', 'GREEN', 'CPC'],
    ...                  SAMPLE_ORDER_1)
    [1, 3, 0, 1]
    >>> voting_plurality(['NDP', 'LIBERAL', 'LIBERAL', 'GREEN', 'GREEN',
    ...                  'GREEN', 'CPC', 'CPC', 'CPC', 'CPC'], SAMPLE_ORDER_2)
    [4, 3, 2, 1]
    >>> voting_plurality(['PEANUT', 'BUTTER', 'BUTTER', 'JELLY', 'JELLY',
    ...                  'JELLY'], SAMPLE_ORDER_3)
    [1, 2, 3]
    """

    number_of_votes = [0] * len(party_order)

    for party in party_order:
        for ballot in single_ballots:
            if ballot == party:
                number_of_votes[party_order.index(party)] += 1
    return number_of_votes


###############################################################################
# Task 3.2: Approval Voting System
###############################################################################

# Note: even though the only thing we need from party_order in this
# function is its length, we still design all voting functions to
# receive party_order, for consistency and readability.
def voting_approval(approval_ballots: List[List[bool]],
                    party_order: List[str]) -> List[int]:
    """Return the total number of approvals for each party in approval
    ballots approval_ballots, in the order specified in party_order.

    Pre: len of each sublist of approval_ballots is len(party_order)
         the approvals in each ballot are specified in the order of party_order

    >>> voting_approval([[True, True, False, False],
    ...                  [False, False, False, True],
    ...                  [False, True, False, False]], SAMPLE_ORDER_1)
    [1, 2, 0, 1]
    >>> voting_approval([[True, False, True, False],
    ...                  [True, True, True, True],
    ...                  [False, True, True, True]], SAMPLE_ORDER_2)
    [2, 2, 3, 2]
    """

    number_of_approvals = [0] * len(party_order)

    for sublist in approval_ballots:
        for i in range(len(party_order)):
            if sublist[i]:
                number_of_approvals[i] += 1
    return number_of_approvals


###############################################################################
# Task 3.3: Range Voting System
###############################################################################

def voting_range(range_ballots: List[List[int]],
                 party_order: List[str]) -> List[int]:
    """Return the total score for each party in range ballots
    range_ballots, in the order specified in party_order.

    Pre: len of each sublist of range_ballots is len(party_order)
         the scores in each ballot are specified in the order of party_order

    >>> voting_range([[1, 3, 4, 5], [5, 5, 1, 2], [1, 4, 1, 1]],
    ...              SAMPLE_ORDER_1)
    [7, 12, 6, 8]
    >>> voting_range([[4, 0, 5, 0], [4, 5, 5, 5], [0, 1, 1, 5]],
    ...              SAMPLE_ORDER_2)
    [8, 6, 11, 10]
    """

    total_votes = [0] * len(party_order)

    for sublist in range_ballots:
        for i in range(len(party_order)):
            total_votes[i] += sublist[i]
    return total_votes


###############################################################################
# Task 3.4: Borda Count Voting System
###############################################################################

def voting_borda(rank_ballots: List[List[str]],
                 party_order: List[str]) -> List[int]:
    """Return the Borda count for each party in rank ballots rank_ballots,
    in the order specified in party_order.

    Pre: each ballot contains all and only elements of party_order

    >>> voting_borda([['LIBERAL', 'GREEN', 'CPC', 'NDP'],
    ...               ['CPC', 'LIBERAL', 'GREEN', 'NDP'],
    ...               ['LIBERAL', 'NDP', 'GREEN', 'CPC']], SAMPLE_ORDER_1)
    [4, 4, 8, 2]
    >>> voting_borda([['LIBERAL', 'CPC', 'NDP', 'GREEN'],
    ...               ['GREEN', 'LIBERAL', 'NDP', 'CPC'],
    ...               ['NDP', 'LIBERAL', 'GREEN', 'CPC']], SAMPLE_ORDER_2)
    [2, 4, 7, 5]
    """

    rank_totals = [0] * len(party_order)

    for sublist in rank_ballots:
        for i in range(len(party_order)):
            rank_totals[party_order.index(sublist[i])] += (len(party_order) - 1
                                                           - i)
    return rank_totals


###############################################################################
# Task 3.5: Instant Run-off Voting System
###############################################################################

def remove_party(rank_ballots: List[List[str]], party_to_remove: str) -> None:
    """Change rank ballots rank_ballots by removing the party
    party_to_remove from each ballot.

    Pre: party_to_remove is in all of the ballots in rank_ballots.

    >>> ballots = [['LIBERAL', 'GREEN', 'CPC', 'NDP'],
    ...            ['CPC', 'NDP', 'LIBERAL', 'GREEN'],
    ...            ['NDP', 'CPC', 'GREEN', 'LIBERAL']]
    >>> remove_party(ballots, 'NDP')
    >>> ballots == [['LIBERAL', 'GREEN', 'CPC'],
    ...             ['CPC', 'LIBERAL', 'GREEN'],
    ...             ['CPC', 'GREEN', 'LIBERAL']]
    True
    >>> ballots = [['PEANUT', 'BUTTER', 'JELLY'],
    ...            ['BUTTER', 'PEANUT', 'JELLY'],
    ...            ['JELLY', 'BUTTER', 'PEANUT']]
    >>> remove_party(ballots, 'PEANUT')
    >>> ballots = [['BUTTER', 'JELLY'],
    ...            ['BUTTER', 'JELLY'],
    ...            ['BUTTER', 'JELLY']]
    """

    for sublist in rank_ballots:
        sublist.remove(party_to_remove)


def get_lowest(party_tallies: List[int], party_order: List[str]) -> str:
    """Return the name of the party with the lowest number of votes in the
    list of vote counts per party party_tallies. In case of a tie,
    return the party that occurs earlier in party_order. Totals in
    party_tallies are ordered by party_order.

    Pre: len(party_tallies) == len(party_order) > 0

    >>> get_lowest([16, 100, 4, 200], SAMPLE_ORDER_1)
    'LIBERAL'
    >>> get_lowest([2, 1, 1, 3], SAMPLE_ORDER_2)
    'GREEN'
    """

    return party_order[party_tallies.index(min(party_tallies))]


def get_winner(party_tallies: List[int], party_order: List[str]) -> str:
    """Return the name of the party with the highest number of votes in the
    list of vote counts per party party_tallies. In case of a tie,
    return the party that occurs earlier in party_order. Totals in
    party_tallies are ordered by party_order.

    Pre: len(party_tallies) == len(party_order) > 0

    >>> get_winner([16, 100, 4, 200], SAMPLE_ORDER_1)
    'NDP'
    >>> get_winner([1, 3, 3, 2], SAMPLE_ORDER_2)
    'GREEN'
    """

    return party_order[party_tallies.index(max(party_tallies))]


def voting_irv(rank_ballots: List[List[str]], party_order: List[str]) -> List:
    """Return the party which wins when IRV is performed on the list of
    rank ballots rank_ballots. Change rank_ballots and party_order as
    needed in IRV, removing parties that are eliminated in the
    process. Each ballot in rank_ballots is ordered by party_order.

    Pre: each ballot contains all and only elements of party_order
         len(rank_ballots) > 0

    >>> order = ['CPC', 'GREEN', 'LIBERAL', 'NDP']
    >>> ballots = [['LIBERAL', 'GREEN', 'CPC', 'NDP'],
    ...            ['CPC', 'NDP', 'LIBERAL', 'GREEN'],
    ...            ['NDP', 'CPC', 'GREEN', 'LIBERAL']]
    >>> voting_irv(ballots, order)
    'NDP'
    >>> ballots == [['LIBERAL', 'NDP'],
    ...             ['NDP', 'LIBERAL'],
    ...             ['NDP', 'LIBERAL']]
    True
    >>> order
    ['LIBERAL', 'NDP']
    """

    firsts = [0] * len(party_order)

    while max(firsts) <= len(party_order) // 2 + 1:
        remove_party(rank_ballots, get_lowest(firsts, party_order))
        party_order.remove(get_lowest(firsts, party_order))
        for sublist in rank_ballots:
            firsts[party_order.index(sublist[0])] += 1
    return party_order[firsts.index(max(firsts))]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
