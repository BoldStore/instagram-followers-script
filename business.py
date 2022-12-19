import csv
import instaloader
import requests


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
            try:
                profile = instaloader.Profile.from_username(bot.context, username)
                print(line_count,"Followers Count: ", str(profile.followers))
                f.write(str(profile.followers)+"\n")
            except:
                print(line_count,"Followers Count: ", "0")
                f.write("0"+"\n")
            

