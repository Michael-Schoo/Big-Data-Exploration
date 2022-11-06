import csv
import matplotlib.pyplot as plt
import numpy as np

# table
# unique postcodes
# pie chart


abns = [row for row in csv.DictReader(open('./data/ABNs.csv', 'r'))]
print(len(abns))


# get the amount of ABNs per postcode
postcodes = {}
for code in abns:
    postcodes[code['AddressPostcode']] = postcodes.get(
        code['AddressPostcode'], 0) + 1

# only consider postcodes with more than 500 ABNs
# and join all the postcodes with less than 500 ABNs into one
# postcode called 'Other'
other = 0
other_amount = 0
postcodes_amount = len(postcodes)
for key in list(postcodes.keys()):
    if postcodes[key] < 500:
        other += postcodes[key]
        other_amount += 1
        del postcodes[key]
# postcodes['Other'] = other


# print(postcodes)

#### Set up Matplotlib ####

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
sorted_postcodes = sorted(postcodes.items(), key=lambda x: x[1], reverse=True)
labels = [x[0] for x in sorted_postcodes]
sizes = [x[1] for x in sorted_postcodes]
explode = [0.1 for i in range(len(postcodes))]
# only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.title('Unique Postcodes (with more than 500 ABNs)')
plt.text(0, -1.5, f'Total number of unique postcodes shown: {len(postcodes)}/{postcodes_amount}')

### Showing/saving the plot ###
print("showing plot...")
plt.savefig("../unique_postcodes.png")
plt.show()
print("shown and saved plot!")
