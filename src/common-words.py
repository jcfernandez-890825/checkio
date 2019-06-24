def checkio(first, second):
    # Return a large string by concatenating the sorted string set using commas
    return ','.join(
        # Sort the resulting string set in alphabetical order
        sorted(
            # Get the common elements of both string sets unsorted
            set(first.split(',')).intersection(set(second.split(',')))
        )
    )


'''
Chekio Mission Link:
https://py.checkio.org/en/mission/common-words/
Chekio Solution Link:
https://py.checkio.org/mission/common-words/publications/jcfernandez/python-3/only-one-line/share/414d7f9ed14f80e259996bdd77e346ee/
Chekio Profile Link:
https://py.checkio.org/user/jcfernandez/solutions/share/83d63afe87a24e810571c961a5f66dfb/
'''

# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("hello,world", "hello,earth") == "hello", "Hello"
    assert checkio("one,two,three", "four,five,six") == "", "Too different"
    assert checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two", "1 2 3"
