#coding:utf-8

import requests,sys
sys.path.append(r"..")
from MysqlDML.postValidData import GetTestData
from publicApi.HZAppPublicAPI import HZAppAPI
from testData import readCsv
from utils.logUtils import logger
def clearPostTestData(ids,mobile):
    if len(ids) > 0:
        testData = HZAppAPI(mobile)
        deleteResult = testData.manyDeletePost({"post_ids":ids})
        logger.info(deleteResult.text)
        if deleteResult.json()['status'] == '200':
            return True
        else:
            return False
    else:
        return True


def DeleteAllPost(mobile):
    postList = GetTestData(mobile)
    ids = []
    for i in postList.getPostListByMobile('ids'):
        ids.append(str(i[0]))
    try:
        result = clearPostTestData(ids,mobile)
        return result
    except Exception as e:
        return 'error',e,ids

def deleteAndCreatePost(mobile,line):
    post = HZAppAPI(mobile)
    deleteResult = DeleteAllPost(mobile)
    if deleteResult:
        createParam = readCsv.getPostData(line)
        postData = post.createPost(createParam)
        return [postData,createParam]
    else:
        return False


def compareJSON(firData,secData):
    firKey = [i for i in firData if i in ['money','describe','title','address']]
    for key in firKey:
        if str(secData['data'][key].encode('utf-8')) == str(firData[key]):
            return True
        else:
            return False
    return True


def compareDataBase(dbResult,JsonResult):
    JsonKey = [i for i in JsonResult if i in ['money', 'describe', 'title', 'address']]
    db_result = []
    for v in dbResult:
        if type(v) == float:
            db_result.append(int(v))
        else:
            db_result.append(v)
        for key in range(len(JsonKey)):
            if str(JsonResult[JsonKey[key]].encode('utf-8')) == str(db_result[key]):
                return True
            else:
                return False

def checkReportDatabase(raw_data,mobile,post_id):
    raw = raw_data
    db = GetTestData(mobile)
    dbData = db.getReportData(post_id)
    if raw == dbData:
        return True
    else:
        return False

def analysisReplyResult(raw_data,customerId):
    result = raw_data['data']
    for dt in result:
        for key in dt:
            if key == 'customer_id':
                if dt['customer_id'].upper() == customerId and dt['is_private'] == '1':
                    return True
                else:
                    return False
            else:
                continue



def anotherReply(data,mobile):
    post = HZAppAPI(mobile)
    replyR = post.postReplay(data)
    return replyR


def createPostAndReturn(self,createParam):
    createPost = self.post.createPost(createParam)
    self.assertEquals(createPost.json()['status'], '200', '创建帖子失败')
    createPostid = createPost.json()['data']['post_id']
    return createPostid




