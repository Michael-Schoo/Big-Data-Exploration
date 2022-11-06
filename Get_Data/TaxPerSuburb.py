import csv
import pandas as pd

# Open the excel file
df = pd.read_excel('./data/ts20individual08medianaveragetaxableincomestateterritorypostcode.xlsx', sheet_name='Table 8')
data = df.to_csv()

# Remove first 27 lines from data
data = data.split('\n', 27)[27]

csv_columns = [
    'state',
    'postcode',
    'individuals_2003-04',
    'median_taxable_income_2003-04',
    'average_taxable_income_2003-04',
    # 'individuals_2004-05',
    # 'median_taxable_income_2004-05',
    # 'average_taxable_income_2004-05',
    # 'individuals_2005-06',
    # 'median_taxable_income_2005-06',
    # 'average_taxable_income_2005-06',
    # 'individuals_2006-07',
    # 'median_taxable_income_2006-07',
    # 'average_taxable_income_2006-07',
    # 'individuals_2007-08',
    # 'median_taxable_income_2007-08',
    # 'average_taxable_income_2007-08',
    # 'individuals_2008-09',
    # 'median_taxable_income_2008-09',
    # 'average_taxable_income_2008-09',
    # 'individuals_2009-10',
    # 'median_taxable_income_2009-10',
    # 'average_taxable_income_2009-10',
    # 'individuals_2010-11',
    # 'median_taxable_income_2010-11',
    # 'average_taxable_income_2010-11',
    # 'individuals_2011-12',
    # 'median_taxable_income_2011-12',
    # 'average_taxable_income_2011-12',
    # 'individuals_2012-13',
    # 'median_taxable_income_2012-13',
    # 'average_taxable_income_2012-13',
    'individuals_2013-14',
    'median_taxable_income_2013-14',
    'average_taxable_income_2013-14',
    'individuals_2014-15',
    'median_taxable_income_2014-15',
    'average_taxable_income_2014-15',
    'individuals_2015-16',
    'median_taxable_income_2015-16',
    'average_taxable_income_2015-16',
    'individuals_2016-17',
    'median_taxable_income_2016-17',
    'average_taxable_income_2016-17',
    'individuals_2017-18',
    'median_taxable_income_2017-18',
    'average_taxable_income_2017-18',
    'individuals_2018-19',
    'median_taxable_income_2018-19',
    'average_taxable_income_2018-19',
    'individuals_2019-20',
    'median_taxable_income_2019-20',
    'average_taxable_income_2019-20',
]

# Open the file that will be used to export data
with open('../Clean_and_Reduce_Data/data/TaxPerSuburb.csv', 'w', newline='') as csvfile:
    # Export writer
    writer = csv.writer(csvfile)
    writer.writerow(csv_columns)

    # Go through every line of excel exported
    for row in data.split('\n'):
        # Split it by ','
        add = row.split(",")
        
        # Remove first entry
        add.pop(0)

        # If there isn't anything, then  don't add
        if not len(add): continue

        # Go through each entry, anr replace things that don't need to exist
        new_row = []
        for i in add: 
            new_row.append(i.replace('\\r', '').replace('\r', '').replace('na', ''))

        # Write the row
        writer.writerow(new_row)
