import csv, json

csvFilePath = "original_hm.csv"
jsonFilePath = "original_hm.json"

data ={}

with open(csvFilePath) as csvFile:
    csvReader = csv.DictReader(csvFile)
    for csvRow in csvReader:
        hmid = csvRow["hmid"]
    data[hmid] = csvRow
with open(jsonFilePath, "w") as jsonFile:
    jsonFile.write(jsonFile.dumps(data, indent= 4))