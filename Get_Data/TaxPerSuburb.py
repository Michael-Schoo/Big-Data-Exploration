import csv
import pandas as pd
df = pd.read_excel('./data/ts20individual08medianaveragetaxableincomestateterritorypostcode.xlsx', sheet_name='Table 8')
data = df.to_csv()

# remove first 27 lines from data
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

with open('../Clean_and_Reduce_Data/data/TaxPerSuburb.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(csv_columns)
    for row in data.split('\n'):
        add = row.split(",")
        add.pop(0)
        if not len(add): continue

        new_row = []
        for i in add:
            i=i.replace('\\r', '').replace('\r', '').replace('na', '')
            new_row.append(i)

        writer.writerow(new_row)


    