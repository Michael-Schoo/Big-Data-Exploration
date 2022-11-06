import csv
import matplotlib.pyplot as plt
import numpy as np

# table
# 2003-2020
# average_taxable_income
# line graph

# Get the ABNs
abns = [row for row in csv.DictReader(open('./data/ABNs.csv', 'r'))]

# Set the tax data
tax = {}

# Go through each entry of tax per suburb, and construct a dictionary keyed by postcode
for row in csv.DictReader(open('./data/TaxPerSuburb.csv', 'r')):
    key = row['postcode']
    tax[key] = row


# Get the amount of ABNs per postcode
postcodes = {}
for code in abns:
    # Use the dict to increment the count
    postcodes[code['AddressPostcode']] = postcodes.get(code['AddressPostcode'], 0) + 1

# Make the dictionary for total data
average_tax = {
    # '2003': 0,
    # '2004': 0,
    # '2005': 0,
    # '2006': 0,
    # '2007': 0,
    # '2008': 0,
    # '2009': 0,
    # '2010': 0,
    # '2011': 0,
    # '2012': 0,
    '2013': 0,
    '2014': 0,
    '2015': 0,
    '2016': 0,
    '2017': 0,
    '2018': 0,
    '2019': 0,
}

median_tax = {
    '2013': 0,
    '2014': 0,
    '2015': 0,
    '2016': 0,
    '2017': 0,
    '2018': 0,
    '2019': 0,
}


def year_to_range(year):
    # 2003 -> 2003-04
    # last two digits
    last_two = year[-2:]
    # first two digits
    first_two = year[:2]
    # add 1 to last two digits
    last_two_2 = str(int(last_two) + 1)
    # return first two digits + last two digits + first two digits + last two digits + 2
    return first_two + last_two + '-' + last_two_2


# Go through the postcodes and use census data to add total data
for code in postcodes:
    # If the postcode exists in the tax database
    if code in tax:
        # Go through the years used for average data and and add the year's taxable income
        for year in average_tax:
            average_tax[year] += float(tax.get(code, {}).get('average_taxable_income_'+year_to_range(year), 2) or 0)
        
        # Go through the years used for median data and and add the year's taxable income
        for year in median_tax:
            median_tax[year] += float(tax.get(code, {}).get('median_taxable_income_'+year_to_range(year), 2) or 0)

#### Set up Matplotlib ####

# make line graph
# x axis: years
# y axis: average taxable income
# line graph (average taxable income) vs (median taxable income)

# Make figure and set its metadata (title, subtitle, and dimensions)
plt.figure('Taxable income with common postcodes', figsize=(7, 6))
plt.title('Average and Median Taxable Income Over Time')
plt.suptitle("Taxable income with common postcodes", y=0.965, fontweight="bold", fontsize=16)
plt.text(0.5, 0.95, '(based on business locations)', ha='center', fontsize=12)

#### Add data ####
# Add the average tax data
plt.plot(list(average_tax.keys()), list(average_tax.values()), label='Average Taxable Income')

# Add the median tax data
plt.plot(list(median_tax.keys()), list(median_tax.values()), label='Median Taxable Income')

# Add lables
plt.xlabel('Year')
plt.ylabel('Taxable Income')
plt.legend()

### Showing/saving the plot ###
print("showing plot...")
plt.savefig("../tax_generated_over_time.png")
plt.show()
print("shown and saved plot!")
