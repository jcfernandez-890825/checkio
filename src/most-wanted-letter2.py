def checkio(string):
    from collections import Counter
    from string import ascii_letters

    string = sorted(
        sorted(
            # Count how many times does a letter repeats
            Counter(
                # Avoid counting anything but letters
                char for char in string.lower() if char in ascii_letters
            ).most_common(),
            # Counter(...).most_common() returns a list of tuples containing each letter and its counting
            # We 1st sort the list of tuples alphabetically
            key=lambda char_count_tpl: char_count_tpl[0]
        ),
        # Then we re-sort by letter counting, from higher to lower
        key=lambda char_count_tpl: char_count_tpl[1], reverse=True
    )
    # Get the letter with the most counting
    # We return only the letter
    return string[0][0] if string else ''


'''
Chekio Mission Link:
https://py.checkio.org/en/mission/most-wanted-letter/

Chekio Solution Link:
https://py.checkio.org/mission/most-wanted-letter/publications/jcfernandez/python-3/using-counter-from-collections-and-sorted-less-iterations/share/dd3dafd3b2c54464aca64d4493f902f9/

Chekio Profile Link:
https://py.checkio.org/user/jcfernandez/solutions/share/83d63afe87a24e810571c961a5f66dfb/
'''


if __name__ == '__main__':

    print("Example:")
    print(checkio("Hello World!"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")