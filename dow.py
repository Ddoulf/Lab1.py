def isLeapYear(year):
    pass


def getDayOfTheWeek(year, month, day):
    #step 1
    last_two_digits = year % 100
    how_many_twelves = last_two_digits // 12
    print(last_two_digits)
    print(how_many_twelves)

    #step 2
    remainder = last_two_digits - how_many_twelves * 12        #or remainder = last_two_digits % 12
    print(remainder)

    #step 3
    how_many_fours = remainder // 4
    print(how_many_fours)

    #step 4
    print(day)

    #step 5
    January = int("1")
    February = int("2")
    March = int("3")
    April = int("4")
    May = int("5")
    June = int("6")
    July = int("7")
    August = int("8")
    September = int("9")
    October = int("10")
    November = int("11")
    December = int("12")

    #step 6
    Weeks_in_year = January + February + March + April + May + June + July + August + September + October + November + December // 7
    print(Weeks_in_year)


def makeCalendar():
    pass