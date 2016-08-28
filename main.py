import sys
import time
import datetime
import configparser
import multiprocessing

import DBdealer as MDB
import DealFTP as MFTP
import DealPQDIF as PQDIF


def maketarget(config):
	deviceID = int(config.get('global', 'id'))
	lines = int(config.get('global', 'lines')) + 1
	makeup = int(config.get('global', 'makeup')) + 1

	res = []
	stamp = datetime.datetime.now()
	for x in range(1,makeup):
		for y in range(1,lines):
			tm = stamp - datetime.timedelta(x)
			path = "HardDisk/board%d/statistics/" %(y)
			datas = "%02d%02d%04d%02d%02d" %(deviceID, y, tm.year, tm.month, tm.day)
			res.append([path, datas, "%02d-%02d" %(deviceID, y), 0])
	return res

def makedb(config, tar):
	host = config.get('DB', 'host')
	port = config.get('DB', 'port')
	db = config.get('DB', 'db')
	user = config.get('DB', 'user')
	passwd = config.get('DB', 'passwd')
	charset = config.get('DB', 'charset')

	mdb = MDB.DBD({'host':host,'port':int(port),'db':db,'user':user,'passwd':passwd,'charset':charset})

	for i, x in enumerate(tar):
		 tar[i][3] = mdb.codeIsExist(x[2],x[1])

	return mdb, tar

def makeftp(config, tar):
	ip = config.get('FTP', 'ip')
	port = int(config.get('FTP', 'port'))
	user = config.get('FTP', 'user')
	passwd = config.get('FTP', 'passwd')

	def makepqdif(orgfile, tarfile):
		pq = PQDIF.PQdeal();
		fp = open(orgfile,'rb')
		data = fp.read()
		fp.close()
		fp = open(tarfile + '.data', 'w')

		pq.chipCut(data, fp)
		fp.close()

	def downloadALL(ip, port, user, passwd, lst, path, name):
		for x in lst:
			print (x, path, name)
			MFTP.DownFile(ip, port, user, passwd, path, x, 'OrgData/' + name + x)
			makepqdif('OrgData/' + name + x, 'Data/' + name + x)
		print ("==" * 40)

	for x in tar:
		if x[3] == 0:
			lst = MFTP.ShowList(ip, port, user, passwd, x[0] + x[1][4:])
			downloadALL(ip, port, user, passwd, lst, x[0] + x[1][4:], x[2])

def main():
	config = configparser.ConfigParser()
	config.read('config.ini')

	tar = maketarget(config)
	mdb, tar= makedb(config, tar)

	makeftp(config, tar)


if __name__ == '__main__':
	main()