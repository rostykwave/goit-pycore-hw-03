from datetime import datetime

def get_days_from_today(date):
    try:
        # Convert a string to a date object
        given_date = datetime.strptime(date, "%Y-%m-%d").date()

        # Get the current date
        todays_date = datetime.now().date()

        # Calculation of the difference in days
        delta_in_days = (todays_date - given_date).days
        return delta_in_days
    except ValueError:
        return "Incorrect date format. Use the 'YYYY-MM-DD' format instead."

print(get_days_from_today("2020-10-09"))
print(get_days_from_today("2025-10-09"))
print(get_days_from_today("Incorrect date format"))