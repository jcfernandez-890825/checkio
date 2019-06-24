def checkio(*args):
    return max(args) - min(args) if len(args) > 0 else 0


'''
Chekio Mission Link:
https://py.checkio.org/en/mission/sort-array-by-element-frequency/
Chekio Solution Link:
https://py.checkio.org/mission/most-numbers/publications/jcfernandez/python-3/only-one-line/share/52f65f203f1acf99d7647fc1b0c52dc8/
Chekio Profile Link:
https://py.checkio.org/user/jcfernandez/solutions/share/83d63afe87a24e810571c961a5f66dfb/
'''

# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    def almost_equal(checked, correct, significant_digits):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision


    print('Example:')
    print(checkio(1, 2, 3))

    assert almost_equal(checkio(1, 2, 3), 2, 3), "3-1=2"
    assert almost_equal(checkio(5, -5), 10, 3), "5-(-5)=10"
    assert almost_equal(checkio(10.2, -2.2, 0, 1.1, 0.5), 12.4, 3), "10.2-(-2.2)=12.4"
    assert almost_equal(checkio(), 0, 3), "Empty"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")