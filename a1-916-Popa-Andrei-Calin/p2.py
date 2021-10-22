"""
Determine a calendar date (as year, month, day) starting from two integer numbers
representing the year and the day number inside that year
(e.g. day number 32 is February 1st). Take into account leap years.
Do not use Python's inbuilt date/time functions.
"""

def check_leap():
    """
    checks if it is a leap year and adds an extra day for Feb
    """
    if year%4==0 and year%100==0 and year%400==0:
        l[1]=29

def find_month(day):
    """
    finds the correct date using the given day number and prints it
    """
    i=int(0)
    while 1:
        if day-l[i]<=0:
            break
        else:
            day=day-l[i]
            i=i+1
    print(year, d[i], day)

if __name__ == "__main__":

    print("give year: ", end="")
    year=int(input())
    print("give day: ", end="")
    day=int(input())
    l=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    d={0:"January", 1:"February", 2:"March", 3:"April", 4:"May", 5:"June", 6:"July", 7:"August", 8:"September", 9:"October", 10:"November", 11:"December"}
    check_leap()
    find_month(day)
