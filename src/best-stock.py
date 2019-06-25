def best_stock(data):
    # Sort the stock values
    return sorted(
        # Iterate over each key, value
        data.items(),
        # Sort by value
        key=lambda i: i[1],
        # Sort from most costly to less
        reverse=True
        # If the dictionary is empty then return 0.0 else return the key
    )[0][0] if len(data) > 0 else 0.0


'''
Chekio Mission Link:
https://py.checkio.org/en/mission/best-stock/
Chekio Solution Link:
https://py.checkio.org/mission/best-stock/publications/jcfernandez/python-3/only-one-line-using-sorted/share/840f9ba6174567394dc8b1a7f243ad04/
Chekio Profile Link:
https://py.checkio.org/user/jcfernandez/solutions/share/83d63afe87a24e810571c961a5f66dfb/
'''

if __name__ == '__main__':
    print("Example:")
    print(best_stock({
        'CAC': 10.0,
        'ATX': 390.2,
        'WIG': 1.2
    }))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert best_stock({
        'CAC': 10.0,
        'ATX': 390.2,
        'WIG': 1.2
    }) == 'ATX', "First"
    assert best_stock({
        'CAC': 91.1,
        'ATX': 1.01,
        'TASI': 120.9
    }) == 'TASI', "Second"
    print("Coding complete? Click 'Check' to earn cool rewards!")
