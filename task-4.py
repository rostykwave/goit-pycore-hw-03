from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    next_week = today + timedelta(days=7)
    
    upcoming_birthdays = []

    for user in users:
        birthday_date = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        
        birthday_this_year = birthday_date.replace(year=today.year)
        
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        
        if today <= birthday_this_year <= next_week:
            if birthday_this_year.weekday() in (5, 6):  # Saturday = 5, Sunday = 6
                # Find next Monday
                days_to_monday = 7 - birthday_this_year.weekday()
                congratulation_date = birthday_this_year + timedelta(days=days_to_monday)
            else:
                congratulation_date = birthday_this_year
            
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })
    
    return upcoming_birthdays

# Example of usage
users = [
    {"name": "Jaden Smith", "birthday": "1990.07.20"},
    {"name": "John Doe", "birthday": "1985.02.23"},
    {"name": "Jane Smith", "birthday": "1990.02.27"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
