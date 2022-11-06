
import csv

csv_columns = [
# too long to copy
]


with open('../Analyze_Data/data/TaxPerSuburb.csv', 'w', newline='') as csvfile:

    census_reader = open('./data/TaxPerSuburb.csv', 'r')
    reader = csv.DictReader(census_reader)
    data = [row for row in reader]

    # nothing to clean

    writer = csv.DictWriter(csvfile, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)
