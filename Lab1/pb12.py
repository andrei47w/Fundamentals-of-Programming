"""
Determine the age of a person, in number of days.
Take into account leap years, as well as the date of birth and current date
(year, month, day).
Do not use Python's inbuilt date/time functions.
"""

def days_of_month(m):
    if m==4 or m==6 or m==9 or m==10:
        return 30
    if m==2:
        return 28
    return 31

def is_leap(y):
    """
    checks if it is a leap year
    """
    if y%400==0:
        return True
    return False

def nr_days(d, m, y):
    """
    calculates the number of days passed
    """
    days=int(d)
    if m>2 and is_leap(y):
        days+=1
    for month in range(1, m):
        days+=days_of_month(m)
    return days

def age_in_days(d1, m1, y1, d2, m2, y2):
    """
    calculates the age of a person in number of days
    """
    age=int(0)
    for year in range(y1, y2):
        if is_leap(year):
            age+=1
        age+=365
    return age-nr_days(d1, m1, y1)+nr_days(d2, m2, y2)

if __name__ == '__main__':
    print("give birth date: ", end="")
    d1,m1,y1=int(input()), int(input()), int(input())
    print("give current date: ", end="")
    d2,m2,y2=int(input()), int(input()), int(input())
    print("age in number of days is:", age_in_days(d1, m1, y1, d2, m2, y2), end="")
