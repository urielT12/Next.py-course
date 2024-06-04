import datetime


def gen_secs():
    """a generator that produce all seconds 0-60"""
    for i in range(60):
        yield i

def gen_minutes():
    """a generator that produce all minutes 0-60"""
    for i in range(60):
        yield i

def gen_hours():
    """a generator that produce all hours 0-24"""
    for i in range(24):
        yield i

def gen_time():
    """a generator that produce all possible time combination in a day"""
    for hour in gen_hours():
        for minute in gen_minutes():
            for second in gen_secs():
                yield f"{hour:02}:{minute:02}:{second:02}"

def gen_years(start=2024):
    """a generator that produce all years number - from input year (or 2024) to now"""
    current_year = datetime.datetime.now().year
    for i in range(start, current_year + 1):
        yield i

def gen_months():
    """a generator that produce all month numbers - 1-12"""
    for i in range(1, 13):
        yield i

def gen_days(month, leap_year=True):
    """a generator that produce all days number in a month based on - is it a leap year and what month is it"""
    thirty_one = [1, 3, 5, 7, 8, 10, 12]
    thirty = [4, 6, 9, 11]
    if month in thirty_one:
        for i in range(1, 32):
            yield i
    elif month in thirty:
        for i in range(1, 31):
            yield i
    elif leap_year:
        for i in range(1, 30):
            yield i
    else:
        for i in range(1, 29):
            yield i

def gen_date():
    """a generator that produce all possible time and date combinations from a specific year"""
    for year in gen_years(2019):
        leap = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
        for month in gen_months():
            for day in gen_days(month, leap):
                date = f"{day:02}/{month:02}/{year}"
                for t in gen_time():
                    yield f"{date} {t}"

def main():
    """"main function that prints the date every 1,000,000 iterations"""
    date_generator = gen_date()
    count = 0
    while True:
        try:

            next_combination = next(date_generator)

            if count == 1000000:
                print(next_combination)
                count = 0
            count += 1
        except StopIteration:
            break

if __name__ == '__main__':
    main()