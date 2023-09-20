from datetime import datetime, timedelta

def schedule_(days, work_days, rest_days, start_date):
    schedule = []
    current_date = start_date
    work_count = 0
    rest_count = 0

    while len(schedule) < days:
        if work_count < work_days:
            schedule.append(current_date)
            work_count += 1
        elif rest_count < rest_days:
            current_date += timedelta(days=1)
            schedule.append(current_date)
            rest_count += 1
        else:
            current_date += timedelta(days=1)
            work_count = 0
            rest_count = 0

    return schedule


start_date = datetime(2020, 1, 30)
schedule = schedule_(5, 2, 1, start_date)
for date in schedule:
    print(date)