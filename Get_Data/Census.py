import csv

# The columns of the csv file
csv_columns = [
    'year',
    'postcode',
    'total_population',
    'median_total_personal_income_weekly',
    'median_total_family_income_weekly',
    'labor_force',
]

#  Open the census csv file
with open('../Clean_and_Reduce_Data/data/Census.csv', 'w', newline='') as csvfile:

    # The dict for data keyed by year and postcode (eg (2011,'2620'))
    data_dict = {}

    # Population 2011 
    census_2011_b01_reader = open('./data/2011_BCP_POA_for_AUST_short-header/2011 Census BCP Postal Areas for AUST/AUST/2011Census_B01_AUST_POA_short.csv', 'r')
    for row in csv.DictReader(census_2011_b01_reader):
        index = (2011, row['region_id'].removeprefix('POA'))
        data_dict[index] = {}
        data_dict[index]['total_population'] = row['Tot_P_P']

    # Population 2021
    census_2021_g01_reader = open('./data/2021_GCP_POA_for_AUS_short-header/2021 Census GCP Postal Areas for AUS/2021Census_G01_AUST_POA.csv', 'r')
    for row in csv.DictReader(census_2021_g01_reader):
        index = (2021, row['POA_CODE_2021'].removeprefix('POA'))
        data_dict[index] = {}
        data_dict[index]['total_population'] = row['Tot_P_P']


    # Income 2011
    census_2011_b02_reader = open('./data/2011_BCP_POA_for_AUST_short-header/2011 Census BCP Postal Areas for AUST/AUST/2011Census_B02_AUST_POA_short.csv', 'r')
    for row in csv.DictReader(census_2011_b02_reader):
        index = (2011, row['region_id'].removeprefix('POA'))
        data_dict[index]['median_total_personal_income_weekly'] = row['Median_Tot_prsnl_inc_weekly']
        data_dict[index]['median_total_family_income_weekly'] = row['Median_Tot_fam_inc_weekly']
    
    # Income 2021
    census_2011_g02_reader = open('./data/2021_GCP_POA_for_AUS_short-header/2021 Census GCP Postal Areas for AUS/2021Census_G02_AUST_POA.csv', 'r')
    for row in csv.DictReader(census_2011_g02_reader):
        index = (2021, row['POA_CODE_2021'].removeprefix('POA'))
        data_dict[index]['median_total_personal_income_weekly'] = row['Median_tot_prsnl_inc_weekly']
        data_dict[index]['median_total_family_income_weekly'] = row['Median_tot_fam_inc_weekly']

    # Labor Force 2011
    census_2011_b37_reader = open('./data/2011_BCP_POA_for_AUST_short-header/2011 Census BCP Postal Areas for AUST/AUST/2011Census_B37_AUST_POA_short.csv', 'r')
    for row in csv.DictReader(census_2011_b37_reader):
        index = (2011, row['region_id'].removeprefix('POA'))
        data_dict[index]['labor_force'] = row['lfs_N_the_labour_force_P']

    # Labor Force 2021
    census_2021_g37_reader = open('./data/2021_GCP_POA_for_AUS_short-header/2021 Census GCP Postal Areas for AUS/2021Census_G60B_AUST_POA.csv', 'r')
    for row in csv.DictReader(census_2021_g37_reader):
        index = (2021, row['POA_CODE_2021'].removeprefix('POA'))
        data_dict[index]['labor_force'] = row['P_Tot_Tot']

    data = []
    # Go through the keyed dictionary, and make it a list
    for key, value in data_dict.items():
        data.append({
            'year': key[0],
            'postcode': key[1],
            'total_population': value['total_population'],
            'median_total_personal_income_weekly': value['median_total_personal_income_weekly'],
            'median_total_family_income_weekly': value['median_total_family_income_weekly'],
            'labor_force': value['labor_force'],
        })


    # Export the list to a new csv file
    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
    writer.writeheader()
    writer.writerows(data)
