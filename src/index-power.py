def index_power(array: list, n: int) -> int:
    """
        Find Nth power of the element with index N.
    """
    # If N is less than length of array  then
    # return N-th power of the N-th element
    # else return -1
    return array[n] ** n if n < len(array) else -1


'''
Chekio Mission Link:
https://py.checkio.org/en/mission/index-power/
Chekio Solution Link:
https://py.checkio.org/mission/index-power/publications/jcfernandez/python-3/only-one-line/share/7a29e95844a0fee962ef4a8008b239f8/
Chekio Profile Link:
https://py.checkio.org/user/jcfernandez/solutions/share/83d63afe87a24e810571c961a5f66dfb/
'''

if __name__ == '__main__':
    print('Example:')
    print(index_power([1, 2, 3, 4], 2))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert index_power([1, 2, 3, 4], 2) == 9, "Square"
    assert index_power([1, 3, 10, 100], 3) == 1000000, "Cube"
    assert index_power([0, 1], 0) == 1, "Zero power"
    assert index_power([1, 2], 3) == -1, "IndexError"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
