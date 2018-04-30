# specify daily-specific formatting stuff
def alex_daily_specific(day, date, month, year, calendar_string):
    """
    Alex's specific stuff
    """

    # specify work days
    at_work_days = ['Monday',
                    'Tuesday',
                    'Wednesday',
                    'Thursday']

    # specify all work days
    all_work_days = at_work_days + ['Sunday']

    # initialize the calendar string
    calendar_string = ''

    # create a weekly summary section
    if day == 'Monday':

        # create headers
        weekly_summary_header = ('# Weekly to-do list for week of ' +
                                 month + ' ' + date + ', ' + year + '\n')
        two_week_goal_header = '\n## Two-week goal: \n'
        weekly_goal_header = ('\n## Three goals for the week:\n' +
                              '1. ...\n' +
                              '1. ...\n' +
                              '1. ...\n')

        # create weekly overview
        weekly_overview_header = ('\n## Overview of things I need to do ' +
                                  'this week\n')
        weekly_overview = ''
        for day in at_work_days:
            weekly_overview = '- **' + day + '** (hours)\n'

        # create breakdown by project
        breakdown_header = '\n## Breakdown by project\n'
        breakdown_table = ('| Project | Day | Time |\n' +
                           '| ------- | --- | ---- |\n')

        # create scratchpad for things I need to do
        scratchpad_header = '\n## Other things I need to do\n'

        # assemble it
        calendar_string = (calendar_string +
                           weekly_summary_header +
                           two_week_goal_header +
                           weekly_goal_header +
                           weekly_overview_header +
                           weekly_overview +
                           breakdown_header +
                           breakdown_table +
                           scratchpad_header +
                           '\n***\n\n')

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
        if day != "Thursday":
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
        if day == "Wednesday":
            calendar_string = calendar_string + ("| | Weekly lab meeting | 1 "
                                                 "hour | |\n")
            calendar_string = calendar_string + ("| | Weekly meeting with Tom"
                                                 " Griffiths | 30 min | |\n")
        if day == "Thursday":
            calendar_string = calendar_string + ("| | BIDS lunch | 1 hour, 30 "
                                                 "min | |\n")

    # print personal things
    if day == "Thursday":
        calendar_string = calendar_string + ('| **Personal** | -- | |'
                                             ' |\n')
        calendar_string = calendar_string + ('| | BAD scrimmage | |'
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


# any birds-eye-specific stuff would go here
def alex_birdseye_specific():

    print("This is where Alex's specific stuff would go!")
