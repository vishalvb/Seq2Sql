import numpy as np
import pandas as p
import jsonlines
from seq2sql import getColumn

table_colums = {}
with jsonlines.open('train.tables.jsonl') as table_file:
    for obj in table_file:
        table_colums[obj['id']] = obj['header']

print('length',len(table_colums))
print(table_colums['2-11365848-1'])

que_table = {}
with jsonlines.open('train.jsonl') as data_file:
    for obj in data_file:
        que_table[obj['question'].strip()] = obj['table_id']

print('len',len(que_table))

print(table_colums[que_table['Which report is names Thuin Circuit and is dated June 10?']])


result = []
getc = getColumn.getColumns()

for question in que_table.keys():
    col_number = getc.predictCol(question= question,columns=table_colums[que_table[question.strip()]])
    result.append(col_number)
    if(col_number == -1):
        print('not found',question, table_colums[que_table[question.strip()]])

print('result len',len(result),result)
col_number = []
with jsonlines.open('train.jsonl') as table_file:
    for obj in table_file:
        col_number.append(obj["sql"]["sel"])

count = 0
for k in range(len(que_table)):
    if result[k] == col_number[k]:
        count += 1

print('count',count)



# tables = dict()
# with jsonlines.open('train.jsonl') as data_file:
#     for obj in data_file:
#         if obj['table_id'] not in tables.keys():
#             question = []
#             question.append(obj['question'])
#             tables[obj['table_id']] = question
#         else:
#             tables[obj['table_id']].append(obj['question'])
#
# print(tables['2-11365848-1'])
#
# j = 0
# columnumbers = [0]*61297
# for table in tables:
#     print('table',table)
#     for question in tables[table]:
#         # print('question',(question[0]))
#         # print('columns',colums[table])
#         j += 1
#         print('question',(question))
#         print('columns',colums[table])
#         print('Prediction = ',getColumn.getColumns().predictCol(question,colums[table]))
#
#






    #
    # for question in tables[table]:
    #     # print('question',(question[0]))
    #     # print('columns',colums[table])
    #     if(question.lower().find('what') != -1):
    #         j += 1
    #         print('question',(question))
    #         print('columns',colums[table])
    #         print('Prediction = ',getColumn.getColumns().predictCol(question,colums[table]))
    #     if (j == 15):
    #         exit(0)
