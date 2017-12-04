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
        self.stemmer = PorterStemmer()
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
            if(question.lower().find(col.lower()) != -1):
                colum_with_number[col] = question.lower().find(col.lower())
            else:
                colum_with_number[col] = 1000
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

        for words in word_tokenize(question):
            new_question +=self.stemmer.stem(words)
            new_question += ' '

        for column in columns:
            new_columns.append(self.stemmer.stem(column))

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
            new_columns.append(self.lemmatize.lemmatize(column))
        return new_question, new_columns



    '''
    predicts the column for the question
    '''
    def predictCol(self,question,columns):
        postag = nltk.pos_tag(word_tokenize(question))

        probable_colum = []

        #
        # temp_question = self.tokenizer.tokenize(question.lower())
        # lemma_question = []
        # for words in temp_question:
        #     lemma_question.append(self.lemmatize.lemmatize(words))
        # for words in temp_question:
        #     lemma_question.append(self.stemmer.stem(words))
        ##
        # for column in columns:
        #     # if(len(self.tokenizer(column)) == 1):
        #     #     if (question.lower().find(column.lower()) != -1):
        #     #         probable_colum.append(column.lower())
        #     # else:
        #     tokens = self.tokenizer.tokenize(column)
        #     for token in tokens:
        #         if (token.lower() in lemma_question):
        #             probable_colum.append(column)
        #             break

            # for token in tokens:
            #     if (question.lower().find(token.lower()) != -1):
            #         probable_colum.append(column)
            #         break

        #
        for column in columns:
            tokens = self.tokenizer.tokenize(column)
            if(len(tokens) == 1):
                if(question.lower().find(column.lower()) != -1):
                    probable_colum.append(column.lower())
            else:
                for token in tokens:
                    if (question.lower().find(token.lower()) != -1):
                        probable_colum.append(column.lower())
                        break
        find = -1
        # if len(probable_colum) == 1:
        #     find = self.findcolum(columns,probable_colum[0])
        # if find == -1:
        if(len(probable_colum) == 1):
            find = self.findcolum(columns,probable_colum[0])
        else:
            find = self.find_first_noun(columns,probable_colum,question)


        return find

    '''
    gets the agg operators
    '''
    def get_agg(self,question):
        agg_ops = ['', 'MAX', 'MIN', 'COUNT', 'SUM', 'AVG']
        agg_number = 0

        # if(question.lower().find('sum') != -1 or question.lower().find('total number') != -1 or question.lower().find('total') != -1):
        # if(question.lower().find('sum') != -1 and (question.lower().find('how many') != -1 or question.lower().find('total') != -1)):
        #     agg_number = 4
        # elif(question.lower().find('average') != -1):
        #     agg_number = 5
        # elif(question.lower().find('how many') != -1 or question.lower().find('total number') !=-1):
        #     agg_number = 3
        # elif(question.lower().find('maximum') != -1 or question.lower().find('max') != -1  or question.lower().find('highest') != -1):
        #     agg_number = 1
        # elif (question.lower().find('minimum') != -1 or question.lower().find('min') != -1 or question.lower().find('lowest') != -1):
        #     agg_number = 2

        max = ['max','maximum','greatest','highest','most','largest','latest','most recent','most','best','top','larger']
        min = ['minimum','lowest','smallest','earliest','least','fewest']


        for i in range(len(max)):
            if(max[i] in question.lower().split() and question.lower().find('average') == -1):
                agg_number = 1
                return agg_number

        for i in range(len(min)):
            if(min[i] in question.lower().split() and question.lower().find('average') == -1):
                agg_number = 2
                return agg_number


        if (question.lower().find('average') == -1 and (question.lower().find('sum') != -1  or question.lower().find('total') != -1 and question.lower().find('total number') == -1)):
            agg_number = 4
        elif (question.lower().find('average') != -1):
            agg_number = 5
        elif (question.lower().find('how many') != -1 or question.lower().find('total number') != -1):
            agg_number = 3
        return agg_number



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