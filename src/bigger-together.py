def bigger_together(ints):
    """
        Returns difference between the largest and smallest values
        that can be obtained by concatenating the integers together.
    """
    from functools import cmp_to_key

    # For finding the lowest number possible with the listed number we will make use of the old sorting technique
    # cmp_to_key is function that compares two arguments by a using math and returns
    # less than for negative numbers
    # greater than for positive numbers
    # equals for zero
    # using this feature we concatenate the string representation of two numbers on the list and subtract them with
    # the mirror concatenation
    lowest = sorted(
        # Transform the numbers into their string representation
        map(
            str,
            ints
        ),
        key=cmp_to_key(lambda x, y: int(x + y) - int(y + x))
    )

    # When you use reversed on a list the sorting is respected, similar to sorted(iter, reverse=True)
    # On strings, reversed do a mirror, which is not what we want, that's why we first do the reverse before
    # transforming the string list into a single string
    return int(''.join(reversed(lowest))) - int(''.join(lowest))


'''
Chekio Mission Link:
https://py.checkio.org/en/mission/bigger-together/
Chekio Solution Link:

Chekio Profile Link:
https://py.checkio.org/user/jcfernandez/solutions/share/83d63afe87a24e810571c961a5f66dfb/
'''

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    # assert bigger_together([1, 2, 3, 4]) == 3087, "4321 - 1234"
    # assert bigger_together([1, 2, 3, 4, 11, 12]) == 32099877, "43212111 - 11112234"
    # assert bigger_together([0, 1]) == 9, "10 - 01"
    # assert bigger_together([100]) == 0, "100 - 100"
    assert bigger_together([3, 12, 22, 32]) == 2099889, '3322212 - 1222323 = 2099889'
    print('Done! I feel like you good enough to click Check')
