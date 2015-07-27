import MySQLdb
from MySQLdb import escape_string as thwart
from passlib.hash import sha256_crypt
import gc

def connection():
  conn =MySQLdb.connect(host='localhost', user='root', passwd='123456', db='users')
  c = conn.cursor()
  return c, conn

def questionEntry(tablename, qno, question, option1, option2, option3, option4, correct_answer):
  c,conn = connection()
  c.execute("INSERT INTO %s (qno, question, option1, option2, option3, option4, correct_answer) values('%s','%s','%s','%s','%s','%s','%s')" %(tablename,thwart(qno), thwart(question), thwart(option1), thwart(option2), thwart(option3), thwart(option4), thwart(correct_answer)))
  conn.commit()
  c.close()
  conn.close()
  gc.collect()
  return "Qestion Added to database Successfully"

def userRegistrationInDatabase(username, password, email, name):
  c, conn = connection()
  c.execute("INSERT INTO users (username, password, email, name) values ('%s','%s','%s','%s')" %(thwart(username),sha256_crypt.encrypt(str(thwart(password))),thwart(email),thwart(name)))
  conn.commit()
  c.close()
  conn.close()
  gc.collect()
  return "User Registration Successfully completed!!!!"


def databaseCreation(databaseName):
  conn =MySQLdb.connect(host='localhost', user='root', passwd='123456', db='users')
  c = conn.cursor()
  c.execute("create database %s" %databaseName)
  conn.commit()
  c.execute("use %s ;" %databaseName)
  conn.commit()
  c.execute("create table users (rno varchar(100), password text, name text, email text, primary key (rno) );")
  conn.commit()
  c.execute("create table questions (qno varchar(760), question text, option1 text, option2 text, option3 text, option4 text, correct_answer text, primary key (qno));")
  conn.commit()
  c.close()
  gc.collect()
  return 

def databaseDeletion(databaseName):
  conn =MySQLdb.connect(host='localhost', user='root', passwd='123456', db='users')
  c = conn.cursor()
  c.execute("drop database %s" %databaseName)
  conn.commit()
  c.close()
  gc.collect()
  return 

if __name__ == '__main__':
  databaseDeletion("Sample")