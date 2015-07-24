from flask import render_template
import os
from os import walk

def generateTestFiles(username, testName, testFile, databaseQuestions, testQuestions, Hours, Minutes, nSeconds, date, time):
  if not os.path.exists(os.getcwd()+'/templates/users/'+username):
      os.makedirs(os.getcwd()+'/templates/users/'+username)
  f = open(os.getcwd()+'/templates/users/'+username+'/' + testName + '.html', 'w' )
  content = render_template(testFile, databaseQuestions=databaseQuestions, testQuestions=testQuestions, hours=Hours, minutes=Minutes, seconds=nSeconds, startDate=date ,startTime=time)
  f.write(content)
  f.close()
  return "Test Created successfully"

def testList(username):
  if not os.path.exists(os.getcwd()+'/templates/users/'+username):
    return False
  else:
    files = []
    for (dirpath, dirnames, filenames) in walk(os.getcwd()+'/templates/users/'+username):
      files.extend(filenames)
      break
    fileList = []
    for f in files:
      fileList.append(f[0:-5])
    return fileList