def add_weekly_table(calendar_string):

    # create a two-week goal subheader
    two_week_goals = '## Two-week goal: \n\n'
    calendar_string = calendar_string + two_week_goals

    # add three primary weekly goals subheader
    three_weekly_goals = ("## Three goals for the week: \n"
                          "1. \n" +
                          "1. \n" +
                          "1. \n" +
                          '\n\n')
    calendar_string = calendar_string + three_weekly_goals

    # print table formatting header
    table_header = ("| Project | Activity | Anticipated time | Total time"
                    " |\n"
                    "|---------|----------|------------------|------------"
                    "|\n")
    calendar_string = calendar_string + table_header

    # add table footer
    calendar_string = calendar_string + ('| ***All*** | -- | |'
                                         ' |\n\n')

    # give us back our string
    return calendar_string
