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
        yield file content 
        """
        for file_path in self.file_list:
            with open(file_path,'r') as file:
                yield file.read()

        
class Text(object):
    """class represent text
    
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


    

    


class TextLib:
    """library for Text object
    """
    pass






# import time
# jieba.enable_parallel(4)
# t1 = time.time()
# f = FileReader()
# for i in f.doc_generator():
#     list(jieba.cut(i))
# t2 = time.time()
# print(t2-t1)