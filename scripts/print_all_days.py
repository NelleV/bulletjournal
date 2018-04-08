import calendar
import argparse
from nelle import nelle_specific_stuff
from alex import alex_specific_stuff

parser = argparse.ArgumentParser()
parser.add_argument("month", type=int)
parser.add_argument("--year", default=2018)
parser.add_argument("--markdown", default=False, action="store_true")
parser.add_argument("--whom", default=None)
args = parser.parse_args()

year = args.year
month = args.month
markdown = args.markdown
whom = args.whom

if whom is not None and whom not in ["alex", "nelle"]:
 
    raise ValueError("I do not know who that person is")

cal = calendar.TextCalendar()
all_days = cal.monthdayscalendar(year, month)

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday",
        "Sunday"]

months = {1: "January",
          2: "February",
          3: "March",
          4: "April",
          5: "May"}

for dates in all_days:
    for day, date in zip(days, dates):
        if date == 0:
            continue

        text = "{day}, {month} {date}".format(
            **{"day": day, "month": months[month], "date": date})
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
