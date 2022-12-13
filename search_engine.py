import os
import jieba
from collections import defaultdict
import scipy.sparse as sp
from tqdm import tqdm
import numpy as np
jieba.enable_parallel(4)  # enable parallelism for tokenize
"""
    TF:term frequency in one text
    IDF = N/df
    df:the number of documents in which term t occurs


"""

class FileReader(object):

    """Read file content

    Attributes:
    path: place where data stored
    file_list: file direction    
    """

    def __init__(self):
        self.path = "./data/"
        self.file_list = [os.path.join(self.path,file_name) for file_name in os.listdir(self.path)]

    def doc_generator(self):
        """
        yield file content and file name
        """
        for file_path in self.file_list:
            with open(file_path,'r') as file:
                file_name = os.path.split(file_path)[1]
                yield (file_name,file.read())

        
class Text(object):
    """class represent text
       
       Attributes:
       tokenize: list contains words from sentence after removing stopwords
       text: raw text read from file
       word_count: dict records term frequency

       Args:
       text
    """
    
    def __init__(self,text):
        self.text = text
        self.tokenize = []
        self.text_name = ""
        self.word_count = defaultdict(int)
       

    def text_tokenize(self):
        """tokenize text saving to self.tokenize
        """
        for i in jieba.cut(self.text):
            self.tokenize.append(i)

    def count_word(self):
        """count term frequency
        """
        for word in self.tokenize:
            self.word_count[word] += 1
    def set_name(self,name):
        """set text name from args
        """
        self.text_name = name

    def remove_stopword(self,stopword):
        """remove stop word from tokenize 
           args: stopword stopword load from Textlib class
        """

        self.tokenize = [word for word in self.tokenize if word not in stopword and word != "\n" and word != "\u3000"]
    
"""
vector space model
row is docmument
col is word
find data of the matrix by index
"""
    


class TextLib(object):
    """library for Text object

        Attributes:
        reader    
    """

    

    def __init__(self):
        self.reader = FileReader()
        self.text_lib = []
        self.stopwords = []
        self.vocabulary = {}

    def load_data(self):
        """load doc data from reader
        """
        for doc in self.reader.doc_generator():
            doc_name,doc_content = doc
            text = Text(doc_content)
            text.text_tokenize()
            text.remove_stopword(self.stopwords)
            text.set_name(doc_name)
            text.count_word()
            self.text_lib.append(text)
            
    def load_stopwords(self):
        with open("./stopword/stopwords.txt",'r') as file:
            stopwords = file.read()
            stopwords = stopwords.split("\n")
            self.stopwords = stopwords
     
    def build_vocabulary(self):
        word_index = 0
        for text in self.text_lib:
            for word in text.tokenize:
                if word not in self.vocabulary:
                    self.vocabulary[word] = word_index
                    word_index += 1
    def init_td_matrix(self):

        num_text = len(self.text_lib)
        num_word = len(self.vocabulary.keys())
        row = []
        col = []
        data = []
        for idx,text in tqdm(enumerate(self.text_lib)):
            for word in text.tokenize:
                row_idx = idx
                col_idx = self.vocabulary[word]
                word_count = text.word_count[word]
                row.append(row_idx)
                col.append(col_idx)
                data.append(word_count)
        row = np.array(row)
        col = np.array(col)
        data = np.array(data)
        tf_matrix = sp.coo_matrix((data,(row,col)),shape = (num_text,num_word))
        print(tf_matrix.todense())
                # if word in text.tokenize:
                #     dt_matrix[idx,word_idx] = text.word_count[word]
                # else:
                #     dt_matrix[idx,word_idx] = 0
        
lib = TextLib()
print("loading stopwords")
lib.load_stopwords()
print("loading data")
lib.load_data()
print("building vocabulary")
lib.build_vocabulary()
print("building matrix")
lib.init_td_matrix()



# import time
# jieba.enable_parallel(4)
# t1 = time.time()
# f = FileReader()
# for i in f.doc_generator():
#     list(jieba.cut(i))
# t2 = time.time()
# print(t2-t1)
