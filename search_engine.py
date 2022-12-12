import os
import jieba
from collections import defaultdict
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
        self.word_count = defaultdict(int)
        jieba.enable_parallel(4) # enable parallelism for tokenize

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
    """

    def __init__(self,):
        pass
    



# with open("./stopword/stopwords.txt",'r') as file:
#     stopwords = file.read()
#     stopwords = stopwords.split("\n")



# import time
# jieba.enable_parallel(4)
# t1 = time.time()
# f = FileReader()
# for i in f.doc_generator():
#     list(jieba.cut(i))
# t2 = time.time()
# print(t2-t1)
