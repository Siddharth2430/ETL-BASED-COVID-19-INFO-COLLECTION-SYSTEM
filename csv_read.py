import csv

with open('final_covid_stats.csv', 'r') as file:
    reader = csv.reader(file)
    csv_count = 0
    for row in reader:
        count += 1