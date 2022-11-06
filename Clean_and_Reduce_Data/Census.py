
import csv

csv_columns = [
    'year',
    'postcode',
    'total_population',
    'median_total_personal_income_weekly',
    'median_total_family_income_weekly',
    'labor_force',
]


with open('../Analyze_Data/data/Census.csv', 'w', newline='') as csvfile:

    census_reader = open('./data/Census.csv', 'r')
    reader = csv.DictReader(census_reader)
    data = [row for row in reader]

    # nothing to clean

    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
    writer.writeheader()
    writer.writerows(data)
