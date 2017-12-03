from stanfordcorenlp import StanfordCoreNLP
from nltk import word_tokenize
from nltk import sent_tokenize
import numpy as np
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk import wordpunct_tokenize
import nltk
from nltk.tokenize import RegexpTokenizer

class getColumns:
    def __init__(self):
        self.lemmatize = WordNetLemmatizer()
        self.tokenizer = RegexpTokenizer(r'\w+')
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
    find the matching column by tokenizing and assigning number
    '''
    def findcol(self,question,columns):
        probable_columns = []

        for col in columns:
            tokens = self.tokenizer(tokens)
            temp = 0
            for token in tokens:
                print()
            #if()


    '''
    find the column which appears first in the sentence 
    with the help of pos tags
    '''
    def find_first_noun(self,columns, probable_columns, question):

        colum_with_number = {}
        for col in probable_columns:
            colum_with_number[col] = question.lower().find(col.lower())
        number = -1
        if len(colum_with_number) > 0:
            number = self.findcolum(columns, min(colum_with_number, key=colum_with_number.get))
        return number

    '''
    perform stemming and match the column
    '''
    def stemming_match(self,question,columns):
        new_question = ''
        new_columns = []
        stemmer = PorterStemmer()
        for words in word_tokenize(question):
            new_question +=stemmer.stem(words)
            new_question += ' '

        for column in columns:
            new_columns.append(stemmer.stem(column))

        return new_question,new_columns

    '''
    perform lemmatization and match the column
    '''

    def lemmatization_match(self, question, columns):
        new_question = ''
        new_columns = []

        for words in word_tokenize(question):
            new_question += self.lemmatize.lemmatize(words)
            new_question += ' '

        for column in columns:
            # if(question.lower().find(self.lemmatize.lemmatize(column)) != -1):
            new_columns.append(self.lemmatize.lemmatize(column))
        # if(len(new_columns) <= 0):
        #     new_columns.append('none')
        return new_question, new_columns



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
        # if len(probable_colum) == 1:
        #     find = self.findcolum(columns,probable_colum[0])
        # if find == -1:
        find = self.find_first_noun(columns,probable_colum,question)


        return find






    #
    # def find_first_noun(self,columns, probable_columns, postags):
    #     nouns = ['NN', 'NNS', 'NNP', 'NNPS', 'JJ', 'JJR', 'JJS']
    #     n = {}
    #     for i in range(len(postags)):
    #         if (postags[i][1] in nouns):
    #             n[i] = (postags[i][0])
    #
    #     col_noun = {}
    #     for col in probable_columns:
    #         if col in n.values():
    #             col_noun[col] = list(n.keys())[list(n.values()).index(col)]
    #
    #     # print('col_noun',col_noun)
    #     number = -1
    #     if len(col_noun) > 0:
    #         number = self.findcolum(columns,min(col_noun, key=col_noun.get))
    #     return number