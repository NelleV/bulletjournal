import calendar
import argparse
from nelle import nelle_specific_stuff
from alex import alex_specific_stuff

# initialize the parser
parser = argparse.ArgumentParser()

# add parser arguments
parser.add_argument("month", type=int)
parser.add_argument("--year", default=2018)
parser.add_argument("--markdown", default=False, action="store_true")
parser.add_argument("--whom", default=None)
args = parser.parse_args()

# add arguments to namespace
year = args.year
month = args.month
markdown = args.markdown
whom = args.whom

# yell at us if we don't provide a valid name
if whom is not None and whom not in ["alex", "nelle"]:
    raise ValueError("I do not know who that person is")

# initialize the calendar
cal = calendar.TextCalendar()
all_days = cal.monthdayscalendar(year, month)

# name the days of the week
days = ["Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"]

# provide numbers for months of the year
months = {1: "January",
          2: "February",
          3: "March",
          4: "April",
          5: "May",
          6: "June",
          7: "July",
          8: "August",
          9: "September",
          10: "October",
          11: "November",
          12: "December"}

# cycle through each day
for dates in all_days:
    for day, date in zip(days, dates):
        if date == 0:
            continue

        # format the day
        text = "{day}, {month} {date}".format(
            **{"day": day, "month": months[month], "date": date})

        # print the day header by our preferred format
        if markdown:
            print("#", text)
        else:
            print(text)
            print("-" * len(text))
        print()

        # Here, let's add weekly specific items
        if whom == "nelle":
            nelle_specific_stuff(day, date, month, year)
        elif whom == "alex":
            alex_specific_stuff(day, date, month, year)
        print()
