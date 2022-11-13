from facebook_scraper import get_posts
import json
import requests
import shutil

import csv
data_file = open('data_file.csv','w')
csv_writer = csv.writer(data_file)
for post in get_posts('613870175328566', pages=3):
    print(post['username'])
    print(post['images'])
    csv_writer.writerow([post['username'], post['images']])
data_file.close()


