def time_converter(time):
    from datetime import datetime
    time = datetime.strptime(time, '%H:%M')
    return time.strftime('%-I:%M {}').format('a.m.' if time.hour < 12 else 'p.m.')


if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:30'))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30') == '12:30 p.m.'
    assert time_converter('09:00') == '9:00 a.m.'
    assert time_converter('23:15') == '11:15 p.m.'
