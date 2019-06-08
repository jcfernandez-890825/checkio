def flat_list(array: list) -> list:
    from itertools import chain

    return list(
        chain(
            *(flat_list(i) if type(i) is list else (i,) for i in array)
        )
    )


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
