class Question:
    def __init__(self,text,choices,answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def checkAnswer(self,string):
        if self.answer == string:
            return True
        else:
            return False


class Quiz:
    answer = ""
    q1 = Question("en iyi programlama dili hangisidir",["python","c#","java","dart"],"python")
    q2 = Question("en populer programlama dili hangisidir",["python","c#","java","dart"],"python")
    q3 = Question("en cok kazandiran programlama dili hangisidir",["python","c#","java","dart"],"python")
    def __init__(self):
        self.questionIndex = 0
        self.score = 0
        self.questions = [Quiz.q1,Quiz.q2,Quiz.q3]
        
    
    def getQuestion(self):
        Quiz.displayQuestion(self)
        
    def displayQuestion(self):
        print(f'{self.questions[self.questionIndex].text.capitalize()}: ')
        for i in self.questions[self.questionIndex].choices:
            print(i)
        Quiz.answer = input("\n")
    def loadQuestion(self):
        if len(self.questions) - 1  == self.questionIndex:
            Quiz.getQuestion(self)
            if self.questions[self.questionIndex].checkAnswer(Quiz.answer):
                self.score+=1
                print(f'Skorunuz {self.score}!')
            else:
                print(f'Skorunuz {self.score}!')
            print("Oyun sonlanmistir.")
        else:
            Quiz.getQuestion(self)
            if self.questions[self.questionIndex].checkAnswer(Quiz.answer):
                self.score+=1
                self.questionIndex+=1
                Quiz.displayScore(self)
                Quiz.loadQuestion(self)
            else:
                self.questionIndex+=1
                Quiz.displayScore(self)
                Quiz.loadQuestion(self)
            
    def displayScore(self):
        Quiz.displayProgress(self)
        print("***********************")
        print(f'Skorunuz {self.score}!')
    def displayProgress(self):
        print(f'{len(self.questions)} adet sorudan {self.questionIndex + 1}. sorudasiniz.')


a1 = Quiz()
a1.loadQuestion()
