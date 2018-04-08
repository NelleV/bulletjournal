def alex_specific_stuff(day, date, month, year):
    """
    Alex's specific stuff
    """

    # print food and social
    print('## Food and social')
    print('- Morning coffee (15 min)')
    if day != "Thursday":
        print("- Lunch (1 hour)")
    print('- Afternoon tea (15 min)')

    # print regular meetings
    print('## Meetings')
    if day == "Monday":
        print("- Weekly accountability meeting with Nelle Varoquaux (1 hour)")
    if day == "Wednesday":
        print("- Weekly lab meeting (1 hour)")
        print("- Weekly meeting with Tom Griffiths (30 min)")
    if day == "Thursday":
        print("- BIDS Lunch (1 hour, 30 min)")

    # print personal things
    print('## Personal')
    if day == "Thursday":
        print("- 7pm: BAD scrimmage")
