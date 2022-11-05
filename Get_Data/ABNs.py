import csv
import sys
import xmltodict
import pprint
import json
# time start
import time

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
def xsv_to_dict(xml_file, csv_file):
    with open(sys.path[0]+xml_file) as fd:
        read = fd.read()
        print("Read file")
        read_time = time.time()
        doc = xmltodict.parse(read)
        parse_time = time.time()

        print("Parsed file in ", parse_time-read_time, " seconds")

    # save to csv
    # csv_columns = list_of_dicts[0].keys()
    with open(csv_file, 'w', newline='') as csvfile:
        csvfile.truncate(0)
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        # writer.writerows(list_of_dicts)

        # save
        # list_of_dicts = []
        a,b = 0,0
        for data in doc['Transfer']['ABR']:
            # print(data)
            # print(i)
            a+=1
            if (not data.get('MainEntity')):
                # print("No MainEntity")
                continue
            if (not data.get('ASICNumber')):
                # print("No ASICNumber")
                continue
            b+=1
            
            new_dict = {
                "ABN": data['ABN']['#text'],
                "EntityTypeText": data['EntityType']['EntityTypeText'],
                "EntityTypeInd": data['EntityType']['EntityTypeInd'],
                "NonIndividualName": data['MainEntity']['NonIndividualName']['NonIndividualNameText'],
                "AddressState": data['MainEntity']['BusinessAddress']['AddressDetails']['State'],
                "AddressPostcode": data['MainEntity']['BusinessAddress']['AddressDetails']['Postcode'],
                "ASICNumber": data['ASICNumber']['#text'],
                "GSTStatus": data['GST']['@status'],
                "GSTStatusFromDate": data['GST']['@GSTStatusFromDate'],
            }
            # break
            # list_of_dicts.append(new_dict)
            writer.writerow(new_dict)
        print(f"{b}/{a}")
        csv_time = time.time()
        print("Saved to csv in ", csv_time-parse_time, " seconds")
        # json.dump(list_of_dicts, file)

        print("saved")

xml_files = [
    './data/public_split_1_10/20221026_Public01.xml',
    './data/public_split_1_10/20221026_Public02.xml',
    './data/public_split_1_10/20221026_Public03.xml',
    './data/public_split_1_10/20221026_Public04.xml',
    './data/public_split_1_10/20221026_Public05.xml',
    './data/public_split_1_10/20221026_Public06.xml',
    './data/public_split_1_10/20221026_Public07.xml',
    './data/public_split_1_10/20221026_Public08.xml',
    './data/public_split_1_10/20221026_Public09.xml',
    './data/public_split_1_10/20221026_Public10.xml',
    './data/public_split_11_20/20221026_Public11.xml',
    './data/public_split_11_20/20221026_Public12.xml',
    './data/public_split_11_20/20221026_Public13.xml',
    './data/public_split_11_20/20221026_Public14.xml',
    './data/public_split_11_20/20221026_Public15.xml',
    './data/public_split_11_20/20221026_Public16.xml',
    './data/public_split_11_20/20221026_Public17.xml',
    './data/public_split_11_20/20221026_Public18.xml',
    './data/public_split_11_20/20221026_Public19.xml',
    './data/public_split_11_20/20221026_Public20.xml',
]

def main():
    csv_files = [xml_file.replace('.xml', '.csv') for xml_file in xml_files]
    for xml_file in xml_files:
        csv_file = xml_file.replace('.xml', '.csv')
        xsv_to_dict(xml_file, csv_file)
    
    data = []
    for csv_file in csv_files:
        # open csv file
        with open(csv_file, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data.append(row)
    print(data[0])
    print(len(data))

    # save data to csv
    with open('../Clean_and_Reduce_Data/data/ABNs.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        writer.writerows(data)

main()