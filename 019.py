#!/usr/bin/env python


def isLeapYear(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0


def getDaysOfMonth(year, month):
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if isLeapYear(year):
        days[1] = 29

    return days[month - 1]


def countMonthsWithFirstDaySunday():
    days = 1
    sundays = 0
    for y in range(1901, 2001):
        for m in range(1, 13):
            # If the last day of previous month was saturday. We know that the
            # first day of this month is sunday.
            if days == 6:
                sundays += 1

            days += getDaysOfMonth(y, m)
            days %= 7

    return(sundays)


print(countMonthsWithFirstDaySunday())
