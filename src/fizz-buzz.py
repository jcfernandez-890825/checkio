def checkio(number: int) -> str:
    # Modulus operator (x % y); gives the remainder of the left value divided by the right value
    # If a number is divisible by another one then its remainder is zero
    # bool(0) gives False, True for any other value so whe negate this behavior
    if not number % 5 and not number % 3:
        return 'Fizz Buzz'
    elif not number % 5:
        return 'Buzz'
    elif not number % 3:
        return 'Fizz'
    else:
        return str(number)


'''
Chekio Mission Link:
https://py.checkio.org/en/mission/fizz-buzz/
Chekio Solution Link:
https://py.checkio.org/mission/even-last/publications/jcfernandez/python-3/only-one-line-using-reduce-and-islice/share/5cfbca0e6c881ce2ec859bd8e53d20e8/
Chekio Profile Link:
https://py.checkio.org/user/jcfernandez/solutions/share/83d63afe87a24e810571c961a5f66dfb/
'''

if __name__ == '__main__':
    print('Example:')
    print(checkio(15))

    assert checkio(15) == "Fizz Buzz", "15 is divisible by 3 and 5"
    assert checkio(6) == "Fizz", "6 is divisible by 3"
    assert checkio(5) == "Buzz", "5 is divisible by 5"
    assert checkio(7) == "7", "7 is not divisible by 3 or 5"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
