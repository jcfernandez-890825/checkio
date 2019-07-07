from itertools import combinations, chain


def seven_segment(lit_seg, broken_seg):
    # Use this as guide
    # Hexadecimal encodings for displaying the digits 0 to F on https://en.wikipedia.org/wiki/Seven-segment_display
    # Code for getting each string in uppercase
    # from itertools import compress
    # set(''.join(compress('ABCDEFG', list(int(i) for i in bin(int(string, 16))[2:].zfill(7)))) for string in
    #     ('0x7E', '0x30', '0x6D', '0x79', '0x33', '0x5B', '0x5F', '0x70', '0x7F', '0x7B'))
    segments_display_dct = {
        'left':  {'ACDFG', 'ABDEG', 'ABCDFG', 'ABCDEFG', 'ABCDG', 'BCFG', 'BC', 'ABC', 'ABCDEF', 'ACDEFG'},
        'right': {'bcfg', 'acdfg', 'abcdfg', 'abdeg', 'bc', 'abcdefg', 'abcdg', 'acdefg', 'abc', 'abcdef'}
    }
    broken_seg_dct = {'left': '', 'right': ''}
    lit_seg_dct = {'left': '', 'right': ''}

    for segment in lit_seg:
        # left display segments are in uppercase and right ones in lowercase
        lit_seg_dct['left' if segment.isupper() else 'right'] += segment

    for segment in broken_seg:
        # left display segments are in uppercase and right ones in lowercase
        broken_seg_dct['left' if segment.isupper() else 'right'] += segment

    total_possible_numbers = 1
    for side in ('left', 'right'):
        # Get broken segments of one side
        broken_segments = broken_seg_dct[side]
        # By calculating the cartesian product length of all possible numbers displayed on each display
        # We get the total possible numbers displayed on the device
        total_possible_numbers *= len(
            # Check how many segment combinations are actually numbers on one display
            set(
                map(
                    lambda comb: ''.join(sorted(lit_seg_dct[side] + ''.join(comb))),
                    # Get all broken segments possible combinations on one display
                    chain.from_iterable(
                        combinations(broken_segments, n) for n in range(len(broken_segments) + 1)
                    )
                )
            ).intersection(segments_display_dct[side])
        )

    # Return the total number that the device may be displaying
    return total_possible_numbers


'''
Chekio Mission Link:
https://py.checkio.org/en/mission/seven-segment/
Chekio Solution Link:
https://py.checkio.org/mission/seven-segment/publications/jcfernandez/python-3/using-combinations-and-chain-from-itertools-along-with-dictionaries/share/c2aa36d94a75fdcfd68d3bd313ae18e7/
Chekio Profile Link:
https://py.checkio.org/user/jcfernandez/solutions/share/83d63afe87a24e810571c961a5f66dfb/
'''

if __name__ == '__main__':
    assert seven_segment({'B', 'C', 'b', 'c'}, {'A'}) == 2, '11, 71'
    assert seven_segment({'B', 'C', 'a', 'f', 'g', 'c', 'd'}, {'A', 'G', 'D', 'e'}) == 6, '15, 16, 35, 36, 75, 76'
    assert seven_segment({'B', 'C', 'a', 'f', 'g', 'c', 'd'}, {'A', 'G', 'D', 'F', 'b', 'e'}) == 20, '15...98'
    print('"Run" is good. How is "Check"?')
