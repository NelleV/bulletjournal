import calendar
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("month", type=int)
parser.add_argument("--year", default=2018)

args = parser.parse_args()
year = args.year
month = args.month

cal = calendar.TextCalendar()
all_days = cal.monthdayscalendar(year, month)
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

days = ["Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"]

string_to_print = "+----+" + 70 * "-" + "+"

for dates in all_days:
    for day, date in zip(days, dates):
        if date == 0:
            continue

        # format the day
        print(string_to_print)
        text = "|{date} {day}".format(
            **{"day": day[0], "date": date})
        if len(text) == 4:
            text = text + " |" + 70 * " " + "|"
        else:
            text = text + "|" + 70 * " " + "|"

        print(text)
print(string_to_print)
