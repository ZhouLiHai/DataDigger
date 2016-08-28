import time
import DBdealer as DB

def schedule(task_q):

	zargs = {
		'host':"localhost",
		'user':"root",
		'passwd':"1",
		'db':"eq",
		'port':3306,
		'charset':"utf8"}

	a = DB.DBD(zargs)

	while True:
		task = task_q.get()
		if(task == "DealRecord"):
			number = a.findLastRecord()
			code = "rd" + "%05d" % (number)
			print (code)

			datas = {
				'name':"Device-03",
				'code':code,
				'info':"This Device is used for General Test."
			}

			a.insertTHistory(datas)
			a.insertRecord(code,(1,1,1,1,1,1))

		if(task == "DealEvent"):
			number = a.findLastEvent()
			code = "ev" + "%05d" % (number)
			print (code)

			datas = {
				'type_id': 1,
				'name':"电压暂升",
				'code':code,
				'info':"This Device is used for General Test."
			}

			a.insertEHistory(datas)
			a.insertEvent(code, (1,2))

		if(task == "DealReal"):
			a.shift()

		task_q.task_done()

	a.destory()