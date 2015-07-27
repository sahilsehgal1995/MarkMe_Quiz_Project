import MySQLdb
from MySQLdb import escape_string as thwart
from passlib.hash import sha256_crypt
import gc

def connection():
  conn =MySQLdb.connect(host='localhost', user='root', passwd='123456', db='users')
  c = conn.cursor()
  return c, conn

def questionEntry(databaseName, qno, question, option1, option2, option3, option4, correct_answer):
  try:
    c,conn = connection()
    databaseName = databaseName.replace(" ","")
    c.execute("use %s ;" %databaseName)
    conn.commit()
    c.execute("INSERT INTO questions (qno, question, option1, option2, option3, option4, correct_answer) values('%s','%s','%s','%s','%s','%s','%s')" %(thwart(qno), thwart(question), thwart(option1), thwart(option2), thwart(option3), thwart(option4), thwart(correct_answer)))
    conn.commit()
    c.close()
    conn.close()
    gc.collect()
    return "Qestion Added to database Successfully"
  
  except Exception as e:
    return "Question could not be entered"

def userRegistrationInDatabase(databaseName, username, password, email, name):
  c, conn = connection()
  databaseName = databaseName.replace(" ","")
  c.execute("use %s ;" %databaseName)
  conn.commit()
  c.execute("INSERT INTO users (username, password, email, name) values ('%s','%s','%s','%s')" %(thwart(username),sha256_crypt.encrypt(str(thwart(password))),thwart(email),thwart(name)))
  conn.commit()
  c.close()
  conn.close()
  gc.collect()
  return "User Registration Successfully completed!!!!"

def databaseCreation(databaseName):
  conn =MySQLdb.connect(host='localhost', user='root', passwd='123456', db='users')
  c = conn.cursor()
  databaseName = databaseName.replace(" ","")
  c.execute("create database %s" %databaseName)
  conn.commit()
  c.execute("use %s ;" %databaseName)
  conn.commit()
  c.execute("create table users (username varchar(100), password text, name text, email text, primary key (username) );")
  conn.commit()
  c.execute("create table questions (qno varchar(760), question text, option1 text, option2 text, option3 text, option4 text, correct_answer text, primary key (qno));")
  conn.commit()
  c.close()
  gc.collect()
  return 

def databaseDeletion(databaseName):
  try:
    conn =MySQLdb.connect(host='localhost', user='root', passwd='123456', db='users')
    c = conn.cursor()
    databaseName = databaseName.replace(" ","")
    c.execute("drop database %s" %databaseName)
    conn.commit()
    c.close()
    gc.collect()
    return True
  
  except Exception as e:
    return False

if __name__ == '__main__':
  databaseDeletion("Sample")