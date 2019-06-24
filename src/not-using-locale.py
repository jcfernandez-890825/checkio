def time_converter(time):
    from datetime import datetime

    time = datetime.strptime(time, '%H:%M')
    return time.strftime('%-I:%M {}').format('a.m.' if time.hour < 12 else 'p.m.')


'''
Chekio Mission Link:
https://py.checkio.org/en/mission/not-using-locale/
Chekio Solution Link:
https://py.checkio.org/mission/time-converter-24h-to-12h/publications/jcfernandez/python-3/not-using-locale/
Chekio Profile Link:
https://py.checkio.org/user/jcfernandez/solutions/share/83d63afe87a24e810571c961a5f66dfb/
'''

if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:30'))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30') == '12:30 p.m.'
    assert time_converter('09:00') == '9:00 a.m.'
    assert time_converter('23:15') == '11:15 p.m.'
