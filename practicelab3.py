#i need a full calendar for every year with the days of the week for each day of the year. I also need to be able to input a year and have it print out the calendar for that year. I also need to be able to input a month and have it print out the calendar for that month. I also need to be able to input a day and have it print out the day of the week for that day. I also need to be able to input a date and have it print out the day of the week for that date. I also need to be able to input a date and have it print out the day of the week for that date in a different format. I also need to be able to input a date and have it print out the day of the week for that date in a different format with the month name instead of the month number. I also need to be able to input a date and have it print out the day of the week for that date in a different format with the month name instead of the month number and with the year at the end instead of at the beginning. I also need to be able to input a date and have it print out the day of the week for that date in a different format with the month name instead of the month number and with the year at the end instead of at the beginning and with the day of the week at the beginning instead of at the end. I also need to be able to input a date and have it print out the day of the week for that date in a different format with the month name instead of the month number and with the year at the end instead of at the beginning and with the day of the week at
year = int(input("Enter a year: "))
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
month_names = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
print(f"Calendar for the year {year}")
for month in range(len(days_in_month)):
    print(f"\n{month_names[month]} {year}")
    for day in range(1, days_in_month[month] + 1):
        print(f"{month + 1}-{day}-{year}")
        #we need to make february have 29 days if it is a leap year
        if month == 1 and year % 4 == 0:
            print(f"{month + 1}-{day}-{year}")
            #we need to print 29 days for february if it is a leap year
            if day == 28:
                print(f"{month + 1}-{day + 1}-{year} (Leap Year)")
                