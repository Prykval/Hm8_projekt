from datetime import date, timedelta

def get_birthdays_per_week(users):
    if not users:
        return {}

    new_users = {
        'Monday': [],
        'Tuesday': [],
        'Wednesday': [],
        'Thursday': [],
        'Friday': []
    }

    today = date.today()
    year = today.year
    current_day_of_week = today.weekday()
    days_until_end_of_week = 6 - current_day_of_week
    days_until_next_week = days_until_end_of_week + 1
    first_day_of_next_week = today + timedelta(days=days_until_next_week)
    last_day_of_next_week = first_day_of_next_week + timedelta(days=6)

    first_day_of_next_week = first_day_of_next_week.replace(year=year)
    last_day_of_next_week = last_day_of_next_week.replace(year=year)
    last_day_of_carrent_week=today+timedelta(days=7)
    for user in users:
        name = user['name']
        birthday_date = user['birthday'].replace(year=year)

        # Перевірка, чи день народження вже минув у цьому році
        if birthday_date < today:
           birthday_date = birthday_date.replace(year=today.year + 1)

        # Перевірка, чи день народження випадає на вихідний (суботу або неділю)
        if today <=birthday_date<=last_day_of_carrent_week:

        # Визначення, на який день тижня припадає день народження
         birthday_date_day = birthday_date.weekday()
         if birthday_date_day == 0:
            new_users['Monday'].append(name)
         elif birthday_date_day == 1:
            new_users['Tuesday'].append(name)
         elif birthday_date_day == 2:
            new_users['Wednesday'].append(name)
         elif birthday_date_day == 3:
            new_users['Thursday'].append(name)
         elif birthday_date_day==4:
            new_users['Friday'].append(name)
         elif birthday_date_day in (5,6):
            new_users['Monday'].append(name)

    # Видаляємо порожні списки зі словника
    new_users = {day: names for day, names in new_users.items() if names}
    print(new_users)
    return new_users