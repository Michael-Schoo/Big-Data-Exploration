
# open ./data/ABNs.csv
import csv
import time 


with open('./data/ABNs.csv', 'r') as csvfile:
    start_time = time.time()
    reader = csv.DictReader(csvfile)
    data = [row for row in reader]
    print("Read/open csv in ", time.time()-start_time, " seconds")

    print(data[0])
    print(len(data))

    # remove rows with no state
    # filter(lambda row: row['AddressState'] != '', data)
    start_time = time.time()
    data = [data for data in data if data['AddressState'] != '']

    # aaa = 0
    # for row in data:
    #     if row['AddressState'] == '':
    #         data.remove(row)
        # elif (row['GSTStatusFromDate'] == '19000101'):
        #     data.remove(row)
        #     aaa +=1
        #     if (aaa % 100_000): print("removed")

    print(len(data))
    # reduce it by 5%
    data = data[::20]
    print("Reduced data in ", time.time()-start_time, " seconds")
    print(len(data))

    # save data to csv
    with open('../Analyze_Data/data/ABNs.csv', 'w', newline='') as csvfile:
        start_time = time.time()
        writer = csv.DictWriter(csvfile, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
        print("Saved to csv in ", time.time()-start_time, " seconds")
