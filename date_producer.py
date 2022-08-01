from datetime import datetime, timedelta
import os

def date_range(start, end):
    delta = end - start  # as timedelta
    days = [start + timedelta(days=i) for i in range(delta.days + 1)]
    return days

def get_total_weeks():
    start_date = datetime(2022, 1, 1)
    end_date = datetime(2022, 8, 1)

    all_dates = (date_range(start_date, end_date))
    count = 0
    new_start_date = 0
    date_dict = dict()
    for i in range(0,len(all_dates)-7):
        start_date = str(all_dates[i]).replace('-','').replace(' ','').replace(':','')
        end_date = str(all_dates[i+7]).replace('-','').replace(' ','').replace(':','')
        if new_start_date == 0 or new_start_date == start_date:
            new_start_date = end_date
            # print(start_date, '< --- >',end_date)
            date_dict[str(count)] = start_date+','+end_date
            count +=1
    return date_dict
