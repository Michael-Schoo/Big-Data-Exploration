import csv
import matplotlib.pyplot as plt
import numpy as np

# table
# 2003-2020
# average_taxable_income
# line graph


abns = [row for row in csv.DictReader(open('./data/ABNs.csv', 'r'))]
print(len(abns))

tax = {}

for row in csv.DictReader(open('./data/TaxPerSuburb.csv', 'r')):
    # print(row)
    key = row['postcode']
    tax[key] = row
# print(tax)


# print(census)
# print(tax['2000'])

# get the amount of ABNs per postcode
postcodes = {}
for code in abns:
    postcodes[code['AddressPostcode']] = postcodes.get(
        code['AddressPostcode'], 0) + 1

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
    # '2003': 0,
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


for code in postcodes:
    if code in tax:
        for year in average_tax:
            if not float(tax.get(code, {}).get('average_taxable_income_'+year_to_range(year), 2) or 0):
                print(tax.get(code, {}))
            average_tax[year] += float(tax.get(code, {}).get('average_taxable_income_'+year_to_range(year), 2) or 0)
        for year in median_tax:
            median_tax[year] += float(tax.get(code, {}).get('median_taxable_income_'+year_to_range(year), 2) or 0)


  

# make line graph
# x axis: years
# y axis: average taxable income
# line graph (average taxable income) vs (median taxable income)
plt.plot(list(average_tax.keys()), list(average_tax.values()), label='Average Taxable Income')
plt.plot(list(median_tax.keys()), list(median_tax.values()), label='Median Taxable Income')
plt.xlabel('Year')
plt.ylabel('Taxable Income')
plt.title('Average and Median Taxable Income Over Time')
plt.legend()



# ### Showing/saving the plot ###
print("showing plot...")
plt.savefig("../tax_generated_over_time.png")
plt.show()
print("shown and saved plot!")

