import csv

file = open('ships_location.csv', 'r')

csv_reader = csv.reader(file)
for i in csv_reader:
    if i:
        print(i)