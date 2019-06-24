def checkio(numbers_array: tuple) -> list:
    return sorted(
        numbers_array,
        key=lambda n: abs(n)
    )


'''
Chekio Mission Link:
https://py.checkio.org/en/mission/absolute-sorting/
Chekio Solution Link:
https://py.checkio.org/mission/verify-anagrams/publications/jcfernandez/python-3/anagrams/share/d7d5432f7efd4f9f31db8f30e481a30c/
Chekio Profile Link:
https://py.checkio.org/user/jcfernandez/solutions/share/83d63afe87a24e810571c961a5f66dfb/
'''

# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(list(checkio((-20, -5, 10, 15))))

    def check_it(array):
        if not isinstance(array, (list, tuple)):
            raise TypeError("The result should be a list or tuple.")
        return list(array)

    assert check_it(checkio((-20, -5, 10, 15))) == [-5, 10, 15, -20], "Example"  # or (-5, 10, 15, -20)
    assert check_it(checkio((1, 2, 3, 0))) == [0, 1, 2, 3], "Positive numbers"
    assert check_it(checkio((-1, -2, -3, 0))) == [0, -1, -2, -3], "Negative numbers"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
