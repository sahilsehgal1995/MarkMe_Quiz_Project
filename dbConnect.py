import MySQLdb
from MySQLdb import escape_string as thwart
from passlib.hash import sha256_crypt
import gc

def connection():
  conn =MySQLdb.connect(host='localhost', user='root', passwd='123456', db='users')
  c = conn.cursor()
  return c, conn

def questionEntry(qno, question, option1, option2, option3, option4, correct_answer):
  c,conn = connection()
  c.execute("INSERT INTO questions (qno, question, option1, option2, option3, option4, correct_answer) values('%s','%s','%s','%s','%s','%s','%s')" %(thwart(qno), thwart(question), thwart(option1), thwart(option2), thwart(option3), thwart(option4), thwart(correct_answer)))
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


