# daily-specific formatting
def nelle_daily_specific(day, date, month, year, calendar_string):
    """
    Nelle's specific daily stuff
    """
    if day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
        calendar_string = (calendar_string +
                           "- BREAK Lunch [1h]\n")
        calendar_string = (calendar_string +
                           "- BREAK Morning coffee break [15min]\n")

        calendar_string = (calendar_string +
                           "- BREAK Afternoon coffee break [15min]\n")

    if day == "Monday":
        calendar_string = calendar_string + ("- ACCOUNTABILITY Alex & Nelle meeting: 11.30am"
                                             "to 12.30pm\n")
        calendar_string = calendar_string + ("- EPICON Elizabeth & Nelle meeting: 7am"
                                             "to 8am\n")
        calendar_string = calendar_string + ("- DIPLOID Diploid meeting: 9am"
                                             "to 10am\n")
    if day == "Wednesday":
        calendar_string = calendar_string + ("- Normalization meeting: 8.30am"
                                             "to 9.30am\n")
    if day == "Thursday":
        calendar_string = (
            calendar_string + "- **BIDS** BIDS lunch: 12.30pm to 2pm\n")
        calendar_string = calendar_string + (
            "- **EPICON** Ben & Nelle meeting: 3.30pm to"
            "4.30pm\n")

    # give us back our string
    return calendar_string


# any birds-eye-specific stuff would go here
def nelle_birdseye_specific():

    print("This is where Nelle's specific stuff would go!")
