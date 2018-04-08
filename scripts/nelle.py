# daily-specific formatting
def nelle_daily_specific(day, date, month, year, calendar_string):
    """
    Nelle's specific daily stuff
    """
    if day == "Thursday":
        calendar_string = calendar_string + "- BIDS lunch: 12.30pm to 2pm\n"
        calendar_string = calendar_string + "- Numpy meeting: 3pm to 3.30pm\n"
        calendar_string = calendar_string + ("- Ben & Nelle meeting: 3.30pm to"
                                             "4.30pm\n")
    if day == "Monday":
        calendar_string = calendar_string + ("- Alex & Nelle meeting: 11.30am"
                                             "to 12.30pm\n")
        calendar_string = calendar_string + ("- Elizabeth & Nelle meeting: 7am"
                                             "to 8am\n")

    # give us back our string
    return calendar_string


# any birds-eye-specific stuff would go here
def nelle_birdseye_specific():

    print("This is where Nelle's specific stuff would go!")
