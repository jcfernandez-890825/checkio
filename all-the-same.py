from typing import List, Any


def all_the_same(elements_lst: List[Any]) -> bool:
    return len(set(elements_lst)) <= 1


if __name__ == '__main__':
    print("Example:")
    print(all_the_same([1, 1, 1]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert all_the_same([1, 1, 1]) is True, 'Bad coding'
    assert all_the_same([1, 1, 1, 1, 1]) is False, 'Bad coding'
    assert all_the_same(['a', 'a', 'a']) is True, 'Bad coding'
    assert all_the_same([]) is True, 'Bad coding'
    assert all_the_same([1]) is True, 'Bad coding'
    print("Coding complete? Click 'Check' to earn cool rewards!")

