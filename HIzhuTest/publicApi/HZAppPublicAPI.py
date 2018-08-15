#coding:utf-8

import requests,sys
sys.path.append(r"..")
from publicParameter import header,clientKey
from utils.RSA import Encrypt
from config import *
import json
def login(mobile):
    verCode = 180205
    url = BASE_URL+"/customer/login.html"
    c = """-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDDYagHoYrjcdl8cCxpEBO2eyGs
Feu44/atWuReFXhwl/EHqqTOfRna5HR56xv/R99Mt2zNFuig8spEoWlJkRv5Eg1M
CNvvAQKFFjlKReYhqgZ2g2yZCi7vLDVDqfg+BQKK+He45M7Jl9YRT1RS4SysNARJ
rPcyCk/GSaCsZkNJiwIDAQAB
-----END PUBLIC KEY-----"""
    headers = header
    baseStr = Encrypt(c,mobile)
    SessionId = requests.post(url=url,headers=headers,data=json.dumps({"phoneNumber":baseStr,"verCode":verCode}))
    return SessionId


class HZAppAPI(object):
    def __init__(self,mobile):
        self.base_url = BASE_URL
        _header = header
        try:
            _header["Session"] = login(mobile).json()['data']['session']
        except KeyError as e:
            _header["Session"] = None
        self.header = _header

    @staticmethod
    def getImageData(imageUrl):
        with open(imageUrl, "rb") as fo:
            filedata = fo.read()
            import base64
            b64file = base64.b64encode(filedata)
        import os
        filesize = os.path.getsize(imageUrl)
        return [b64file,filesize]


    def postList(self,data):

        '''帖子列表'''
        url = self.base_url + '/v2/circle/post/list.html'
        Postlist = requests.post(url=url,data=json.dumps(data),headers=self.header)
        return Postlist

    def createPost(self,data):

        '''创建帖子'''
        url = self.base_url + '/v1/circle/post/create.html'
        Createpost = requests.post(url=url,data=json.dumps(data),headers=self.header)
        return Createpost

    def postDetail(self,data):
        '''帖子详情'''
        url = self.base_url + '/v1/circle/post/detail.html'
        postDetail = requests.get(url=url,data=json.dumps(data),headers=self.header)
        return postDetail

    def postReplayList(self,data):
        '''帖子回复列表'''
        url = self.base_url + '/v2/circle/post/replaylist.html'
        Postreplaylist = requests.get(url=url,data=json.dumps(data),headers=self.header)
        return Postreplaylist

    def reportMainPost(self,data):

        '''举报帖子'''
        url = self.base_url + '/circle/post/report.html'
        ReportMainPost = requests.get(url=url,data=json.dumps(data),headers=self.header)
        return ReportMainPost

    def reportReplayPost(self,data):
        '''举报回复的帖子'''
        url = self.base_url + '/circle/post/reportreplay.html'
        ReportReplayPost = requests.get(url=url,data=json.dumps(data),headers=self.header)
        return ReportReplayPost

    def myReplaylist(self,data):
        '''他人回复我的帖子'''
        url = self.base_url + '/v2/circle/post/myreplaylist.html'
        MyReplaylist = requests.get(url=url,data=json.dumps(data),headers=self.header)
        return MyReplaylist

    def postReplay(self,data):
        '''回复帖子'''
        url = self.base_url + '/v4/circle/post/replay.html'
        postReplay = requests.get(url=url,data=json.dumps(data),headers=self.header)
        return postReplay

    def customerInfo(self,data):
        '''租客信息'''
        url = self.base_url + '/customer/viewinfo.html'
        CustomerInfo = requests.get(url=url,data=json.dumps(data),headers=self.header)
        return CustomerInfo

    def messageImgUpload(self,data):
        '''话题图片上传'''
        url = r"http://testimg.loulifang.com.cn/imgapi/circle/topic/app/upload"
        import hashlib
        md5 = hashlib.md5("A100004CFAAA34"+"4.7"+"android").hexdigest()
        header = {"ClientVer": "4.7",
                  "androidId": "4ef07b5e-9f54-3635-8549-364318d7b3de",
                  "ScreenSize": "720x1280",
                  "Platform": "android",
                  "Session": "6b82c472-f1bf-02b7-f2e4-20fa73a7f636",
                  "Udid": "A100004CFAAA34",
                  "os_model": "GiONEE_GN5001S",
                  "uniqueId": "00000000-4823-726a-ffff-ffffcceaa262",
                  "OSVer": "android5.1",
                  "channel": "devoffline",
                  "md5": md5}
        MessageImgUpload = requests.post(url=url,data=json.dumps(data),headers=header)
        return MessageImgUpload

    def likeList(self,data):
        '''收藏的帖子列表'''
        url = self.base_url + '/circle/post/likelist.html'
        LikeList = requests.get(url=url,data=json.dumps(data),headers=self.header)
        return LikeList

    def cancelLike(self,data):
        '''取消收藏'''
        url = self.base_url + '/circle/post/like.html'
        CancelLike = requests.get(url=url,data=json.dumps(data),headers=self.header)
        return CancelLike

    def manyDeletePost(self,data):
        '''删除多个帖子'''
        url = self.base_url + '/v2/circle/post/delete.html'
        ManyDeletePost = requests.get(url=url,data=json.dumps(data),headers=self.header)
        return ManyDeletePost

    def singelDeletePost(self,data):
        '''单个帖子删除'''
        url = self.base_url + '/v1/circle/post/delete.html'
        SingelDeletePost = requests.get(url=url,data=json.dumps(data),headers=self.header)
        return SingelDeletePost

    def postAuthority(self):
        url = self.base_url + '/circle/post/create/power.html'
        unlike = requests.get(url=url,headers=self.header)

        return unlike

if __name__ == '__main__':
    post = HZAppAPI('15197029715')
    # print post.postList({
    #     "time":0,
    #     "limit":1,
    #     "sort":-1,
    #     "is_main":1
    # }).text

    # print post.createPost({"estate_names":"","address":"北外滩","has_room":2,"describe":"去去去","longitude":0,"money":0,"money_max":99999,"main_url":"https:\/\/testimg.loulifang.com.cn\/imgapi\/tie\/D0\/00\/D01152E92E4C224840988D6BBABFD3932400.jpg","money_min":0,"title":"QQ测试区","image_ids":["5C8A4BCF-2479-851A-494B-CDD33CEB3BB7"],"plate_ids":["89"],"latitude":0,"stand_ids":[]}).text
    # print post.postDetail({"post_id":"B804755B-A71A-0FA6-29B2-99B71039090D"}).text
    # print post.postReplayList({"post_id":"B804755B-A71A-0FA6-29B2-99B71039090D",
    #                            "time":0,
    #                            "limit":100,
    #                            "sort":-1,}).text
    # print post.reportMainPost({"post_id":"B54BBAD4-B29F-DE6A-A4BE-94A0716721BD","content":"测试举报"}).text
    # print post.reportReplayPost({"reply_id":"45F9BC42-0671-48FF-DDAB-E341B33869F4","content":"回复举报测试"}).text
    # print post.myReplaylist({"time":0,"limit":1,"sort":-1}).text
    # print post.postReplay({"post_id":"B804755B-A71A-0FA6-29B2-99B71039090D","reply_content":"嘿嘿嘿","reply_position":5,"parent_id":"","customer_id":"6b82c472-f1bf-02b7-f2e4-20fa73a7f636","is_private": 0}).text
    # print post.customerInfo({"customer_id":"6b82c472-f1bf-02b7-f2e4-20fa73a7f636"}).text
    # ImageData = HZAppAPI.getImageData()
    print post.messageImgUpload({"fileName":"4.png","fileSize":ImageData[1],"data":ImageData[0] ,"degree":0}).text
    #有问题
    # print post.likeList({"gender":0,"is_main":1,"limit":20,"money_max":99999,"money_min":0,"owner_id":"6d6f0bb6-383e-2c1d-4440-0a87de07f775","pageno":1,"plate_ids":[],"roomie_type":0,"sort":-1,"stand_ids":[],"time":0}).text
    # print post.cancelLike({"ids":["672F69E7-B8D8-5292-5862-74DA24EA73C1"],"is_collect":0}).text
    # print post.singelDeletePost({"post_id":"B804755B-A71A-0FA6-29B2-99B71039090D"}).text
    # print post.manyDeletePost({"post_ids":["5A579656-0CCE-ACF9-5BEA-8708854F1278"]}).text
    # print post.postAuthority().text