def alex_specific_stuff(day, date, month, year, calendar_string):
    """
    Alex's specific stuff
    """

    # specify work days
    at_work_days = ['Monday',
                    'Tuesday',
                    'Wednesday',
                    'Thursday']

    # print food and social
    if day in at_work_days:
        calendar_string = calendar_string + '- **Food and social**\n'
        calendar_string = calendar_string + '\t- Morning coffee (15 min)\n'
        if day != "Thursday":
            calendar_string = calendar_string + "\t- Lunch (1 hour)\n"
        calendar_string = calendar_string + '\t- Afternoon tea (15 min)\n'

    # print accountability
    if day in at_work_days:
        calendar_string = calendar_string + "- **Accountability**\n"
        calendar_string = calendar_string + "\t- Create to-do list (15 min)\n"
        calendar_string = calendar_string + "\t- Update to-do list (15 min)\n"

    # print regular meetings
    if day in at_work_days:
        calendar_string = calendar_string + '- **Meetings**\n'
        if day == "Monday":
            calendar_string = calendar_string + ("\t - Weekly accountability "
                                                 "meeting with Nelle Varoquaux"
                                                 " (1 hour)\n")
        if day == "Wednesday":
            calendar_string = calendar_string + ("\t- Weekly lab meeting (1 "
                                                 "hour)\n")
            calendar_string = calendar_string + ("\t- Weekly meeting with Tom"
                                                 " Griffiths (30 min)\n")
        if day == "Thursday":
            calendar_string = calendar_string + ("\t- BIDS Lunch (1 hour, 30 "
                                                 "min)\n")

    # print personal things
    if day == "Thursday":
        calendar_string = calendar_string + '- **Personal**\n'
        calendar_string = calendar_string + "\t- 7pm: BAD scrimmage\n"

    # give us back our string
    return calendar_string
