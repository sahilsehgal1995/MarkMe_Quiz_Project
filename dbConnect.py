import MySQLdb
from MySQLdb import escape_string as thwart
from passlib.hash import sha256_crypt
import gc
import csv
import os

def connection():
  conn =MySQLdb.connect(host='localhost', user='root', passwd='123456', db='users')
  c = conn.cursor()
  return c, conn

def resultGeneration(testname):
  try:
    cursor,conn = connection()
    databaseName = testname
    databaseName = databaseName.replace(" ","")
    cursor.execute("use %s ;" %databaseName)
    conn.commit()
    cursor.execute("select username, name, score, email from users")
    with open(os.getcwd()+'/results/'+testname+'.csv', 'w') as f:
      writer = csv.writer(f)
      while True:
	  row = cursor.fetchone()
	  if row is None: break
	  writer.writerow(row)
    return "Result Generated Successfully"
  
  except Exception as e:
    return str(e)
      
def userLogin(databaseName, username, password):
  try:
    c,conn = connection()
    databaseName = databaseName.replace(" ","")
    c.execute("use %s ;" %databaseName)
    conn.commit()
    if c.execute("select * from users where username= '%s'" %(thwart(username))):
	  data = c.execute("select * from users where username= '%s'" %(thwart(username)))
	  data = c.fetchone()[1]
	  if sha256_crypt.verify(password,data):
	    return True
	  else:
	    return False
    else:
      return False
  except Exception as e:
    return str(e)
    

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
  c.execute("create table users (username varchar(100), score varchar(100),password text, name text, email text, primary key (username) );")
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

def submitScore(databaseName, username, score):
  try:
    conn =MySQLdb.connect(host='localhost', user='root', passwd='123456', db='users')
    c = conn.cursor()
    databaseName = databaseName.replace(" ","")
    c.execute("use %s ;" %databaseName)
    conn.commit()
    c.execute("update users set score='%s' where username='%s'" %(thwart(score), thwart(username)))
    conn.commit()
    return True
  except Exception as e:
    return False

def questionData(id, databaseName):
  c, conn= connection()
  databaseName = databaseName.replace(" ","")
  c.execute("use %s ;" %databaseName)
  conn.commit()
  c.execute("select * from questions where qno ='%s'" %(str(id)))
  return c.fetchone()
  

if __name__ == '__main__':
  output("Practice Test")