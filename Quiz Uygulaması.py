class Question:
    def __init__(self,text,choices,answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def chechAnswer(self, answer):
        return self.answer == answer

# print(q1.chechAnswer("python"))

class Quiz:
    def __init__(self,questions):
        self.questions = questions
        self.score = 0
        self.questionIndex = 0          # 1 yaparsan diğer soru gelir

    def getQuestion(self):
        return self.questions[self.questionIndex]

    def displayQuestion(self):
        question = self.getQuestion()
        print(f"Soru {self.questionIndex+1}: {question.text}")

        for q in question.choices:
            print("-"+ q)

        answer = input("cevap: ")
        self.guess(answer)
        self.loadQuestion()

    def guess(self, answer):
        question = self.getQuestion()

        if question.chechAnswer(answer):
            self.score += 1
        self.questionIndex += 1

    def loadQuestion(self):
        if len(self.questions) == self.questionIndex:
            self.showScore()
        else:
            self.displayProgress()
            self.displayQuestion()

    def showScore(self):
        print("score:", self.score)

    def displayProgress(self):
        totalQuestion = len(self.questions)
        questionNumber = self.questionIndex + 1

        if questionNumber > totalQuestion:
            print("Quiz bitti.")
        else:
            print(f"Question {questionNumber} of {totalQuestion}".center(50, "*"))

q1 = Question("En iyi programlama dili hangisidir?", ["c#", "python", "java"], "python")
q2 = Question("En popüler programlama dili hangisidir?", ["c#", "python", "java"], "python")
q3 = Question("En çok kazandıran programlama dili hangisidir?", ["c#", "python", "java"], "python")
questions = [q1,q2,q3]

quiz = Quiz(questions)
# question = quiz.getQuestion()         # quiz.questions[quiz.questionIndex]
# print(question.text)
quiz.loadQuestion()