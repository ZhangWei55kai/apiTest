#coding:utf-8

import csv
import testData
import sys
sys.path.append('..')
from config import *
def getTestDatabyCSV(url,model):
    data = []
    with open(url,model) as fp:
        reader = csv.reader(fp)
        for i in reader:
            data.append(i)
    return data


def getPostData(line):
    data = getTestDatabyCSV(TEST_DATA, 'r')[line]
    result = testData.getTestData(address=data[0],
                         describe=data[1],
                         main_url=data[2],
                         title=data[3],
                         image_ids=data[4],
                         plate_ids=data[5],
                         stand_ids=data[6],
                         hasRoom=data[7],
                         longitude=data[8],
                         latitude=data[9])
    return result
if __name__ == "__main__":
    print getTestDatabyCSV(r'D:\TestCode\HiZhuAPP\testData\postTestData.csv','r')