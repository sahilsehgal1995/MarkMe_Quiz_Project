from flask import render_template
import os
from os import walk
import datetime
from dbConnect import databaseCreation, databaseDeletion

def generateTestFiles(testName, testFile, databaseQuestions, testQuestions, Hours, Minutes, nSeconds, date, time):
  if not os.path.exists(os.getcwd()+'/templates/tests/'):
      os.makedirs(os.getcwd()+'/templates/tests/')
  f = open(os.getcwd()+'/templates/tests/' + testName + '.html', 'w' )
  content = render_template(testFile,testName=testName , databaseQuestions=databaseQuestions, testQuestions=testQuestions, hours=Hours, minutes=Minutes, seconds=nSeconds, startDate=date ,startTime=time)
  f.write(content)
  f.close()
  
  databaseCreation(testName)
  
  f = open(os.getcwd()+'/templates/tests/' + testName + '.txt', 'w' )
  f.write(testName+'\n')
  f.write(testFile+'\n')
  f.write(databaseQuestions+'\n')
  f.write(testQuestions+'\n')
  f.write(Hours+'\n')
  f.write(Minutes+'\n')
  f.write(nSeconds+'\n')
  f.write(date+'\n')
  f.write(time+'\n')
  f.close()
  return "Test Created successfully"

def testList():
  if not os.path.exists(os.getcwd()+'/templates/tests/'):
    return False
  else:
    files = []
    for (dirpath, dirnames, filenames) in walk(os.getcwd()+'/templates/tests/'):
      files.extend(filenames)
      break
    if not files:
      return False
    fileList = []
    for f in files:
      string =f[-5:]
      if(string =='.html'):
	fileList.append(f[0:-5])
    dic = {}
    for f in fileList:
      fileObject = open(os.getcwd() + '/templates/tests/'+f+'.txt', 'r')
      lines= fileObject.readlines()
      date=lines[-2]
      dic[f] = date[:-1]
    return dic
     

  
def TimeVerification(testname):
  f = open(os.getcwd()+'/templates/tests/'+testname+'.txt', 'r' )
  lines = f.readlines()
  date = lines[-2]
  date = date[:-1]
  time = lines[-1]
  time = time[:-1]
  date=date.replace("-", " ")
  time =time.replace(":", " ")
  dt = date + " "+time
  startTime = datetime.datetime.strptime(dt, '%Y %m %d %H %M')
  endTime = endTimeVerification(testname)
  if datetime.datetime.now() < startTime or datetime.datetime.now() > endTime:
    return False
  else:
    return True


def endTimeVerification(testname):
  f = open(os.getcwd()+'/templates/tests/'+testname+'.txt', 'r' )
  lines = f.readlines()
  date = lines[-2]
  date = date[:-1]
  time = lines[-1]
  time = time[:-1]
  date=date.replace("-", " ")
  time =time.replace(":", " ")
  dt = date + " "+time
  date = datetime.datetime.strptime(dt, '%Y %m %d %H %M')
  
  hours=lines[-5]
  hours = int(hours[:-1])
  minutes=lines[-4]
  minutes=int(minutes[:-1])
  seconds=lines[-3]
  seconds=int(seconds[:-1])
  return date + datetime.timedelta(0,hours*3600 + (minutes+3)*60 + seconds)


def deleteFiles(testName):
  os.remove(os.getcwd()+'/templates/tests/'+testName+'.html')
  os.remove(os.getcwd()+'/templates/tests/'+testName+'.txt')
  reply = databaseDeletion(testName)
  return reply
  
def sample():
  s= "Computer archi sample"
  print s
  s=s.replace(" ", "")
  print s

if __name__=='__main__':
  sample()