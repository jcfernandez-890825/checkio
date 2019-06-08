def frequency_sort(items):
    r = [
        (items.count(i), -1 * items.index(i), n, i)
        for n, i in enumerate(items)
    ]

    r.sort(reverse=True)

    r = [
        i for count, index, n, i in r
    ]

    # your code here
    return sorted(items, key=lambda i: (items.count(i), -1 * items.index(i)), reverse=True)


if __name__ == '__main__':
    # item_lst = [4, 6, 2, 2, 2, 6, 4, 4, 4]
    item_lst = [4, 6, 2, 2, 6, 4, 4, 4]
    # item_lst = ['bob', 'bob', 'carl', 'alex', 'bob']
    # item_lst = [17, 99, 42]
    # item_lst = []
    # item_lst = [1]
    # item_lst.sort(key=lambda i: item_lst.count(i), reverse=True)

    print(item_lst)
    print(frequency_sort(item_lst))
