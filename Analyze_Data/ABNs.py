import csv
import time
import matplotlib.pyplot as plt

csv_columns = [
    'ABN',
    'EntityTypeText',
    'EntityTypeInd',
    'NonIndividualName',
    'AddressState',
    'AddressPostcode',
    'ASICNumber',
    'GSTStatus',
    'GSTStatusFromDate'
]


csvfile = open('./data/ABNs.csv', 'r')
reader = csv.DictReader(csvfile)
data = [row for row in reader]
print(len(data))


#### Set up Matplotlib ####
plt.figure(figsize=(7, 7))
plt.suptitle("ABNs", y=0.965, fontweight="bold", fontsize=16)


# set basic data
plt.title("ABNs")
plt.ylabel("Postcode")

# add first data (Brisbane - BOM)
plt.plot([d.get('AddressPostcode') for d in data])
plt.tick_params(colors="C0", axis="x")

# add legend & other basic data
plt.xlabel("Postcode")

### Showing/saving the plot ###
print("showing plot...")
# plt.savefig("current_graph.png")
plt.show()
print("shown and saved plot!")


csvfile.close()
