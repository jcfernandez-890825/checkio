def long_repeat(line):
    max_len = current_len = 1
    for i in range(1, len(line)):
        if line[i-1] == line[i]:
            current_len += 1
        else:
            if max_len < current_len:
                max_len = current_len
            current_len = 1

    return max(max_len, current_len) if line else 0


if __name__ == '__main__':
    from timeit import default_timer as time

    start = time()

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    print('"Run" is good. How is "Check"?')

    end = time()

    print(end - start)
