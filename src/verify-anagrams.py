def verify_anagrams(first_word, second_word):
    # Remove spaces and then make upper characters into lower
    first_word = first_word.replace(' ', '').lower()
    second_word = second_word.replace(' ', '').lower()

    # Return true if both phrases have same length and same letters
    return len(first_word) == len(second_word) and not any(
        map(
            lambda i: first_word.count(i) != second_word.count(i),
            first_word
        )
    )


'''
Chekio Mission Link:
https://py.checkio.org/en/mission/verify-anagrams/
Chekio Solution Link:
https://py.checkio.org/mission/verify-anagrams/publications/jcfernandez/python-3/anagrams/share/d7d5432f7efd4f9f31db8f30e481a30c/
Chekio Profile Link:
https://py.checkio.org/user/jcfernandez/solutions/share/83d63afe87a24e810571c961a5f66dfb/
'''

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    # assert isinstance(verify_anagrams("a", 'z'), bool), "Boolean!"
    assert verify_anagrams("Programming", "Gram Ring Mop") == True, "Gram of code"
    assert verify_anagrams("Hello", "Ole Oh") == False, "Hello! Ole Oh!"
    assert verify_anagrams("Kyoto", "Tokyo") == True, "The global warming crisis of 3002"

