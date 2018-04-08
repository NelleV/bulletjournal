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
parser.add_argument("--language", default="en")
args = parser.parse_args()

# add arguments to namespace
year = args.year
month = args.month
markdown = args.markdown
whom = args.whom
language = args.language

# yell at us if we don't provide a valid name
if whom is not None and whom not in ["alex", "nelle"]:
    raise ValueError("I do not know who that person is")

# initialize the calendar
cal = calendar.TextCalendar()
all_days = cal.monthdayscalendar(year, month)

# name the days of the week
en_days = ["Monday",
           "Tuesday",
           "Wednesday",
           "Thursday",
           "Friday",
           "Saturday",
           "Sunday"]
fr_days = ["lundi",
           "mardi",
           "mercredi",
           "jeudi",
           "vendredi",
           "samedi",
           "dimanche"]

# provide numbers for months of the year
en_months = {1: "January",
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
fr_months = {1: "janvier",
             2: "février",
             3: "mars",
             4: "avril",
             5: "mai",
             6: "juin",
             7: "juillet",
             8: "août",
             9: "septembre",
             10: "octobre",
             11: "novembre",
             12: "décembre"}

# initialize the calendar string
cal_string = ""

# cycle through each day
for dates in all_days:

    # account for language preference
    if language == "fr":
            days = fr_days
            months = fr_months
    else:
        days = en_days
        months = en_months

    # print the calendar
    for day, date in zip(days, dates):
        if date == 0:
            continue

        # format the day
        text = "{day}, {month} {date}".format(
            **{"day": day, "month": months[month], "date": date})

        # print the day header by our preferred format
        if markdown:
            cal_string = cal_string + "#" + text
        else:
            cal_string = cal_string + text + '\n'
            cal_string = cal_string + "-" * len(text)
        cal_string = cal_string + "\n"

        # Here, let's add weekly specific items
        if whom == "nelle":
            nelle_specific_stuff(day, date, month, year, language, cal_string)
        elif whom == "alex":
            alex_specific_stuff(day, date, month, year, language, cal_string)
        cal_string = cal_string + '\n'
