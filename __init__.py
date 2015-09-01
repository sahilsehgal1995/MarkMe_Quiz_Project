from flask import Flask, render_template, url_for, flash, session, redirect, request, jsonify
from dbConnect import connection,questionEntry, userRegistrationInDatabase, submitScore, questionData, userLogin, resultGeneration
from wtforms import Form, TextField, PasswordField, BooleanField, StringField
from wtforms.validators import Required, Length, EqualTo
from datetime import datetime
from passlib.hash import sha256_crypt
from MySQLdb import escape_string as thwart
from functools import wraps
from os import path
import gc, json
import commands, os
from createTestFiles import generateTestFiles, testList, TimeVerification, deleteFiles


app=Flask(__name__)
app.config['SECRET_KEY'] = 'HARD TO GUESS'

class UserRegisteration(Form):
  username = TextField('Username', validators=[Required(), Length(min=3, max=15)])
  name = TextField('Full name', validators=[Required(), Length(min=3, max=20)])
  email = TextField('Email', validators=[Required()])
  password = PasswordField('Password', validators=[Required(), EqualTo('confirm'), Length(min=3)])
  confirm = PasswordField('Confirm Password', validators=[Required()])

class questions(Form):
  qno = StringField('Question number')
  question = TextField('Question',validators=[Required()])
  option1 = TextField('Option A', validators=[Required()])
  option2 = TextField('Option B', validators=[Required()])
  option3 = TextField('Option C', validators=[Required()])
  option4 = TextField('Option D', validators=[Required()])
  correct_answer = TextField('Correct Answer', validators=[Required()])
  
@app.route('/')
def index():
  return render_template("main.html")



def login_required(f):
  @wraps(f)
  def wrap(*args, **kwargs):
    if 'logged_in' in session:
      return f(*args, **kwargs)
    else:
      flash("You need to login first")
      return redirect(url_for("login"))
  return wrap


@app.route('/dashboard/', methods=['GET', 'POST'])
def dashboard():
  return render_template("dashboard.html")

@app.route('/logout/')
@login_required
def log_out():
  session.clear()
  flash("You have been logged out!")
  gc.collect()
  return redirect(url_for('dashboard'))

@app.route('/login/', methods=['GET', 'POST'])
def login():
  error=''
  try:
    form2 = UserRegisteration(request.form)
    c,conn = connection()
    if request.method =='POST':
      if request.args.get('testname'):
	reply = userLogin(request.args.get('testname'), request.form['username'], request.form['password'])
	if reply:
	  session['logged_in'] = True
	  session['username'] = request.form['username']
	  flash('You are now logged in!')
	  return redirect(url_for('dashboard'))
	else:
	  flash('Authentication failed')
	
      else:
	reply = userLogin("users", request.form['username'], request.form['password'])
	if reply is True:
	  session['logged_in'] = True
	  session['username'] = request.form['username']
	  session['admin'] = True
	  flash('You are now logged in!')
	  return redirect(url_for('dashboard'))
	else:
	  flash('Authentication failed')
    else:
      flash("Welcome to login page")
    return render_template("login.html", form=form2, testname=request.args.get('testname'))
  
  except Exception as e:
    return (str(e))

@app.route('/questions/<databasename>', methods=['GET', 'POST'])
@login_required
def question_set(databasename):
  try:
    form = questions(request.form)
    if request.method=='POST' and form.validate():
      databaseReply = questionEntry(databasename, form.qno.data, form.question.data, form.option1.data, form.option2.data, form.option3.data, form.option4.data, form.correct_answer.data)
      flash(databaseReply)
      return redirect('questions/'+databasename)
    else:
      return render_template('question.html', testname=databasename)
    
  except Exception as e:
    return (str(e))


@app.route('/test/<testname>', methods=['GET','POST'])
@login_required
def taketest(testname):
  try:
    reply = TimeVerification(testname)
    if reply:
      session['testname']=testname
      return render_template("tests/"+testname +".html", )
    
    flash("Test is not available now")
    return render_template('dashboard.html')
    
  except Exception as e:
    return (str(e))
  
@app.route('/scoresubmission/', methods=['GET','POST'])
@login_required
def scoreSubmission():
  try:
    
    if request.method == 'POST':
      testname = request.args.get('testname')
      reply = TimeVerification(testname)
      if reply:
	session['score'] = request.args.get('score')
	response = submitScore(testname, session['username'], request.args.get('score'))
	if response:
	  return "Score Submitted Successfully"
	else:
	  return "UnAble To submit your Score"
      else:
	return "Test is not available now"

    if request.method == 'GET':
      return render_template("testCompletion.html")
  
  except Exception as e:
    return (str(e))

@app.errorhandler(404)
def page_not_found(e):
  try:
    return render_template(url_for("dashboard"))
  except Exception as e:
    return render_template("404.html", error=e)
  
@app.route('/register/<testname>', methods=['GET', 'POST'])
def register(testname):
  try:
    flash ("Welcome to User Registration Page!!")
    form = UserRegisteration(request.form)
    if request.method == 'POST' and form.validate():
      username = form.username.data
      c, conn = connection()
      testname = testname.replace(" ","")
      c.execute("use %s ;" %testname)
      conn.commit()
      x = c.execute("select * from users where username = '%s'" %(thwart(username)))
      if int(x) > 0:
	flash("Oops!! That username already exists, Try something else")
	return render_template("register.html", form = form)
      else:
	databaseReply = userRegistrationInDatabase(testname, username, form.password.data,form.email.data, form.name.data,)
	flash(databaseReply)
	session['logged_in'] = True
	session['username'] = username
	return redirect(url_for('dashboard'))
    else:
      return render_template("register.html", form=form, testname=testname)
  except Exception as e:
    return (str(e))

@app.route('/adminregister/', methods=['GET', 'POST'])
def adminRegisteration():
  try:
    if request.method == 'POST':
      if request.form['regcode'] == 'ss123':
	c, conn = connection()
	testname = 'users'
	c.execute("use %s ;" %testname)
	conn.commit()
	x = c.execute("select * from users where username = '%s'" %(thwart(request.form['username'])))
	if int(x) > 0:
	  flash("Oops!! That username already exists, Try something else")
	  return render_template("adminregister.html")
	else:
	  databaseReply = userRegistrationInDatabase(testname, request.form['username'], request.form['password'],request.form['emailid'], request.form['name'])
	  flash(databaseReply)
	  session['logged_in'] = True
	  session['username'] = request.form['username']
	  return redirect(url_for('dashboard'))
      else:
	flash("Invalid Registeration Code")
	return redirect(url_for('adminRegisteration'))
    else:
      return render_template("adminregister.html")
    
  except Exception as e:
    return str(e)

@app.route('/ques/', methods=['GET', 'POST'])
@login_required
def ajax():
  try:
    if request.method == 'POST':
      x = questionData(request.args.get('testid'), request.args.get('testname'))
      Question = {
      'question': x[1],
      'option1': x[2],
      'option2': x[3],
      'option3': x[4],
      'option4': x[5],
      'correct_answer': x[6],
      }
      return jsonify(Question)
  
  except Exception as e:
    return str(e)
  
@app.route('/createtest/', methods=['GET','POST'])
@login_required
def createTest():
  try:
    if request.method == 'POST':
       response = generateTestFiles(request.form['testName'], "test.html", request.form['databaseQuestions'], request.form['testQuestions'], request.form['noOfHours'], request.form['noOfMinutes'], request.form['noOfSeconds'], request.form['startDate'], request.form['startTime'])
       flash(response)
       return redirect('/questions/'+request.form['testName'])
    
    return render_template("createTest.html")
    
  except Exception as e:
    return str(e)

@app.route('/testlist/', methods=['GET','POST'])
def test_list():
  try:
    response=testList()
    if response is False:
      flash("You have not created any test")
      return redirect(url_for('createTest'))
    
    return render_template("testList.html", dic=response)
    
  except Exception as e:
    return str(e)

@app.route('/deletetest/<testname>', methods=['GET', 'POST'])
@login_required
def delete_test(testname):
  try:
    reply = deleteFiles(testname)
    if reply:
      flash("Test Deleted Successfully")
    else:
      flash("Unable to delete test")
    return redirect(url_for('test_list'))
    
  except Exception as e:
    return str(e)

@app.route('/results/<testname>', methods=['GET', 'POST'])
def result(testname):
  try:
    reply = resultGeneration(testname)
    flash(reply)
    return redirect(url_for('test_list'))
  
  except Exception as e:
    return str(e)

if __name__=='__main__':
  app.run(host='172.16.230.1')
