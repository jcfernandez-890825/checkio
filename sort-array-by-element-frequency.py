def frequency_sort(items):
    # your code here
    return sorted(items, key=lambda i: (items.count(i), -1 * items.index(i)), reverse=True)

'''
Chekio Mission Link:
https://py.checkio.org/en/mission/sort-array-by-element-frequency/

Chekio Solution Link:
https://py.checkio.org/mission/sort-array-by-element-frequency/publications/jcfernandez/python-3/only-one-line/share/b925502bb310020ce2dd7314ec038769/

Chekio Profile Link:
https://py.checkio.org/user/jcfernandez/solutions/
'''

if __name__ == '__main__':
    print("Example:")
    print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
    assert list(frequency_sort([4, 6, 2, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 2, 2, 2, 6, 6]
    assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex']
    assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    assert list(frequency_sort([])) == []
    assert list(frequency_sort([1])) == [1]
    print("Coding complete? Click 'Check' to earn cool rewards!")
