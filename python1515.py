# i need to make a calendar that prints out the days of the month for a given year, and also accounts for leap years. I will use a list to store the number of days in each month, and then use nested loops to iterate through each month and day, printing them out in the format "month-day-year". I will also check if the year is a leap year and adjust February's days accordingly.
starting_year = int(input("Enter a year: "))
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days_in_month_leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days_in_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
#i need the code to tell me for example monday is on the 1st of january, and then tuesday is on the 2nd of january, and so on. I will use a variable to keep track of the current day of the week, and increment it as I iterate through the days of the month. I will also use the modulo operator to wrap around to the beginning of the week when I reach the end.
day_of_week = 0  # January 1st is a Sunday
starting_year = 1  # Starting year for the calendar
print("Calendar for the year", starting_year)
for month in range(len(days_in_month)):
    if starting_year % 4 == 0 and month == 1:  # Check for leap year in February
        days = days_in_month_leap[month]
    else:
        days = days_in_month[month]
    
    print(f"\nMonth: {month + 1}")
    for day in range(1, days + 1):
        print(f"{days_in_week[day_of_week]} - {month + 1}-{day}-{starting_year}")
        day_of_week = (day_of_week + 1) % 7  # Increment day of the week and wrap around after Saturday
#user input for the year
starting_year = int(input("Enter a year: "))
