
import csv

csv_columns = [
    'year',
    'postcode',
    'total_population',
    'median_total_personal_income_weekly',
    'median_total_family_income_weekly',
    'labor_force',
]


with open('../Clean_and_Reduce_Data/data/Census.csv', 'w', newline='') as csvfile:

    data = []

    data2 = {}

    census_2011_b01_reader = open('./data/2011_BCP_POA_for_AUST_short-header/2011 Census BCP Postal Areas for AUST/AUST/2011Census_B01_AUST_POA_short.csv', 'r')
    reader_a = csv.DictReader(census_2011_b01_reader)
    census_2011_b01 = [row for row in reader_a]

    census_2021_g01_reader = open('./data/2021_GCP_POA_for_AUS_short-header/2021 Census GCP Postal Areas for AUS/2021Census_G01_AUST_POA.csv', 'r')
    reader_b = csv.DictReader(census_2021_g01_reader)
    census_2021_g01 = [row for row in reader_b]

    for row in census_2011_b01:
        index = (2011, row['region_id'].removeprefix('POA'))
        data2[index] = {}
        data2[index]['total_population'] = row['Tot_P_P']

    
    for row in census_2021_g01:
        index = (2021, row['POA_CODE_2021'].removeprefix('POA'))
        data2[index] = {}
        data2[index]['total_population'] = row['Tot_P_P']


    # Income 2011
    census_2011_b02_reader = open('./data/2011_BCP_POA_for_AUST_short-header/2011 Census BCP Postal Areas for AUST/AUST/2011Census_B02_AUST_POA_short.csv', 'r')
    for row in csv.DictReader(census_2011_b02_reader):
        index = (2011, row['region_id'].removeprefix('POA'))
        data2[index]['median_total_personal_income_weekly'] = row['Median_Tot_prsnl_inc_weekly']
        data2[index]['median_total_family_income_weekly'] = row['Median_Tot_fam_inc_weekly']
    
    # Income 2021
    census_2011_g02_reader = open('./data/2021_GCP_POA_for_AUS_short-header/2021 Census GCP Postal Areas for AUS/2021Census_G02_AUST_POA.csv', 'r')
    for row in csv.DictReader(census_2011_g02_reader):
        index = (2021, row['POA_CODE_2021'].removeprefix('POA'))
        data2[index]['median_total_personal_income_weekly'] = row['Median_tot_prsnl_inc_weekly']
        data2[index]['median_total_family_income_weekly'] = row['Median_tot_fam_inc_weekly']

    # Labor Force 2011
    census_2011_b37_reader = open('./data/2011_BCP_POA_for_AUST_short-header/2011 Census BCP Postal Areas for AUST/AUST/2011Census_B37_AUST_POA_short.csv', 'r')
    for row in csv.DictReader(census_2011_b37_reader):
        index = (2011, row['region_id'].removeprefix('POA'))
        data2[index]['labor_force'] = row['lfs_N_the_labour_force_P']

    # Labor Force 2021
    census_2021_g37_reader = open('./data/2021_GCP_POA_for_AUS_short-header/2021 Census GCP Postal Areas for AUS/2021Census_G60B_AUST_POA.csv', 'r')
    for row in csv.DictReader(census_2021_g37_reader):
        index = (2021, row['POA_CODE_2021'].removeprefix('POA'))
        data2[index]['labor_force'] = row['P_Tot_Tot']

    for key, value in data2.items():
        data.append({
            'year': key[0],
            'postcode': key[1],
            'total_population': value['total_population'],
            'median_total_personal_income_weekly': value['median_total_personal_income_weekly'],
            'median_total_family_income_weekly': value['median_total_family_income_weekly'],
            'labor_force': value['labor_force'],
        })


    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
    writer.writeheader()
    writer.writerows(data)


# b2 Median_total_personal_income_weekly,Median_rent_weekly,Median_total_family_income_weekly
