#coding:utf-8
import os
#数据库连接参数
DATABASE_PARAM = {
    "host":"120.27.162.0",
    "port":"3306",
    "username":"root",
    "password":"gdroot",
    "databaseName":["gaodudata",
                    "gaodu"]
}
FILE_URL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#测试地址
BASE_URL = r"http://testsh.loulifang.com.cn"
#测试数据的url
TEST_DATA = os.path.join(FILE_URL,'workspace','testData','postTestData.csv')
#本地测试变量
# TEST_DATA = FILE_URL+r"\HiZhuAPP\testData\postTestData.csv"
PATH = os.path.join(FILE_URL,'workspace','testData','TestImage')

UNIMAGE_DATA = os.path.join(PATH,'testFile.txt')

IMAGE_DATA = {'jpg':os.path.join(PATH,'2.jpg'),
              'jpeg':os.path.join(PATH,'3.jpeg'),
              'png':os.path.join(PATH,'4.png')}
#本地测试变量
# IMAGE_DATA = {'jpg':FILE_URL+r'\HiZhuAPP\testData\TestImage\2.jpg',
#               'jpeg':FILE_URL+r'\HiZhuAPP\testData\TestImage\3.jpeg',
#               'png':FILE_URL+r'\HiZhuAPP\testData\TestImage\4.png'}


