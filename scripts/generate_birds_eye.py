# import standard packages
import calendar
import os
import argparse

# import custom packages
from en_calendar import en_months, en_days
from fr_calendar import fr_months, fr_days

# add arguments
parser = argparse.ArgumentParser()
parser.add_argument("month", type=int)
parser.add_argument("--year", default=2018)
parser.add_argument("--markdown", default=False, action="store_true")
parser.add_argument("--whom", default=None)
parser.add_argument("--language", default="en")
parser.add_argument("--save", default=None)  # path name to save

# parse arguments
args = parser.parse_args()
year = args.year
month = args.month
markdown = args.markdown
whom = args.whom
language = args.language
save = args.save

# initialize the calendar
cal = calendar.TextCalendar()
all_days = cal.monthdayscalendar(year, month)

# specify days/months by language
if language == "fr":
    days = fr_days
    months = fr_months
else:
    days = en_days
    months = fr_months

# create table formatting
if markdown == False:
    string_to_print = "+----+" + 70 * "-" + "+"
else:

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
