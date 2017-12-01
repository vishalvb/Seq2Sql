from stanfordcorenlp import StanfordCoreNLP
from nltk import word_tokenize
from nltk import sent_tokenize
import numpy as np
from pycorenlp import StanfordCoreNLP

import nltk


class getColumns:
    def __init__(self):
        n = 1
        # # self.nlp = StanfordCoreNLP('http://corenlp.run', port=80)
        # self.nlp = StanfordCoreNLP('http://localhost:9000')


    def printNoun(self,postag):
        print('postag',postag)
        return 1

    '''find the number of the matching column'''
    def findcolum(self,columns,column):
        for i in range(len(columns)):
            if(columns[i].lower() == column.lower()):
                return i

    '''
    find the column which appears first in the sentence 
    with the help of pos tags
    '''
    def find_first_noun(self,columns, probable_columns, postags):
        nouns = ['NN', 'NNS', 'NNP', 'NNPS', 'JJ', 'JJR', 'JJS']
        n = {}
        for i in range(len(postags)):
            if (postags[i][1] in nouns):
                n[i] = (postags[i][0])

        col_noun = {}
        for col in probable_columns:
            if col in n.values():
                col_noun[col] = list(n.keys())[list(n.values()).index(col)]

        # print('col_noun',col_noun)
        number = -1
        if len(col_noun) > 0:
            number = self.findcolum(columns,min(col_noun, key=col_noun.get))
        return number

    '''
    predicts the column for the question
    '''
    def predictCol(self,question,columns):
        postag = nltk.pos_tag(word_tokenize(question))

        probable_colum = []
        for column in columns:
            if(question.lower().find(column.lower()) != -1):
                probable_colum.append(column.lower())

        find = -1
        if len(probable_colum) == 1:
            find = self.findcolum(columns,probable_colum[0])
        elif len(probable_colum) > 1:
            find = self.find_first_noun(columns,probable_colum,postag)

        return find
