import csv
import matplotlib.pyplot as plt
import numpy as np

# table
# 2011 vs 2021
# population vs income vs working age population
# 3 bar graphs

# Get the ABNs
abns = [row for row in csv.DictReader(open('./data/ABNs.csv', 'r'))]

# Set the census data
census = {}

# Go through each entry of census, and construct a tuple keyed dictionary
for row in csv.DictReader(open('./data/Census.csv', 'r')):
    key = (int(row['year']), row['postcode'])
    census[key] = {}
    census[key]['total_population'] = int(row['total_population'])
    census[key]['median_total_personal_income_weekly'] = int(row['median_total_personal_income_weekly'])
    census[key]['median_total_family_income_weekly'] = int(row['median_total_family_income_weekly'])
    census[key]['labor_force'] = int(row['labor_force'])

# Get the amount of ABNs per postcode
postcodes = {}
for code in abns:
    # Use the dict to increment the count
    postcodes[code['AddressPostcode']] = postcodes.get(code['AddressPostcode'], 0) + 1

# Make the dictionary for total data
data_2011 = {'population': 0, 'income': 0, 'working_age_population': 0}
data_2021 = {'population': 0, 'income': 0, 'working_age_population': 0}

# Go through the postcodes and use census data to add total data
for code in postcodes:
    # Add population data from the census data
    data_2011['population'] += census.get((2011, code), {}).get('total_population', 0)
    data_2021['population'] += census.get((2021, code), {}).get('total_population', 0)

    # Add the income data from the census data
    data_2011['income'] += census.get((2011, code), {}).get('median_total_personal_income_weekly', 0)
    data_2021['income'] += census.get((2021, code), {}).get('median_total_personal_income_weekly', 0)

    # Add the working age population (labor force) from the census data
    data_2011['working_age_population'] += census.get((2011, code), {}).get('labor_force', 0)
    data_2021['working_age_population'] += census.get((2021, code), {}).get('labor_force', 0)


#### Set up Matplotlib ####

# make 3 bar graphs using subplots
# population 2021 vs 2011
# income 2021 vs 2011
# working age population 2021 vs 2011
 
# Make figure and set its metadata (title, subtitle, and dimensions) 
fig, (ax1, ax2, ax3) = plt.subplots(3, 1)
fig.canvas.set_window_title('Census with common postcodes')
fig.suptitle("Census with common postcodes", y=0.965, fontweight="bold", fontsize=16)
fig.text(0.5, 0.91, '(based on business locations)', ha='center', fontsize=12)
fig.set_figheight(7)
fig.set_figwidth(7)

#### Add data ####
# Add the population data
ax1.bar(['2011', '2021'], [data_2011['population'], data_2021['population']])
ax1.set_title('Population')

# add the income data
ax2.bar(['2011', '2021'], [data_2011['income'], data_2021['income']])
ax2.set_title('Income')

# Add the working age population data
ax3.bar(['2011', '2021'], [data_2011['working_age_population'], data_2021['working_age_population']])
ax3.set_title('Working Age Population')

# Give some padding for the dubplots 
plt.subplots_adjust(hspace=0.5, top=0.85)

### Showing/saving the plot ###
print("showing plot...")
plt.savefig("../population_income_working_laborsize.png")
plt.show()
print("shown and saved plot!")
