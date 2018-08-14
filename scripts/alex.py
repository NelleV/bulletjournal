# specify daily-specific formatting stuff with time-tracking
def alex_daily_specific(day, date, month, year, calendar_string):
    """
    Alex's specific stuff
    """

    # specify work days
    at_work_days = ['Monday',
                    'Tuesday',
                    'Wednesday',
                    'Thursday',
                    'Friday']

    # specify all work days
    all_work_days = at_work_days

    # create header for work days
    if day in all_work_days:

        # add goal header
        goal_subheader = ('### Primary foci: \n\n')

        # print table formatting header
        table_header = ("| Project | Activity | Anticipated time | Total time"
                        " |\n"
                        "|---------|----------|------------------|------------"
                        "|\n")

        # assemble it
        calendar_string = calendar_string + goal_subheader + table_header

    # print food and social
    if day in at_work_days:
        calendar_string = calendar_string + ('| **Food and social** | -- | |'
                                             ' |\n')
        calendar_string = calendar_string + ('| | Morning coffee | 15 min |'
                                             ' |\n')
        calendar_string = calendar_string + ('| | Lunch | 1 hour |'
                                             ' |\n')
        calendar_string = calendar_string + ('| | Afternoon tea | 15 min |'
                                             ' |\n')
    # print accountability
    if day in all_work_days:
        calendar_string = calendar_string + ('| **Accountability** | -- | |'
                                             ' |\n')
        calendar_string = calendar_string + ('| | Create to-do list | 15 min |'
                                             ' |\n')
        calendar_string = calendar_string + ('| | Update to-do list | 15 min |'
                                             ' |\n')

    # print regular meetings
    if day in at_work_days:
        calendar_string = calendar_string + '| **Meetings** | -- | | |\n'
        if day == "Monday":
            calendar_string = calendar_string + ("| | Weekly accountability "
                                                 "meeting with Nelle Varoquaux"
                                                 " | 1 hour | |\n")

    # print personal things
    if day == "Tuesday":
        calendar_string = calendar_string + ('| **Personal** | -- | |'
                                             ' |\n')

    # add a cumulative time
    if day in all_work_days:
        calendar_string = calendar_string + ('| ***All*** | -- | |'
                                             ' |\n')

    # if we're in a work day, allow for activity logs
    if day in all_work_days:
        log_footer = '\n### Activity logs \n'
        calendar_string = calendar_string + log_footer

    # add a section for the grateful list
    calendar_string = calendar_string + "\n### Today, I'm grateful for...\n"
    calendar_string = calendar_string + "1. ...\n"
    calendar_string = calendar_string + "1. ...\n"
    calendar_string = calendar_string + "1. ...\n"

    # add a horizontal line between days
    calendar_string = calendar_string + "\n***\n"

    # give us back our string
    return calendar_string


# specify simplified daily-specific formatting (e.g., for summer)
def alex_daily_simplified(day, date, month, year, calendar_string):
    """
    Alex-specific formatting with simplified reporting and tracking
    """

    # specify work days
    at_work_days = ['Monday',
                    'Tuesday',
                    'Wednesday',
                    'Thursday',
                    'Friday']

    # specify all work days
    all_work_days = at_work_days

    # create header for work days
    if day in all_work_days:

        # add goal header
        goal_subheader = ('### Primary foci: \n\n')

        # print table formatting header
        table_header = ("| Project | Activity | Done? |\n"
                        "|---------|----------|:-----:|\n")

        # assemble it
        calendar_string = calendar_string + goal_subheader + table_header

    # print accountability
    if day in all_work_days:
        calendar_string = calendar_string + ("| **Accountability**"
                                             "| Create to-do list |  | \n")
        calendar_string = calendar_string + ("| **Accountability**"
                                             "| Update to-do list |  | \n")

    # print regular meetings
    if day in at_work_days:
        if day == "Monday":
            calendar_string = calendar_string + ("| **Meetings** "
                                                 "| Weekly meeting with "
                                                 "Nelle Varoquaux |  |\n")

    # add a cumulative time
    if day in all_work_days:
        calendar_string = calendar_string + ('| ***All*** | -- | |'
                                             ' |\n')

    # if we're in a work day, allow for activity logs
    if day in all_work_days:
        log_footer = '\n### Activity logs \n'
        calendar_string = calendar_string + log_footer

    # add a section for the grateful list
    calendar_string = calendar_string + "\n### Today, I'm grateful for...\n"
    calendar_string = calendar_string + "1. ...\n"
    calendar_string = calendar_string + "1. ...\n"
    calendar_string = calendar_string + "1. ...\n"

    # add a horizontal line between days
    calendar_string = calendar_string + "\n***\n"

    # give us back our string
    return calendar_string


# any birds-eye-specific stuff would go here
def alex_birdseye_specific():

    print("This is where Alex's specific stuff would go!")
