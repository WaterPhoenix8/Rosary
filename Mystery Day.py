days_of_the_week = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')

while True:
    day = input('\nWhat day is today (in abbreviated form please)? ')
    if day not in days_of_the_week:
        print('Your input is invalid.')
    else:
        if day == days_of_the_week[0] or day == days_of_the_week[5]:
            print('\nToday is Joyful Mysteries Day!')
            print('\n\t1. The Annunciation')
            print('\n\t2. The Visitation')
            print('\n\t3. The Nativity')
            print('\n\t4. The Presentation in the Temple')
            print('\n\t5. The Finding of Jesus in the Temple')
        elif day == days_of_the_week[1] or day == days_of_the_week[4]:
            print('\nToday is Sorrowful Mysteries Day!')
            print('\n\t1. The Agony in the Garden')
            print('\n\t2. The Scourging at the Pillar')
            print('\n\t3. The Crowning with Thorns')
            print('\n\t4. The Carrying of the Cross')
            print('\n\t5. The Crucifixion')
        elif day == days_of_the_week[2] or day == days_of_the_week[6]:
            print('\nToday is Glorious Mysteries Day!')
            print('\n\t1. The Resurrection')
            print('\n\t2. The Ascension')
            print('\n\t3. The Descent of the Holy Spirit')
            print('\n\t4. The Assumption')
            print('\n\t5. The Coronation')
        elif day == days_of_the_week[3]:
            print('\nToday is Luminous Mysteries Day!')
            print('\n\t1. The Baptism of Our Lord')
            print('\n\t2. The Wedding of Cana')
            print('\n\t3. The Proclamation of the Kingdom')
            print('\n\t4. The Transfiguration')
            print('\n\t5. The Institution of the Eucharist')
        break



#day = input('\nWhat day is today (in abbreviated form please)? ')

#while day not in days_of_the_week:
    #print('You input is invalid.')