import random

def getAnswer(answerNumber):
    if answerNumber == 1:
           return 'It is certain'
    elif answerNumber == 2:
           return 'It is decidedly so'
    elif answerNumber == 3:
           return 'Yes'
    elif answerNumber == 4:
           return 'why bother?'
    elif answerNumber == 5:
           return 'Ask again later'
    elif answerNumber == 6:
           return 'Concentrate and ask again'
    elif answerNumber == 7:
           return 'My reply is no'
    elif answerNumber == 8:
           return 'oof dawg, thats gotta be a no from me'
    elif answerNumber == 9:
           return 'Very doubtful'
    elif answerNumber == 10:
           return 'bruh seriously?'
    elif answerNumber == 11:
    	   return 'For sure-zies bro-beanie'       
print(getAnswer(random.randint(1,11)))
