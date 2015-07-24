from flask import render_template
import os

def generateTestFiles(username, testName, testFile, databaseQuestions, testQuestions, Hours, Minutes, nSeconds):
  if not os.path.exists(os.getcwd()+'/templates/'+username):
      os.makedirs(os.getcwd()+'/templates/'+username)
  f = open('templates/'+username+'/' + testName + '.html', 'w' )
  content = render_template(testFile, databaseQuestions=databaseQuestions, testQuestions=testQuestions, hours=Hours, minutes=Minutes, seconds=nSeconds)
  f.write(content)
  f.close()
  return "Test Created successfully"