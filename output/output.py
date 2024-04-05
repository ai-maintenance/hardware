'''
author: GAL ASHKENAZI
date:   04/04/2024
'''
import csv
import os
from dotenv import load_dotenv

load_dotenv()
PARENT_DIR = os.environ.get("PARENT_DIR")
LIMIT =  int(os.environ.get("LIMIT"))

'''
CSV OUTPUT 
'''
class CSV :
    def __init__(self, directory_name, header):
        print(f'@@@@@@@@@@@@@@@@@@ {LIMIT} @@@@@@@@@@@@@@@')
        self.header = ['id'] + header           # add 'id' column for header of csv file
        self.directory_name = directory_name    # folder name
        
        self.file_id = 0    # serial file id
        self.rec_id = 0     # serial recode id

        self.folder_path = self.createFolder()  # create a new folder for saving records files
        self.rec_file = self.createFile()       # create a new record file

    '''
    CTREATE NEW FOLDER
    '''
    def createFolder(self):
        path = os.path.join(PARENT_DIR, self.directory_name)   
        os.mkdir(path)

        return PARENT_DIR + '/' + self.directory_name   # return the new directory path

    '''
    CTREATE NEW FILE
    '''
    def createFile(self):
        csv_file = open(f'{self.folder_path}/{self.file_id}.csv', 'w', newline='')  # crete and open for write a new recording file
        rec_file = csv.writer(csv_file, delimiter=',',
                            quotechar=',', quoting=csv.QUOTE_MINIMAL)
        
        rec_file.writerow(self.header)  # write the header of csv file
        self.log(self.header)

        self.file_id += 1   # increase the serial file id for the next time

        return rec_file 

    '''
    WRITE A LINE OF RECORD
    '''
    def write(self, row):
        # create a new file if it contian over the limit of recordes
        if (self.rec_id % (LIMIT + 1)) >= LIMIT :              
            self.rec_file = self.createFile()

        # write a line of record and add the serial id
        self.rec_file.writerow([self.rec_id] + row) 
        self.log([self.rec_id] + row)

        self.rec_id += 1

    '''
    PRINT A LINE TO CONSOLE
    '''
    def log(self, o):
        for res in o:
            print(res, end='\t')

        print() # new line


'''
EXAMPLE
'''
# out = Output(directory_name='testFolder', header=['te', 'st'])
# out.write(["1","2"])
# out.write(["3","4"])