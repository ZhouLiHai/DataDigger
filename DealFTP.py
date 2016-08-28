from ftplib import FTP

"""
    处理FTP文件下载功能
    指定网络参数、目录以及需要下载的文件名

    处理文件监测功能
    指定网络参数、目录，返回此目录下的文件列表
"""

def DownFile(ip, port, user, passwd, path, filename, localfile):

    ftp=FTP()
    ftp.set_debuglevel(0)
    ftp.connect(ip, port)
    ftp.login(user, passwd)

    ftp.cwd(path)
    bufsize = 1024

    file_handler = open(localfile, 'wb')
    ftp.retrbinary('RETR ' + filename, file_handler.write, bufsize)
    file_handler.close()

    ftp.quit()

def ShowList(ip, port, user, passwd, path):

    ftp=FTP()
    ftp.set_debuglevel(0)
    ftp.connect(ip, port)
    ftp.login(user, passwd)

    ftp.cwd(path)
    lst = ftp.nlst()

    ftp.quit()
    return lst


if __name__ == '__main__':
    DownFile('192.168.0.40', 21, 'admin', '123456', 'HardDisk/board1/statistics/20151103', '20151103T005911.pqd')
    lst = ShowList('192.168.0.40', 21, 'admin', '123456', 'HardDisk/board1/statistics/20151103')
    print (lst)




