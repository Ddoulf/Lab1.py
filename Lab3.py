year = int(input("Enter a year: "))
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for month in range(len(days_in_month)):
    for day in range(1, days_in_month[month] + 1):
        print(f"{month + 1}-{day}-{year}")
        #we need to make february have 29 days if it is a leap year
        if month == 1 and year % 4 == 0:
            print(f"{month + 1}-{day}-{year}")
            #we need to print 29 days for february if it is a leap year
            if day == 28:
                print(f"{month + 1}-{day + 1}-{year} (Leap Year)")
                