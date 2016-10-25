import datetime

day = datetime.datetime.today().weekday()

#day = int(input('\nWhat day is today (0-6)? '))

if day == 0:
    print('\nToday is Monday!')
elif day == 1:
    print('\nToday is Tuesday!')
elif day == 2:
    print('\nToday is Wednesday!')
elif day == 3:
    print('\nToday is Thursday!')
elif day == 4:
    print('\nToday is Friday!')
elif day == 5:
    print('\nToday is Saturday!')
elif day == 6:
    print('\nToday is Sunday!')

if day == 0 or day == 5:
    print('\nToday is Joyful Mysteries Day!')
    print('\n\t1. The Annunciation')
    print('\n\t2. The Visitation')
    print('\n\t3. The Nativity')
    print('\n\t4. The Presentation in the Temple')
    print('\n\t5. The Finding of Jesus in the Temple')
elif day == 1 or day == 4:
    print('\nToday is Sorrowful Mysteries Day!')
    print('\n\t1. The Agony in the Garden')
    print('\n\t2. The Scourging at the Pillar')
    print('\n\t3. The Crowning with Thorns')
    print('\n\t4. The Carrying of the Cross')
    print('\n\t5. The Crucifixion')
elif day == 2 or day == 6:
    print('\nToday is Glorious Mysteries Day!')
    print('\n\t1. The Resurrection')
    print('\n\t2. The Ascension')
    print('\n\t3. The Descent of the Holy Spirit')
    print('\n\t4. The Assumption')
    print('\n\t5. The Coronation')
elif day == 3:
    print('\nToday is Luminous Mysteries Day!')
    print('\n\t1. The Baptism of Our Lord')
    print('\n\t2. The Wedding of Cana')
    print('\n\t3. The Proclamation of the Kingdom')
    print('\n\t4. The Transfiguration')
    print('\n\t5. The Institution of the Eucharist')