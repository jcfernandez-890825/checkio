def checkio(array):
    """
        sums even-indexes elements and multiply at the last
    """
    from functools import reduce
    from itertools import islice

    # Sum elements using reduce(...) function
    return reduce(
        lambda x, y: x + y,
        # Make an iterator of elements with even indexes
        islice(
            array,
            None, None, 2
        )
        # Multiply the sum with the last element
        # Make the whole operation only if the array length is higher than 0
    ) * array[-1] if len(array) > 0 else 0


'''
Chekio Mission Link:
https://py.checkio.org/en/mission/even-last/
Chekio Solution Link:
https://py.checkio.org/mission/even-last/publications/jcfernandez/python-3/only-one-line-using-reduce-and-islice/share/5cfbca0e6c881ce2ec859bd8e53d20e8/
Chekio Profile Link:
https://py.checkio.org/user/jcfernandez/solutions/share/83d63afe87a24e810571c961a5f66dfb/
'''

# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(checkio([0, 1, 2, 3, 4, 5]))

    assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
    assert checkio([6]) == 36, "(6)*6=36"
    assert checkio([]) == 0, "An empty array = 0"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
