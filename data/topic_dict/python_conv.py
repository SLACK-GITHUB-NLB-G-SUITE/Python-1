import csv, json

csvFilePath = "pets-dict.csv"
jsonFilePath = "pets-dict.json"

data ={}

with open(csvFilePath) as csvFile:
    csvReader = csv.DictReader(csvFile)
    for csvRow in csvReader:
        CEO = csvRow["CEO"]
    data[CEO] = csvRow
with open(jsonFilePath, "w") as jsonFile:
    jsonFile.write(jsonFile.dumps())