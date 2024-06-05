# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar

days = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]

# input_date = map(int, input().split(" "))
# mm, dd, yyyy = input_date
mm, dd, yyyy = 8, 5, 2999
day= calendar.weekday(yyyy, mm, dd)
print(day)
print(days[day])
print(calendar.day_name[day].upper())