from datetime import datetime, date, timedelta
from pandas import period_range, PeriodIndex

def find_first_monday(year, month):
    d = datetime(year, month, 7)
    offset = -d.weekday() #weekday = 0 means monday
    return d + timedelta(offset)

def date_for_crawler(year, month):
    date_crawler = find_first_monday(year, month)
    date_year = date_crawler.year
    date_month = date_crawler.strftime("%B")
    date_day = date_crawler.day
    return [date_year, date_month, date_day]

def monthly_loop(year_begin, month_begin, year_end, month_end):
    # all inputs are ints
    
    date_begin = f'{year_begin}-{month_begin}'
    date_end = f'{year_end}-{month_end}'
    dates_to_crawl = []

    p = period_range(start=date_begin, end=date_end, freq='M')

    for i in p.strftime('%Y-%m'):
        dates_to_crawl.append(i)
    
    return dates_to_crawl





# x = monthly_loop(2019,1,2020,2)
# print(x[0].split('-'))




    

