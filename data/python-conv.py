import csv, json

csvFilePath = "cleaned_hm.csv"
jsonFilePath = "cleaned_hm.json"

data = {}

with open(csvFilePath) as csvFile:
    csvReader = csv.DictReader(csvFile)
    for csvRow in csvReader:
        hmid = csvRow["hmid"]
    data[hmid] = csvRow
with open(jsonFilePath, "w") as jsonFile:
    jsonFile.write(json.dumps(data, indent=4))