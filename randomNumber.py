import random
question_set= {}
def rand():
  i = 1
  while (i < 11):
    y = random.randint(1,10)
    if (y not in question_set.values()):
      ques = 'question_' + str(i)
      question_set[ques]=y
      i = i + 1
  return question_set
  #for keys,values in dic.items():
    #print keys + " " +str(values)
  ##print dic
  
if __name__=='__main__':
  rand()