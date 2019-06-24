def checkio(string):
    from string import ascii_lowercase

    # Return the letters with the most counting
    return max(
        # This creates a tuple of (letter, letter count)
        zip(
            ascii_lowercase,
            map(  # This mapping will count how many times a letter repeats on string variable
                lambda s: string.lower().count(s),
                ascii_lowercase
            )
        ),
        key=lambda t: t[1]  # We are telling the max function to use the letter counting for finding the max value
    )[0]


'''
Chekio Mission Link:
https://py.checkio.org/en/mission/most-wanted-letter/

Chekio Solution Link:
https://py.checkio.org/mission/most-wanted-letter/publications/jcfernandez/python-3/only-one-line/share/7fe6b109d0ccf79f4ddaa28339e46d9f/

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
