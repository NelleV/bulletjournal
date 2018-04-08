def alex_specific_stuff(day, date, month, year, calendar_string):
    """
    Alex's specific stuff
    """

    # print food and social
    calendar_string = calendar_string + '\n## Food and social\n'
    calendar_string = calendar_string + '- Morning coffee (15 min)\n'
    if day != "Thursday":
        calendar_string = calendar_string + "- Lunch (1 hour)\n"
    calendar_string = calendar_string + '- Afternoon tea (15 min)\n'

    # print regular meetings
    calendar_string = calendar_string + '\n## Meetings\n'
    if day == "Monday":
        calendar_string = calendar_string + ("- Weekly accountability meeting"
                                             "with Nelle Varoquaux (1 hour)\n")
    if day == "Wednesday":
        calendar_string = calendar_string + "- Weekly lab meeting (1 hour)\n"
        calendar_string = calendar_string + ("- Weekly meeting with Tom"
                                             "Griffiths (30 min)\n")
    if day == "Thursday":
        calendar_string = calendar_string + "- BIDS Lunch (1 hour, 30 min)\n"

    # print personal things
    calendar_string = calendar_string + '\n## Personal\n'
    if day == "Thursday":
        calendar_string = calendar_string + "- 7pm: BAD scrimmage\n"

    # give us back our string
    return calendar_string
