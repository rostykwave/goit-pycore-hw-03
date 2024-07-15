from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    next_week = today + timedelta(days=7)
    
    upcoming_birthdays = []

    for user in users:
        name = user["name"]
        birthday_str = user["birthday"]
        birthday_date = datetime.strptime(birthday_str, "%Y.%m.%d").date()
        
        # Birthday in the current year
        birthday_this_year = birthday_date.replace(year=today.year)
        
        # If the birthday has already passed, consider the next year
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        
        # Checking if the birthday is in the next 7 days
        if today <= birthday_this_year <= next_week:
            # If the birthday falls on a weekend, we postpone it to the following Monday
            if birthday_this_year.weekday() in (5, 6):  # Saturday = 5, Sunday = 6
                # Find next Monday
                days_to_monday = 7 - birthday_this_year.weekday()
                congratulation_date = birthday_this_year + timedelta(days=days_to_monday)
            else:
                congratulation_date = birthday_this_year
            
            upcoming_birthdays.append({
                "name": name,
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })
    
    return upcoming_birthdays

# Приклад використання
users = [
    {"name": "Jaden Smith", "birthday": "1990.07.20"},
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
