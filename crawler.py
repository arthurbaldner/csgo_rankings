from distutils import archive_util
from bs4 import BeautifulSoup
import requests

# def csgo_crawler(year, month, day):

#     link_to_crawl = f"https://www.hltv.org/ranking/teams/{year}/{month}/{day}"
#     source = requests.get(link_to_crawl).text
#     soup = BeautifulSoup(source, "lxml")

#     team_list = {}
#     standing = 1
#     for team_html in soup.find_all("div", class_="ranked-team"):
#         team_name_temp = team_html.find("div", class_="teamLine")
#         team_name = team_name_temp.text.split("(")[0]

#         player_list = []
#         for team_player in team_html.find_all("div", class_="nick"):
#             team_player_name = team_player.text
#             team_player_country = team_player.img["title"]
#             player_list.append((team_player_name, team_player_country))

#         #team_list[team_name] = player_list
#         team_list[(team_name, standing)] = player_list
#         standing += 1

#     return team_list


def csgo_crawler(year, month, day):

    link_to_crawl = f"https://www.hltv.org/ranking/teams/{year}/{month}/{day}"
    source = requests.get(link_to_crawl).text
    soup = BeautifulSoup(source, "lxml")

    team_list = {}
    for team_html in soup.find_all("div", class_="ranked-team"):
        team_name_temp = team_html.find("div", class_="teamLine")
        team_name = team_name_temp.text.split("(")[0]

        player_list = []
        for team_player in team_html.find_all("div", class_="nick"):
            team_player_name = team_player.text
            team_player_country = team_player.img["title"]
            player_list.append(team_player_name)
            player_list.append(team_player_country)

        team_list[team_name] = player_list

    return team_list



# year = 2018
# month = "march"
# day = 5

# x = csgo_crawler(year, month, day)
# print(x)
