from typing import List


def checkio(game_result: List[str]) -> str:
    from itertools import chain

    positions = chain(
        # Search winner by row
        ((x, y) for x in range(3) for y in range(3)),
        # Search winner by column
        ((x, y) for y in range(3) for x in range(3)),
        # Search winner by SW-NE diagonal
        zip(range(3), range(2, -1, -1)),
        # Search winner by NW-SE diagonal
        zip(range(3), range(3)),
    )

    # Get the first 3 positions to analyse
    first, second, third = next(positions), next(positions), next(positions)
    while first is not None:
        # If we have 3 X or 3 O there is a winner
        if game_result[first[0]][first[1]] == game_result[second[0]][second[1]] == game_result[third[0]][third[1]] != '.':
            return game_result[first[0]][first[1]]

        # Keep looking
        # Get the next 3 positions to analyse
        first, second, third = next(positions, None), next(positions, None), next(positions, None)

    # We don't have a winner
    # Is a draw
    return 'D'


'''
Chekio Mission Link:
https://py.checkio.org/en/mission/x-o-referee/
Chekio Solution Link:
https://py.checkio.org/mission/x-o-referee/publications/jcfernandez/python-3/using-iterators/share/a19fc78c52f271dc7d92a2ff38f1b57e/
Chekio Profile Link:
https://py.checkio.org/user/jcfernandez/solutions/share/83d63afe87a24e810571c961a5f66dfb/
'''

if __name__ == '__main__':
    print("Example:")
    print(checkio(["X.O",
                   "XX.",
                   "XOO"]))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
