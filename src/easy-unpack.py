def easy_unpack(elements: tuple) -> tuple:
    """
        returns a tuple with 3 elements - first, third and second to the last
    """
    # your code here
    return elements[0], elements[2], elements[-2]


'''
Chekio Mission Link:
https://py.checkio.org/en/mission/easy-unpack/
Chekio Solution Link:
https://py.checkio.org/mission/easy-unpack/publications/jcfernandez/python-3/only-one-line/share/17a285fc9bf1ecb4bbc371e8868b0ad9/
Chekio Profile Link:
https://py.checkio.org/user/jcfernandez/solutions/share/83d63afe87a24e810571c961a5f66dfb/
'''

if __name__ == '__main__':
    print('Examples:')
    print(easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)) == (1, 3, 7)
    assert easy_unpack((1, 1, 1, 1)) == (1, 1, 1)
    assert easy_unpack((6, 3, 7)) == (6, 7, 3)
    print('Done! Go Check!')
