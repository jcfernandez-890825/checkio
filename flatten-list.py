def flat_list(array: list) -> list:
    from itertools import chain

    return list(
        chain(
            *(flat_list(i) if type(i) is list else (i,) for i in array)
        )
    )


'''
Chekio Mission Link:
https://py.checkio.org/en/mission/flatten-list/
Chekio Solution Link:
https://py.checkio.org/mission/flatten-list/publications/jcfernandez/python-3/only-one-line/share/e6a4e1b0c5345946e932e6f2844656b5/
Chekio Profile Link:
https://py.checkio.org/user/jcfernandez/solutions/share/83d63afe87a24e810571c961a5f66dfb/
'''

if __name__ == '__main__':
    print(flat_list([1, 2, 3]))
    print(flat_list([1, [2, 2, 2], 4]))
    print(flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]))
    print(flat_list([-1, [1, [-2], 1], -1]))

    assert flat_list([1, 2, 3]) == [1, 2, 3], "First"
    assert flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4], "Second"
    assert flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [2, 4, 5, 6, 6, 6, 6, 6, 7], "Third"
    assert flat_list([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1], "Four"
    print('Done! Check it')
