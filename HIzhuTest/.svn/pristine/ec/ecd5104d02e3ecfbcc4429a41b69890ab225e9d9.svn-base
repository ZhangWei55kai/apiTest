# # -*- coding: utf-8 -*-
# # @Author: zhangwei
# # @Date:   2016-11-21 15:50:16
# # @Last Modified by:   zhangwei
# # @Last Modified time: 2016-11-29 16:13:20
# import pymssql

# class MSSQL(object):

# 	def __init__(self,host,user,pwd,db,port):
# 		self.host = host
# 		self.user = user
# 		self.pwd = pwd
# 		self.db = db
# 		self.port = port

# 	def __getConnect(self):
# 		if not self.db:
# 			raise(NameError,u'暂未设置数据库信息')
# 		self.conn = pymssql.connect(host=self.host,user=self.user,password=self.pwd,database=self.db,charset='utf8')
# 		cur = self.conn.cursor()
# 		if not cur:
# 			raise(NameError,u'连接数据库失败')
# 		else:
# 			return cur

# 	def execQuery(self,sql):
# 		cur = self.__getConnect()
# 		cur.execute(sql)
# 		resList = cur.fetchall()
# 		self.conn.close()
# 		return resList

# 	def main():
# ## ms = MSSQL(host="localhost",user="sa",pwd="123456",db="PythonWeiboStatistics")
# ## #返回的是一个包含tuple的list，list的元素是记录行，tuple的元素是每行记录的字段
# ## ms.ExecNonQuery("insert into WeiBoUser values('2','3')")

#     ms = MSSQL(host="192.168.1.22",user="root",pwd="123456",db="PythonWeiboStatistics")
#     resList = ms.ExecQuery("SELECT id,weibocontent FROM WeiBo")
#     for (id,weibocontent) in resList:
#         print str(weibocontent).decode("utf8")


# 	Data Source=192.168.1.22;port=3306;Initial Catalog=volvo_annualmeeting;uid=root;password=123456;Charset=utf8
# if __name__ == '__main__':
# 	pass
from mysql.connector import connect

class MysqlC(object):

	def __init__(self,host,port,user,pwd,db):
		self.host = host
		self.port = port
		self.user = user
		self.pwd = pwd
		self.db = db

	def __getConnect(self):
		if not self.db:
			raise(NameError,u'暂未设置数据库信息')
		self.conn = connect(host=self.host,
							port=self.port,
							user=self.user,
							password=self.pwd,
							database=self.db,
							charset='utf8')
		cur = self.conn.cursor()
		if not cur:
			raise(NameError,u'连接数据库失败')
		else:
			return cur

	def execQuery(self,sql):
		cur = self.__getConnect()
		cur.execute(sql)
		resList = cur.fetchall()
		self.conn.close()
		return resList

	def deleteDml(self,sql):
		cur = self.__getConnect()
		cur.execute(sql)
		self.conn.commit()
		self.conn.close()


if __name__ == "__main__":

	model = MysqlC('120.27.162.0','3306','root','123456','volvo_annualmeeting')
