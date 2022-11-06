import csv
import matplotlib.pyplot as plt
import numpy as np

# table
# unique postcodes
# pie chart

# Get the ABNs
abns = [row for row in csv.DictReader(open('./data/ABNs.csv', 'r'))]

# Get the amount of ABNs per postcode
postcodes = {}
for code in abns:
    # Use the dict to increment the count
    postcodes[code['AddressPostcode']] = postcodes.get(code['AddressPostcode'], 0) + 1

# Only consider postcodes with more than 500 ABNs
# and join all the postcodes with less than 500 ABNs into one
# postcode called 'Other'
other = 0
other_amount = 0
postcodes_amount = len(postcodes)
# Go through each postcode, and check the amount ofd entries
for key in list(postcodes.keys()):
    # If less than 500, remove from list and add to another list 
    if postcodes[key] < 500:
        other += postcodes[key]
        other_amount += 1
        del postcodes[key]

# Add the other category to pie char (not using anymore)
# postcodes['Other'] = other

#### Set up Matplotlib ####

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
sorted_postcodes = sorted(postcodes.items(), key=lambda x: x[1], reverse=True)
labels = [x[0] for x in sorted_postcodes]
sizes = [x[1] for x in sorted_postcodes]
explode = [0.1 for i in range(len(postcodes))]
# only "explode" the 2nd slice (i.e. 'Hogs')

# Make figure and set its metadata (title, subtitle, and dimensions)
plt.figure('Unique Postcodes (with more than 500 ABNs)', figsize=(8, 7))
plt.suptitle("Unique Postcodes (with more than 500 ABNs)", y=0.965, fontweight="bold", fontsize=16)
plt.text(0, -1.5, f'Total number of unique postcodes shown: {len(postcodes)}/{postcodes_amount}')

# Add pie chart from data
plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

### Showing/saving the plot ###
print("showing plot...")
plt.savefig("../unique_postcodes.png")
plt.show()
print("shown and saved plot!")
