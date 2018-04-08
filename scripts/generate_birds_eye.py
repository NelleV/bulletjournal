# import standard packages
import calendar
import os
import argparse

# import custom packages
from en_calendar import en_months, en_days
from fr_calendar import fr_months, fr_days
from nelle import nelle_birdseye_specific
from alex import alex_birdseye_specific

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

# yell at us if we don't provide a valid name
if whom is not None and whom not in ["alex", "nelle"]:
    raise ValueError("I do not know who that person is")

# initialize the calendar
cal = calendar.TextCalendar()
all_days = cal.monthdayscalendar(year, month)
calendar_string = ""

# specify days/months by language
if language == "fr":
    days = fr_days
    months = fr_months
else:
    days = en_days
    months = en_months

# create table formatting
header_string = " ---- " + 70 * "-" + " "

# cycle through individual daily entries
for dates in all_days:
    for day, date in zip(days, dates):
        if date == 0:
            continue

        # format the day
        calendar_string = calendar_string + header_string
        text = " {date} {day}".format(
            **{"day": day[0], "date": date})
        if len(text) == 4:
            text = text + " " + 70 * " " + " "
        else:
            text = text + " " + 70 * " " + " "

        calendar_string = calendar_string + text

# print or save as desired
if save is None:
    print(calendar_string)
else:
    with open(save, "w") as calendar_file:
        calendar_file.write(calendar_string)
