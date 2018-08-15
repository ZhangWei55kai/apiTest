#coding:utf-8
import requests,sys
sys.path.append(r"..")
from publicApi.HZAppPublicAPI import HZAppAPI
from MysqlDML.postValidData import GetTestData
from config import *
import readCsv

imageUrl = IMAGE_DATA
def getTestData(address=None,describe=None,main_url=None,title=None,image_ids=None,plate_ids=None,stand_ids=None,hasRoom=None,longitude=None,latitude=None):
    CreatePostData = {
        "estate_names": "",
        "address": address,
        "has_room": hasRoom,
        "describe": describe,
        "longitude": longitude,
        "money": 0,
        "money_max": 99999,
        "main_url": main_url,
        "money_min": 0,
        "title": title,
        "image_ids": image_ids.split(','),#list
        "plate_ids": plate_ids.split(','),#list
        "latitude": latitude,
        "stand_ids": stand_ids.split(',')#list
    }
    return CreatePostData

def getPostId(id):
    postId = {"post_id":id}
    return postId







def getReplyListData(id):
    listData = {"post_id": id,
     "time": 0,
     "limit": 100,
     "sort": -1, }
    return listData

def getReplyData(id,cusId,parent_id='',is_private=0):
    replyData = {"post_id": id,
                 "reply_content": u"嘿嘿嘿",
                 "reply_position": 5,
                 "parent_id": parent_id,
                 "customer_id": cusId,
                 "is_private": is_private}
    return replyData

def getReportMainData(id):
    replyData = {"post_id":id,"content":u"测试举报"}
    return replyData

def getReportReplyData(id):
    replyData = {"reply_id":id,"content":u"回复举报测试"}
    return replyData

def getImageData(ImageData):
    imgData = {"fileName":"4.png",
               "fileSize":ImageData[1],
               "data":ImageData[0] ,
               "degree":0}
    return imgData









if __name__ == "__main__":
    # postList = GetTestData()
    # print postList.getPostListByMobile('15197029715','len')
    pass

