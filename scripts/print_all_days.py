# import standard libraries
import calendar
import argparse

# import custom packages
from en_calendar import en_months, en_days
from fr_calendar import fr_months, fr_days
from weekly_table_to_do import add_weekly_table

# import specific people's info
from nelle import nelle_daily_specific
from alex import alex_daily_specific
from alex import alex_daily_simplified

# initialize the parser
parser = argparse.ArgumentParser()

# add parser arguments
parser.add_argument("month", type=int)
parser.add_argument("--year", default=2018)
parser.add_argument("--markdown", default=False, action="store_true")
parser.add_argument("--whom", default=None)
parser.add_argument("--language", default="en")
parser.add_argument("--save", default=None)  # path name to save
parser.add_argument("--simplified", default=None)  # allow simplified tracking
args = parser.parse_args()

# add arguments to namespace
year = args.year
month = args.month
markdown = args.markdown
whom = args.whom
language = args.language
save = args.save
simplified = args.simplified

# yell at us if we don't provide a valid name
if whom is not None and whom not in ["alex", "nelle"]:
    raise ValueError("I do not know who that person is")

# initialize the calendar
cal = calendar.TextCalendar()
all_days = cal.monthdayscalendar(year, month)

# account for language preference
if language == "fr":
    days = fr_days
    months = fr_months
else:
    days = en_days
    months = en_months

# create title
title_text = months[month] + " " + str(year)
if not markdown:
    title_string = (title_text + '\n' +
                    "=" * len(title_text) +
                    '\n\n-------\n\n')
else:
    title_string = ('# ' + title_text +
                    "\n\n***\n\n")

# initialize the calendar string
cal_string = title_string

# cycle through each day
for dates in all_days:

    # print the calendar
    for day, date in zip(days, dates):
        if date == 0:
            continue

        # add spaces for weekly to-do list
        if day == fr_days[0] or day == en_days[0]:
            weekly_to_do_title = ("Weekly to-do list for week of " +
                                  months[month] + " " + str(date) + ", " +
                                  str(year))

            # if it's markdown, create a weekly table
            if markdown:
                cal_string = (cal_string +
                              '# ' + weekly_to_do_title + '\n\n')
                cal_string = add_weekly_table(cal_string,
                                              days,
                                              simplified)
                cal_string = cal_string + "***\n\n"

            # if it's not markdown, just leave a space for the goals
            else:
                cal_string = (cal_string +
                              '----\n\n' +
                              weekly_to_do_title + '\n' +
                              "=" * len(weekly_to_do_title) +
                              '\n\n----\n\n')

        # format the day
        text = "{day}, {month} {date}".format(
            **{"day": day, "month": months[month], "date": date})

        # print the day header by our preferred format
        if markdown:
            cal_string = cal_string + "## " + text + "\n\n"
        else:
            cal_string = (cal_string + text + '\n' +
                          "-" * len(text) + '\n\n')

        # let's add weekly specific items
        if whom == "nelle":
            cal_string = nelle_daily_specific(day, date, month, year,
                                              cal_string)
        elif whom == "alex":
            if simplified:
                cal_string = alex_daily_simplified(day,
                                                   date,
                                                   months[month],
                                                   year,
                                                   cal_string)
            else:
                cal_string = alex_daily_specific(day,
                                                 date,
                                                 months[month],
                                                 year,
                                                 cal_string)
        cal_string = cal_string + '\n'

# print or save as desired
if save is None:
    print(cal_string)
else:
    with open(save, "w") as calendar_file:
        calendar_file.write(cal_string)
