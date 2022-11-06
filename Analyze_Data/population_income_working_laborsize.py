import csv
import matplotlib.pyplot as plt
import numpy as np

# table
# 2011 vs 2021
# population vs income vs working age population
# 3 bar graphs


abns = [row for row in csv.DictReader(open('./data/ABNs.csv', 'r'))]
print(len(abns))

census = {}

for row in csv.DictReader(open('./data/Census.csv', 'r')):
    # print(row)
    key = (int(row['year']), row['postcode'])
    census[key] = {}
    census[key]['total_population'] = int(row['total_population'])
    census[key]['median_total_personal_income_weekly'] = int(row['median_total_personal_income_weekly'])
    census[key]['median_total_family_income_weekly'] = int(row['median_total_family_income_weekly'])
    census[key]['labor_force'] = int(row['labor_force'])

# print(census)
print(census[(2011, '2000')])

# get the amount of ABNs per postcode
postcodes = {}
for code in abns:
    postcodes[code['AddressPostcode']] = postcodes.get(code['AddressPostcode'], 0) + 1


data_2011 = {'population': 0, 'income': 0, 'working_age_population': 0}
data_2021 = {'population': 0, 'income': 0, 'working_age_population': 0}
for code in postcodes:
    data_2011['population'] += census.get((2011, code), {}).get('total_population', 0)
    data_2021['population'] += census.get((2021, code), {}).get('total_population', 0)
    data_2011['income'] += census.get((2011, code), {}).get('median_total_personal_income_weekly', 0)
    data_2021['income'] += census.get((2021, code), {}).get('median_total_personal_income_weekly', 0)
    data_2011['working_age_population'] += census.get((2011, code), {}).get('labor_force', 0)
    data_2021['working_age_population'] += census.get((2021, code), {}).get('labor_force', 0)


#### Set up Matplotlib ####

# make 3 bar graphs using subplots
# population 2021 vs 2011
# income 2021 vs 2011
# working age population 2021 vs 2011
fig, (ax1, ax2, ax3) = plt.subplots(3, 1)
ax1.bar(['2011', '2021'], [data_2011['population'], data_2021['population']])
ax1.set_title('Population')
ax2.bar(['2011', '2021'], [data_2011['income'], data_2021['income']])
ax2.set_title('Income')
ax3.bar(['2011', '2021'], [data_2011['working_age_population'], data_2021['working_age_population']])
ax3.set_title('Working Age Population')

### Showing/saving the plot ###
print("showing plot...")
plt.savefig("../population_income_working_laborsize.png")
plt.show()
print("shown and saved plot!")
