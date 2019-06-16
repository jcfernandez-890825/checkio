def safe_pawns(pawns: set) -> int:
    return len(  # Count how many pawns are safe
        set(
            filter(  # A pawn is safe if ...
                lambda p: any(  # has another pawn 1 row below it and either on the left(-1) or right(+1) column
                    chr(ord(p[0]) + n) + chr(ord(p[1]) - 1)
                    in pawns for n in (-1, 1)
                ),
                pawns
            )
        )
    )


'''
Chekio Mission Link:
https://py.checkio.org/en/mission/pawn-brotherhood/
Chekio Solution Link:
https://py.checkio.org/mission/pawn-brotherhood/publications/jcfernandez/python-3/only-one-line/share/59aa6392a3790f96ea6fdacb60ab72b9/
Chekio Profile Link:
https://py.checkio.org/user/jcfernandez/solutions/share/83d63afe87a24e810571c961a5f66dfb/
'''

if __name__ == '__main__':
    print(safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}))
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
