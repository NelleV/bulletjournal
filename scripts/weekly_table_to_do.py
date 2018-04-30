def add_weekly_table(calendar_string, days):

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
    for day in days:
        weekly_overview = weekly_overview + '- **' + day + '** ( hours)\n'

    # create breakdown by project
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
