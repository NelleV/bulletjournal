# import standard libraries
import calendar
import argparse

# import general packages

# import specific people's info
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
parser.add_argument("--save", default=None)  # path name to save
args = parser.parse_args()

# add arguments to namespace
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

# initialize the calendar string
cal_string = ""

# account for language preference
if language == "fr":
        days = fr_days
        months = fr_months
else:
    days = en_days
    months = en_months

# cycle through each day
for dates in all_days:

    # print the calendar
    for day, date in zip(days, dates):
        if date == 0:
            continue

        # format the day
        text = "{day}, {month} {date}".format(
            **{"day": day, "month": months[month], "date": date})

        # print the day header by our preferred format
        if markdown:
            cal_string = cal_string + "# " + text
        else:
            cal_string = cal_string + text + '\n'
            cal_string = cal_string + "-" * len(text)
        cal_string = cal_string + "\n"

        # Here, let's add weekly specific items
        if whom == "nelle":
            cal_string = nelle_specific_stuff(day, date, month, year,
                                              cal_string)
        elif whom == "alex":
            cal_string = alex_specific_stuff(day, date, month, year,
                                             cal_string)
        cal_string = cal_string + '\n'

# print or save as desired
if save is None:
    print(cal_string)
else:
    with open(save, "w") as calendar_file:
        calendar_file.write(cal_string)
