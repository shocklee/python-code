"""weekdayCalendar.

    Compute the day of the week for any calendar day.
    Argument contains the date as three integers, ccyy, mm, and dd.
    Results will be looked up in the day of week table.

    return string
    
"""

from datetime import date

def calcWeekday(aYear, aMonth, aDay):
    return dayOfWeek(date(aYear, aMonth, aDay).weekday())

def dayOfWeek(aNumber):         #Day of week table
    aDay = ('MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN')
    return (aDay[aNumber])

if __name__ == "__main__":      #Test run results
    #If the calculations match, print True otherwise print False.
    testData = ((1982, 4, 24, 'SAT'),
                (1783, 9, 18, 'THU'),
                (2000, 1, 1, 'SAT'),
                (2054, 6, 19, 'FRI'))
    valid = True
    for x in testData:
      valid = valid and calcWeekday(x[0], x[1], x[2]) == x[3]
    print valid
