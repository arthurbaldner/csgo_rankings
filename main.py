from day_of_week import date_for_crawler, monthly_loop
from crawler import csgo_crawler
import csv
from datetime import datetime

def main():

    columns = ['Date',  'Team', 'Standing', 'Player 1', 
                'Country 1', 'Player 2', 'Country 2', 
                'Player 3', 'Country 3', 'Player 4', 
                'Country 4', 'Player 5', 'Country 5']

    file_name = 'test'
    with open(f'{file_name}.csv', 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(columns)

        for i in monthly_loop(2018, 1, 2021, 12):
            temp = i.split('-')
            year, month_name, day = date_for_crawler(int(temp[0]), int(temp[1]))
            month_name = month_name.lower()
            team_list = csgo_crawler(year,month_name,day)

            standing = 1
            month_number = datetime.strptime(month_name, "%B").month
            for key in team_list.keys():
                w.writerow([f'{day}-{month_number}-{year}', key,  str(standing)] + team_list[key])
                print(key, standing, team_list[key])
                standing += 1


if __name__ == '__main__':
    main()

