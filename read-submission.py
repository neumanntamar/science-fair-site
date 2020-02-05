import csv
import os
import json

csvFilePath = 'testSubmission.csv'
jsonFilePath = 'data/submission.json'

data = {}
with open(csvFilePath, mode="r", encoding="utf-8-sig") as csvFile:
    csvReader = csv.DictReader(csvFile)
    for csvRow in csvReader:
        id = csvRow['author']
        data[id] = csvRow

        with open(jsonFilePath, 'w') as jsonFile:
            jsonFile.write(json.dumps(data[id], indent=4))

        authorName = csvRow['author'].replace(' ','_').lower()
        os.system('hugo new --kind authors authors/' + authorName)
