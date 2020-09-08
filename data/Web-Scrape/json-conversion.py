import csv
import json
file = csv.DictReader(open('books.csv','r',encoding="utf8"))
output =[]
for each in file:
    row = {}
    row['title'] = each['title']
    row['price'] = each['price']
    row['image_url'] = each['image_url']
    row['rating'] = each['rating']
    row['description'] = each['description']
# row['cleaned_hm'] = each['cleaned_hm']
    # row['modified'] = each['modified']
    # row['num_sentence'] = each['num_sentence']
    # row['ground_truth_category'] = each['ground_truth_category']
    # row['predicted_category'] = each['predicted_category']
    # row['MWE'] = each['MWE']
    output.append(row)

json.dump(output,open('books.json','w'),indent=4,sort_keys=False)