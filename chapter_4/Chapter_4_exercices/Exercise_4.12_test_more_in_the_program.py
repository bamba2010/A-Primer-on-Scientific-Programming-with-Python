import calendar,sys
try:
    year= float(sys.argv[1])
    month= float(sys.argv[2])
    day = float(sys.argv[3])
except IndexError:
    print("You must supply year,month and day to the command line")
    sys.exit(1)
if len(year)<4 and len(month)!=1 and len(day)!=1:
    raise ValueError("the year must be four digits")
    sys.exit(1)
c=calendar.weekday(year, month, day)
print(c)
