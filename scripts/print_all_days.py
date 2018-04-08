import calendar
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("month", type=int)
parser.add_argument("--year", default=2018)
parser.add_argument("--markdown", default=False, action="store_true")
args = parser.parse_args()

year = args.year
month = args.month
markdown = args.markdown

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
