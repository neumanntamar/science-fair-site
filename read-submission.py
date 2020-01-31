import csv
import os
import datetime
import json

csvFilePath = 'testSubmission.csv'
jsonFilePath = 'data/test.json'

data = {}
with open(csvFilePath, mode="r", encoding="utf-8-sig") as csvFile:
    csvReader = csv.DictReader(csvFile)
    for csvRow in csvReader:
        id = csvRow['id']
        data[id] = csvRow

with open(jsonFilePath, 'w') as jsonFile:
    jsonFile.write(json.dumps(data['1'], indent=4))

os.system("hugo new --kind authors authors/test")