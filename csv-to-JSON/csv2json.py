#!/usr/bin/env python
# coding: utf-8
import csv
import json
import pandas as pd

#fieldnames = ("F1","F2","F3","F4") #Assuming F4 is phonenum

csv_input = pd.read_csv('Customer_Details.csv',header=0)
csv_input.insert(20, 'Telephone_formatted',csv_input['Telephone'].astype(str).apply(lambda x: x[:3]+ '-'+x[3:6]+'-'+x[6:10]))
#csv_input['Phone_no']=csv_input['Telephone'].astype(str).apply(lambda x: x[:3]+ '-'+x[3:6]+'-'+x[6:10])
del csv_input['Telephone']
csv_input.columns = ['Telephone' if x=='Telephone_formatted' else x for x in csv_input.columns]
csv_input.to_csv('Customer_Details_formatted.csv', index=False)
#print(csv_input['Phone_no'])

# Another way to do the same thing
csv_input= csv_input.assign(Telephone = csv_input['Telephone'].astype(str).apply(lambda x: x[:3]+ '-'+x[3:6]+'-'+x[6:10]))
csv_input.to_csv('Customer_Details_formatted.csv', index=False)

# Finally, write the new csv to JSON
with open('Customer_Details_formatted.csv') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

with open('Customer_Details.json', 'w') as f:
    json.dump(rows, f)   

