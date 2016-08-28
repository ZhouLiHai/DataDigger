import time
import pymysql as DB

ISOTIMEFORMAT='%Y-%m-%d %X'

"""
	处理数据库相关的日常事务
	1. 维护数据库连接
	2. 保障没有缺失的数据库表
	3. 处理实时数据的插入
	4. 处理历史数据的周期性插入
	5. 检查数据库中出现的错误

"""

class DBD(object):


	def __init__(self, args):
		self.args = args
		self.conn=DB.connect(host=args['host'],user=args['user'],\
			passwd=args['passwd'],db=args['db'],port=args['port'])
		self.cur=self.conn.cursor()


	def destory(self):
		self.cur.close()
		self.conn.close()

	def resetRealData(self):
		count = self.cur.execute("select * from realdata");
		row = self.cur.fetchall()

		if (count != 1 or row[0][0] !=1):
			self.cur.execute("delete from realdata");

	def codeIsExist(self, name, code):
		self.cur.execute("select * from thistories where name = '%s' and code = '%s'" %(name, code));
		codes = self.cur.fetchall()

		return (len(codes))

	def insertTHistory(self, args):
		self.cur.execute("insert into thistory(name,code,info,date) values(\"%s\", \"%s\", \"%s\", \"%s\")"\
		 % (args['name'],args['code'],args['info'],time.strftime(ISOTIMEFORMAT, time.localtime())))

		# self.cur.execute('drop table if exists %s' % (args['code']))
		self.cur.execute('create table if not exists %s(id int auto_increment not null primary key, d1 float, d2 float, d3 float, d4 float, d5 float, d6 float)' % (args['code']))


	def insertRecord(self, code, datas):
		self.cur.execute("insert into %s(d1,d2,d3,d4,d5,d6) values(%f, %f, %f, %f, %f, %f)"\
			% (code,datas[0],datas[1],datas[2],datas[3],datas[4],datas[5]))
	
	def shift(self):
		command = "alter table realdata add d"

		for x in range(200,201):
			self.cur.execute("alter table realdata add d" + str(x) + " float;")
