import sys
import xmltodict
import pprint
import json

with open(sys.path[0]+'/data/public_split_1_10/20221026_Public01.xml') as fd:
    read = fd.read()
    print("Read file")
    doc = xmltodict.parse(read)
    print("Parsed file")

# pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(json.dumps(doc))

# Save to json (to test what it is parsed to)
with open(sys.path[0]+'/data/public_split_1_10/20221026_Public01.json', 'w', newline='') as file:
    # save
    json.dump(doc, file)
    print("saved")

#####################################
#### WILL MAKE IT INTO CSV LATER ####
#####################################

# with open('./data/public_split_1_10/20221026_Public01.better.json', 'w', newline='') as file:
#     # delete contents
#     file.truncate(0)
    
#     # save
#     list_of_dicts = []
#     for data in doc['Transfer']['ABR']:
#         new_dict = {
#             "ABN": data['ABN']['#text'],
#             "EntityTypeText": data['EntityType']['EntityTypeText'],
#             "EntityTypeText": data['EntityType']['EntityTypeText'],
#             "EntityTypeInd": data['EntityType']['EntityTypeInd'],
#             "NonIndividualName": data['MainEntry']['NonIndividualName']['NonIndividualNameText'],
#             "BusinessAddressDetails": {
#                 "State": data['MainEntry']['BusinessAddress']['AddressDetails']['State'],
#                 "Postcode": data['MainEntry']['BusinessAddress']['AddressDetails']['Postcode'],
#             },
#             "ASICNumber": data['ASICNumber']['#text'],
#             # "GST": data['GST']['#text'],
#         }
#         list_of_dicts.append(new_dict)
#     print("saving")
#     json.dump(list_of_dicts, file)


#     print("saved")
