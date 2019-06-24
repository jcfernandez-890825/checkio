def group_equal(els):
    from itertools import groupby
    # Return a list of consecutive groups
    return [
        # Make each consecutive groups into a list
        list(g)
        for k, g in groupby(els)
    ]


'''
Chekio Mission Link:
https://py.checkio.org/en/mission/group-equal-consecutive/
Chekio Solution Link:
https://py.checkio.org/mission/group-equal-consecutive/publications/jcfernandez/python-3/only-one-line/share/6b73d13c60d38396f1cd70d241b3ef5d/
Chekio Profile Link:
https://py.checkio.org/user/jcfernandez/solutions/share/83d63afe87a24e810571c961a5f66dfb/
'''

if __name__ == '__main__':
    print("Example:")
    print(group_equal([1, 1, 4, 4, 4, "hello", "hello", 4]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert group_equal([1, 1, 4, 4, 4, "hello", "hello", 4]) == [[1, 1], [4, 4, 4], ["hello", "hello"], [4]]
    assert group_equal([1, 2, 3, 4]) == [[1], [2], [3], [4]]
    assert group_equal([1]) == [[1]]
    assert group_equal([]) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")
