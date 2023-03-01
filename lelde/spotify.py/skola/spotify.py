import csv
import json


json_file ="spotify,py/skola/songs.json"

songs_list = []

with open('spotify.csv', 'r', encoding='UTF8') as data_file:
    for line in csv.DictReader(data_file):
        songs_list.append(line)

with open(json_file)