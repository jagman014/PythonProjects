import csv
import os

directory = os.path.dirname(__file__)
filename = os.path.join(directory, 'movies.csv')

movies = [["Top Gun", "Risky Business", "Minority Report"],
          ["Titanic", "The Revenant", "Inception"],
          ["Training Day", "Man on Fire", "Flight"]]

with open(filename, 'w') as csvfile:
    write = csv.writer(csvfile, delimiter=',')
    for idx in movies:
        write.writerow(idx)
