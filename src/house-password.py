def checkio(data):
    return all(  # For each checking
        any(  # At least one character must comply with the follow
            map(is_func, data)  # Either lower letter, upper letter or digit
        )
        for is_func in (str.isdigit, str.isupper, str.islower)
    ) and len(data) >= 10  # Also the password length must be 10 or more


'''
Chekio Mission Link:
https://py.checkio.org/en/mission/house-password/
Chekio Solution Link:
https://py.checkio.org/mission/house-password/publications/jcfernandez/python-3/only-one-line/share/931ffa90236fa844f8be4925865ac3bc/
Chekio Profile Link:
https://py.checkio.org/user/jcfernandez/solutions/share/83d63afe87a24e810571c961a5f66dfb/
'''

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') is False, "1st example"
    assert checkio('bAse730onE4') is True, "2nd example"
    assert checkio('asasasasasasasaas') is False, "3rd example"
    assert checkio('QWERTYqwerty') is False, "4th example"
    assert checkio('123456123456') is False, "5th example"
    assert checkio('QwErTy911poqqqq') is True, "6th example"
