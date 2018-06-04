def add_weekly_table(calendar_string, days, simplified):

    # create headers
    two_week_goal_header = '## Two-week goal: \n'
    weekly_goal_header = ('\n## Three goals for the week:\n' +
                          '1. ...\n' +
                          '1. ...\n' +
                          '1. ...\n')

    # create weekly overview
    weekly_overview_header = ('\n## Overview of things I need to do ' +
                              'this week\n')
    weekly_overview = ''

    # if simplified, only track the items
    if simplified:
        for day in days:
            weekly_overview = weekly_overview + '- **' + day + '**\n'

    # otherwise, also track hours
    else:
        for day in days:
            weekly_overview = weekly_overview + '- **' + day + '** ( hours)\n'

    # if simplified, skip project time breakdown
    if simplified:
        breakdown_table = ""
        breakdown_header = ""

    # otherwise, track project time by day
    else:
        breakdown_header = '\n## Breakdown by project\n'
        breakdown_table = ('| Project | Day | Time |\n' +
                           '| ------- | --- | ---- |\n')

    # create scratchpad for things I need to do
    scratchpad_header = '\n## Other things I need to do\n\n'

    # assemble it
    calendar_string = (calendar_string +
                       two_week_goal_header +
                       weekly_goal_header +
                       weekly_overview_header +
                       weekly_overview +
                       breakdown_header +
                       breakdown_table +
                       scratchpad_header)

    # # give us back our string
    return calendar_string
