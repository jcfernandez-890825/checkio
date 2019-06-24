def checkio(data: list) -> list:
    # Return all elements whose that repeat more than once in the list
    return [item for item in data if data.count(item) > 1]


'''
Chekio Mission Link:
https://py.checkio.org/en/mission/non-unique-elements/
Chekio Solution Link:
https://py.checkio.org/mission/common-words/publications/jcfernandez/python-3/only-one-line/share/414d7f9ed14f80e259996bdd77e346ee/
Chekio Profile Link:
https://py.checkio.org/mission/non-unique-elements/publications/jcfernandez/python-3/only-one-line/share/b058fd3dcc05ce3e29153c703ef0a2d8/
'''

if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3], "1st example"
    assert list(checkio([1, 2, 3, 4, 5])) == [], "2nd example"
    assert list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5], "3rd example"
    assert list(checkio([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9], "4th example"
    print("It is all good. Let's check it now")
