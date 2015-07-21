  
var questionNumbers = {};
var optionsMarked = {};
var timeLeft = new Date();
var correctAnswer;
var questionButtonList = {}, responses = {};
var currentQuestion;
var timer;

function questionListGeneration()
 {
  var array = new Array;
  for (var i=1; i<=10;)
  {
    var rand = Math.floor((Math.random() * 10) + 1);
    if((array.indexOf(rand)) == -1)
    {
      var x=rand.toString();
      array.push(rand);
      var string = "Question " + i.toString();
      questionNumbers[string] = rand;
      optionsMarked[string]="unMarked";
      questionButtonList[string] = "button_" + i.toString();
      responses[string] = "Wrong Answer";
      i++;
    }
   }  
   currentQuestion = "Question 1"
   questionChange(currentQuestion);
}

function optionUpdationOnForm()
{
  var choiceMarking = document.forms[0];
  if(optionsMarked[currentQuestion] != "unMarked")
    choiceMarking[optionsMarked[currentQuestion] - 1].checked=true;
  else
    for(var i=0; i<4;i++)
    {
      choiceMarking[i].checked = false;
    }
}

function markAnswerClicked()
{
	var option = document.forms[0];
	for (var i=0; i<4; i++)
	{
		if(option[i].checked)
		{
			if (option[i].value == correctAnswer)
			{
			  alert("Correct Answer");
			  responses[currentQuestion] = "Correct Answer";
			}
			optionsMarked[currentQuestion] = i+1;
			document.getElementById(questionButtonList[currentQuestion]).className = "btn btn-success";
						
		}
	}
}

function questionChange(questionId)
{
  xmlhttp = new XMLHttpRequest();
  xmlhttp.onreadystatechange = function()
  {
    if (xmlhttp.readyState==4 && xmlhttp.status==200)
    {
      var myArr = JSON.parse(xmlhttp.responseText);
      currentQuestion=questionId;
      document.getElementById("question").innerHTML = currentQuestion + ": " + myArr.question;
      document.getElementById("option1").innerHTML = myArr.option1;
      document.getElementById("option2").innerHTML = myArr.option2;
      document.getElementById("option3").innerHTML = myArr.option3;
      document.getElementById("option4").innerHTML = myArr.option4;
      correctAnswer = myArr.correct_answer;
      var option = document.forms[0];
      option[0].value=myArr.option1;
      option[1].value=myArr.option2;
      option[2].value=myArr.option3;
      option[3].value=myArr.option4;
      optionUpdationOnForm();
    }
  }
  var url = "/test/" + questionNumbers[questionId].toString();
  xmlhttp.open("GET", url, true);
  xmlhttp.send();
}

function scoreSubmission(score)
{
  xmlhttp = new XMLHttpRequest();
  
  xmlhttp.onreadystatechange = function()
  {
    if (xmlhttp.readyState==4 && xmlhttp.status==200)
    {
     // alert(xmlhttp.responseText);
      window.location.href="/scoresubmission/";
    }
  }
  //var my = document.getElementById("user").innerHTML;
  var url = "/scoresubmission/?username="+ document.getElementById("user").innerHTML + "&score="+ score.toString();
  xmlhttp.open("POST",url, true);
  xmlhttp.send();
}

function startButtonClicked()
{
	timeLeft.setHours(0);
	timeLeft.setMinutes(0);
	timeLeft.setSeconds(10);
	document.getElementById("endButton").style.visibility='visible';
	document.getElementById("ques").style.visibility='visible';
	document.getElementById("questionButtons").style.visibility='visible';
	document.getElementById("startButton").style.visibility='hidden';
	timer = setInterval(function(){timeUpdation()}, 1000);
}

function endTest()
{
	var score=0;
	for (var key in responses)
	{
	  if(responses[key] == "Correct Answer")
	    score++;
	}
	scoreSubmission(score);
	clearTimeout(timer);
}

function timeUpdation()
{	
	var seconds = timeLeft.getSeconds();
	var hours = timeLeft.getHours(), 
	    minutes = timeLeft.getMinutes();
	    
	if(minutes<10)
		minutes = "0"+ minutes.toString();
	
	if (hours<10)
		hours = "0"+ hours.toString();
	
	if (seconds<10)
		seconds = "0" + seconds.toString();
	document.getElementById("Timer").innerHTML = hours +" : " +
												 minutes + " : " +
												 seconds ;
	
	if((timeLeft.getHours())==0 && (timeLeft.getMinutes()==0) && (timeLeft.getSeconds()==0))
		{
		  endTest();
		}
	
	if((timeLeft.getHours())==0 && (timeLeft.getMinutes()<1))
		{
			var myvar = document.getElementById("Timer");
			myvar.innerHTML = ""+myvar.innerHTML + "";
		}

	timeLeft.setSeconds(timeLeft.getSeconds()-1);
}
questionListGeneration();


