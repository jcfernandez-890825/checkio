def bigger_price(limit: int, data: list) -> list:
    """
        TOP most expensive goods
    """
    return sorted(
        data,
        reverse=True,               # In descending order
        key=lambda i: i['price']    # Short data by price
    )[:limit]                       # Only return as much data as limit


'''
Chekio Mission Link:
https://py.checkio.org/en/mission/bigger-price/
Chekio Solution Link:
https://py.checkio.org/mission/bigger-price/publications/jcfernandez/python-3/only-one-line/share/389ad71af43401bc76983e2eff896628/
Chekio Profile Link:
https://py.checkio.org/user/jcfernandez/solutions/share/83d63afe87a24e810571c961a5f66dfb/
'''

if __name__ == '__main__':
    from pprint import pprint
    print('Example:')
    pprint(bigger_price(2, [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
    ]))

    # These "asserts" using for self-checking and not for auto-testing
    assert bigger_price(2, [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
    ]) == [
        {"name": "wine", "price": 138},
        {"name": "bread", "price": 100}
    ], "First"

    assert bigger_price(1, [
        {"name": "pen", "price": 5},
        {"name": "whiteboard", "price": 170}
    ]) == [{"name": "whiteboard", "price": 170}], "Second"

    print('Done! Looks like it is fine. Go and check it')
