import numpy as np
import pandas as p
import jsonlines


colums = {}
with jsonlines.open('train.tables.jsonl') as table_file:
    for obj in table_file:
        colums[obj['id']] = obj['header']

print('length',len(colums))
print(colums['2-11365848-1'])

tables = dict()
with jsonlines.open('train.jsonl') as data_file:
    for obj in data_file:
        # print(obj)
        if obj['table_id'] not in tables.keys():
            question = []
            question.append(obj['question'])
            tables[obj['table_id']] = question
        else:
            tables[obj['table_id']].append(obj['question'])

print(tables['2-11365848-1'])


for table in tables:
    print('table',table)
    for question in tables[table]:
        print('question',(question))
        print('columns',colums[table])