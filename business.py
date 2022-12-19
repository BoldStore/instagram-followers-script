import requests
import json
import time


import csv

import instaloader

# Creating an instance of the Instaloader class
bot = instaloader.Instaloader()
bot.login("avivashishta", "AviVashishta29072002") 


with open('followerCount.txt', 'w') as f:
    with open('list.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            line_count += 1
            username = row[0]
            # username = username.replace(" ","" )
            # print(username)
            # data = requests.get('https://i.instagram.com/api/v1/users/web_profile_info/?username='+username, headers={"User-Agent":"Instagram 76.0.0.15.395 Android (24/7.0; 640dpi; 1440x2560; samsung; SM-G930F; herolte; samsungexynos8890; en_US; 138226743"})
            # if data and data.status_code == 200 and json.loads(data.content)['data'] and json.loads(data.content)['data']['user']:
            #     followers = json.loads(data.content)
            #     f.write(str(followers['data']['user']['edge_followed_by']['count']))
            #     f.write("\n")
            # else: 
            #     f.write("0")
            #     f.write("\n")
            # Loading a profile from an Instagram handle
            profile = instaloader.Profile.from_username(bot.context, username)
            print(line_count,"Followers Count: ", str(profile.followers))
            f.write(str(profile.followers))
