import os
doc_list = []
data_path_root = ('./data/')
data_path = os.listdir(data_path_root)

"""
    TF term frequency in one text


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
    """
    
    """
    def __init__(self):
        pass

    reader = FileReader()

    for i in reader.doc_generator():
        print(i)