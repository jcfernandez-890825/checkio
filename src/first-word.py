def first_word(text: str) -> str:
    from itertools import takewhile, dropwhile

    # Return the 1st word
    return ''.join(
        # Remove everything else after a space or punctuation
        takewhile(
            lambda c: c not in ',. ',
            # Remove spaces and punctuation from the beginning
            dropwhile(lambda c: c in ',. ', text)
        )
    )


'''
Chekio Mission Link:
https://py.checkio.org/en/mission/first-word/
Chekio Solution Link:
https://py.checkio.org/mission/first-word/publications/jcfernandez/python-3/first/share/c503b2344054be9893b38d128b3cbbb4/
Chekio Profile Link:
https://py.checkio.org/user/jcfernandez/solutions/share/83d63afe87a24e810571c961a5f66dfb/
'''

if __name__ == '__main__':
    print("Example:")
    print(first_word('.a' * 100000000 + "Hello world"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert first_word("Hello world") == "Hello"
    assert first_word(" a word ") == "a"
    assert first_word("don't touch it") == "don't"
    assert first_word("greetings, friends") == "greetings"
    assert first_word("... and so on ...") == "and"
    assert first_word("hi") == "hi"
    assert first_word("Hello.World") == "Hello"
    print("Coding complete? Click 'Check' to earn cool rewards!")