import csv
import sys
import xmltodict
import time

# The columns of the csv file
csv_columns = [
    'ABN',
    'ABNStatusFromDate',
    'EntityTypeText',
    'EntityTypeInd',
    'NonIndividualName',
    'AddressState',
    'AddressPostcode',
    'ASICNumber',
    'GSTStatus',
    'GSTStatusFromDate'
]

# The function that is used to convert the xsv to a csv
def xml_to_csv(xml_file, csv_file):

    # Open the xml file 
    with open(sys.path[0]+xml_file) as fd:
        # Read file, and show how long it took
        read = fd.read()
        print("Read file")
        read_time = time.time()

        # Parse the xml
        doc = xmltodict.parse(read)
        parse_time = time.time()

        print("Parsed file in ", parse_time-read_time, " seconds")

    # Make a csv file with a similar name
    with open(csv_file, 'w', newline='') as csvfile:
        # Delete contents of file
        csvfile.truncate(0)
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()

        # Save each row
        amount_of_entries, kept_entries = 0,0
        for data in doc['Transfer']['ABR']:

            amount_of_entries+=1
            # Check that the MainEntity and ASICNumber is still in data
            if (not data.get('MainEntity')): continue
            if (not data.get('ASICNumber')): continue
            kept_entries+=1

            # Make the dict that is used for csv
            new_dict = {
                "ABN": data['ABN']['#text'],
                "ABNStatusFromDate": data['ABN']['@ABNStatusFromDate'],
                "EntityTypeText": data['EntityType']['EntityTypeText'],
                "EntityTypeInd": data['EntityType']['EntityTypeInd'],
                "NonIndividualName": data['MainEntity']['NonIndividualName']['NonIndividualNameText'],
                "AddressState": data['MainEntity']['BusinessAddress']['AddressDetails']['State'],
                "AddressPostcode": data['MainEntity']['BusinessAddress']['AddressDetails']['Postcode'],
                "ASICNumber": data['ASICNumber']['#text'],
                "GSTStatus": data['GST']['@status'],
                "GSTStatusFromDate": data['GST']['@GSTStatusFromDate'],
            }
            
            # Write the row
            writer.writerow(new_dict)
        
        # Print the amount of entries that were kept
        print(f"{kept_entries}/{amount_of_entries}")
        csv_time = time.time()
        print("Saved to csv in ", csv_time-parse_time, " seconds")

xml_files = [
    './data/public_split_1_10/20221102_Public01.xml',
    './data/public_split_1_10/20221102_Public02.xml',
    './data/public_split_1_10/20221102_Public03.xml',
    './data/public_split_1_10/20221102_Public04.xml',
    './data/public_split_1_10/20221102_Public05.xml',
    './data/public_split_1_10/20221102_Public06.xml',
    './data/public_split_1_10/20221102_Public07.xml',
    './data/public_split_1_10/20221102_Public08.xml',
    './data/public_split_1_10/20221102_Public09.xml',
    './data/public_split_1_10/20221102_Public10.xml',
    './data/public_split_11_20/20221102_Public11.xml',
    './data/public_split_11_20/20221102_Public12.xml',
    './data/public_split_11_20/20221102_Public13.xml',
    './data/public_split_11_20/20221102_Public14.xml',
    './data/public_split_11_20/20221102_Public15.xml',
    './data/public_split_11_20/20221102_Public16.xml',
    './data/public_split_11_20/20221102_Public17.xml',
    './data/public_split_11_20/20221102_Public18.xml',
    './data/public_split_11_20/20221102_Public19.xml',
    './data/public_split_11_20/20221102_Public20.xml',
]

def main():
    # Ask wether the file should really be run
    print("note: this file takes a while to run (for my computer it was ~30mins)")
    if input("Are you sure you want to run this? (y/n): ") != "y":
        return

    # Convert the xml to the new csv file
    for xml_file in xml_files:
        # Make the csv name by replacing the xml with csv
        csv_file = xml_file.replace('.xml', '.csv')
        xml_to_csv(xml_file, csv_file)
    
    # Read the many csv files and add it to data
    data = []
    csv_files = [xml_file.replace('.xml', '.csv') for xml_file in xml_files]
    for csv_file in csv_files:
        # Open csv file
        with open(csv_file, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            # Add each row to data
            for row in reader: data.append(row)

    # Print size of data (amount of entries)
    print(len(data))

    # Save data to csv
    with open('../Clean_and_Reduce_Data/data/ABNs.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        writer.writerows(data)

main()
