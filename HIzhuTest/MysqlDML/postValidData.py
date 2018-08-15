#coding:utf-8
import sys
sys.path.append('..')
from utils.mysqlConnector import MysqlC
from config import *
db = DATABASE_PARAM
class GetTestData(object):


    def __init__(self,mobile=None):
        self.gaodudataModel =  MysqlC(db['host'],db['port'],db['username'],db['password'],db['databaseName'][0])
        self.gaoduModel = MysqlC(db['host'],db['port'],db['username'],db['password'],db['databaseName'][1])
        try:
            self.UserId = self.gaodudataModel.execQuery("select id from customer where mobile=%s" % mobile)[0][0]
        except IndexError as e:
            self.UserId = None
    #根据手机号获取用户发的帖子数据
    def getPostListByMobile(self,way):
        if way == 'len':
            postLength = self.gaoduModel.execQuery("select count(*) from circlepost where customer_id='%s' and record_status=1"%self.UserId)[0][0]
            return postLength
        elif way == 'ids':
            post_ids = self.gaoduModel.execQuery("select id from circlepost where customer_id='%s' and record_status=1" % self.UserId)
            return post_ids

    def getPostDetailInfo(self,keyWord):
        post_detail = self.gaoduModel.execQuery("select money,`describe`,title,address from circlepost where customer_id='%s' and record_status=1 and title='%s'" % (self.UserId,keyWord))[0]
        return post_detail

    def getReportData(self,postId):
        report_data = self.gaoduModel.execQuery("SELECT content FROM circlepostreport WHERE customer_id = '%s' AND post_id = '%s'"%(self.UserId,postId))[0][0]
        return report_data


if __name__ == "__main__":
    # test = GetTestData('13974030833').UserId
    # print test
    pass
    # print test.getPostDetailInfo(u'找房就送车，金地自在城')[2]
