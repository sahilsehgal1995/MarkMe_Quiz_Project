from flask import render_template
import os
from os import walk

def generateTestFiles(username, testName, testFile, databaseQuestions, testQuestions, Hours, Minutes, nSeconds, date, time):
  if not os.path.exists(os.getcwd()+'/templates/tests/'):
      os.makedirs(os.getcwd()+'/templates/tests/')
  f = open(os.getcwd()+'/templates/tests/' + testName + '.html', 'w' )
  content = render_template(testFile, databaseQuestions=databaseQuestions, testQuestions=testQuestions, hours=Hours, minutes=Minutes, seconds=nSeconds, startDate=date ,startTime=time)
  f.write(content)
  f.close()
  
  f = open(os.getcwd()+'/templates/tests/' + testName + '.txt', 'w' )
  f.write(username+'\n')
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

def testList(username):
  if not os.path.exists(os.getcwd()+'/templates/tests/'):
    return False
  else:
    files = []
    for (dirpath, dirnames, filenames) in walk(os.getcwd()+'/templates/tests/'):
      files.extend(filenames)
      break
    fileList = []
    for f in files:
      string =f[-5:]
      if(string =='.html'):
	fileList.append(f[0:-5])
    return fileList
     
from datetime import datetime

  
def startTimeVerification(testname):
  f = open(os.getcwd()+'/templates/tests/'+testname+'.txt', 'r' )
  lines = f.readlines()
  date = lines[-2]
  date = date[:-1]
  time = lines[-1]
  time = time[:-1]
  date=date.replace("-", " ")
  time =time.replace(":", " ")
  dt = date + " "+time
  date = datetime.strptime(dt, '%Y %m %d %H %M')
  if datetime.now()< date:
    return False
  else:
    return True

  
if __name__=='__main__':
  token()