# -*- coding: utf-8 -*-
import numpy as np
import jsonlines
from pprint import pprint
from stanfordcorenlp import StanfordCoreNLP
from nltk import word_tokenize
from nltk import pos_tag
from nltk import parse
import collections
import nltk
from langdetect import detect
# nltk.download()


count = 0
questions ={}
with jsonlines.open('train.jsonl') as data_file:
    for obj in data_file:
        count += 1
        questions[obj['table_id']] = obj['question']
print(len(questions))
print('count = ',count)

colums = {}
with jsonlines.open('train.tables.jsonl') as table_file:
    for obj in table_file:
        colums[obj['id']] = obj['header']


queColumn = {}
for key in (questions.keys()):
    if key in questions: queColumn.setdefault(key, []).append(questions[key])
    if key in colums: queColumn.setdefault(key, []).append(colums[key])


howMany = {}
sum = 0
queryType = {}

for key in queColumn:
    question = word_tokenize(queColumn[key][0])
    if question[0].lower() not in queryType:
        queryType[question[0].lower()] = 1
    else:
        queryType[question[0].lower()] = queryType[question[0].lower()] +1
    if(question[0] == 'How' and question[1] == 'many'):
        # print(question)
        howMany[key] = queColumn[key]
print('end')

import operator


print(sorted(queryType.items(),key = operator.itemgetter(1)))
print(sum)

top20howMany = {}


top20howMany = collections.Counter(howMany).most_common(20)
# print(top20howMany)
newdict = {}
for obj in top20howMany:
    newdict[obj[0]] = obj[1]
    # print(obj[1][0])


nlp = StanfordCoreNLP('http://corenlp.run', port=80)
tags = []
parse = []
dependency = []
for key in newdict.keys():
    tags.append((nlp.pos_tag(newdict[key][0])))
    parse.append(nlp.parse(newdict[key][0]))
    dependency.append((nlp.dependency_parse(newdict[key][0])))
print('tag')

# print(tags[1])
# print(parse[1])
# print(dependency[1])
# print(howMany['1-1037590-1'])

for i in range(len(tags)):
    print(tags[i])
    print(dependency[i])
    print('\n')

# file = open('parse.txt','w')

# for i in range(len(tags)):
#     file.write(str(tags[i]))
#     file.write(str(parse[i]))
#     file.write(str(dependency[i]))
#     file.write('\n')
# file.close()

