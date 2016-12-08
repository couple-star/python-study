breakfast_special='texas omelet'
breakfast_note='contains brisket,horseradish cheddar'
lunch_special='greek patty melt'
lunch_note='like the regular one, but with tzatziki sauce'
dinner_special='buffalo steak'
dinner_note='top loin with hot sauce and blue cheese, not buffalo meat'
meal_time=raw_input('which mealtime do you want? [breakfast, lunch, dinner,q to quit]')
print 'specials for{}:'.format(meal_time)
if meal_time=='breakfast':
    print breakfast_special
    print breakfast_note
elif meal_time=='lunch':
    print lunch_special
    print lunch_note
elif meal_time=='dinner':
    print dinner_special
    print dinner_note
else:
    print 'sorry,{} isn\'t valid.'.format(meal_time)