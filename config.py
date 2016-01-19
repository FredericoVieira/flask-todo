import MySQLdb as mysqldb

def conn():
	return mysqldb.connect(host='localhost', user='root', passwd='', db='flask-todo')