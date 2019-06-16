def non_repeat(line):
    # Here we will store a list of non-repeating character sequences
    non_repeat_lst = []
    # Here we will store the non-repeating characters sequence
    ret_str = ''
    # Loop over each character
    for c in line:
        # If the character is not in the non-repeating sequence
        if c not in ret_str:
            ret_str += c        # Add it to the sequence
        else:
            # Add the current sequence to the list of non-repeating characters sequences
            non_repeat_lst.append(ret_str)
            # Create a new sequence of non-repeating characters
            # Starting from the next character after the repeating one
            # Up to the repeating character
            ret_str = ret_str[ret_str.find(c) + 1:] + c

    # Add the last non-repeating character sequence
    non_repeat_lst.append(ret_str)
    # Return the non-repeating characters sequence with largest length
    return max(non_repeat_lst, key=len, default='')


'''
Chekio Mission Link:
https://py.checkio.org/en/mission/long-non-repeat/
Chekio Solution Link:
https://py.checkio.org/mission/long-non-repeat/publications/jcfernandez/python-3/one-loop-very-fast/share/5444a2e6bd9b604fa03f43d89175efd3/
Chekio Profile Link:
https://py.checkio.org/user/jcfernandez/solutions/share/83d63afe87a24e810571c961a5f66dfb/
'''

if __name__ == '__main__':
    from timeit import default_timer as time

    start = time()

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert non_repeat('aaaaa') == 'a', "First"
    assert non_repeat('abdjwawk') == 'abdjw', "Second"
    assert non_repeat('abcabcffab') == 'abcf', "Third"
    assert non_repeat('fghfrtyfgh') == 'ghfrty', "Fourth"
    assert non_repeat('') == '', "Fifth"
    print('"Run" is good. How is "Check"?')

    end = time()

    print(end - start)
