import csv
import json
file = csv.DictReader(open('original_hm.csv','r',encoding="utf8"))
output =[]
for each in file:
    row = {}
    row['hmid'] = each['hmid']
    row['hm'] = each['hm']
    row['reflection'] = each['reflection']
    row['wid'] = each['wid']
    # row['cleaned_hm'] = each['cleaned_hm']
    # row['modified'] = each['modified']
    # row['num_sentence'] = each['num_sentence']
    # row['ground_truth_category'] = each['ground_truth_category']
    # row['predicted_category'] = each['predicted_category']
    # row['MWE'] = each['MWE']
    output.append(row)

json.dump(output,open('original_hm.json','w'),indent=4,sort_keys=False)