import datetime


def gen_secs():
    for i in range(60):
        yield i

def gen_minutes():
    for i in range(60):
        yield i

def gen_hours():
    for i in range(24):
        yield i

def gen_time():
    for hour in gen_hours():
        for minute in gen_minutes():
            for second in gen_secs():
                yield f"{hour:02}:{minute:02}:{second:02}"

def gen_years(start=2024):
    current_year = datetime.datetime.now().year
    for i in range(start, current_year + 1):
        yield i

def gen_months():
    for i in range(1, 13):
        yield i

def gen_days(month, leap_year=True):
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
    for year in gen_years(2019):
        leap = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
        for month in gen_months():
            for day in gen_days(month, leap):
                date = f"{day:02}/{month:02}/{year}"
                for t in gen_time():
                    yield f"{date} {t}"


date = gen_date()
count = 0
for i in date:
    if count == 1000000:
        print(i)
        count = 0
    count += 1

