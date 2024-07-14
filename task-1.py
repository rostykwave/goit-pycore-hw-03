from datetime import datetime

def get_days_from_today(date):
    given_date = datetime.strptime(date, "%Y-%m-%d").date()
    todays_date = datetime.now().date()
    delta_in_days = (todays_date - given_date).days
    return delta_in_days


print(get_days_from_today("2020-10-09"))