class Question:

     def __init__(self)  :
          self.qText=''
          self.answer =''
          self.response=''
          
     def setQuestion(self,QuestionText):
          self.qText=QuestionText

     def displayQuestion(self):
         print( self.qText)

     def setAnswer(self,answer):
          self.answer=answer
          
     def putResponse(self,response):
         self.response=response
          

     def checkAnswer(self):
          return self.answer==self.response

     
 
class MultiChoiceQuestion (Question):
      def __init__(self) :
          super().__init__(qText,answer,response) 
          self.choices=[]

          
      def addChoice(self,choice):
          self.choices.append(choice)

          
      def dispayQuestion(self):
          super().dispayQuestion()
          for i in range( len(self.choices ) ):
               print(i +': '+self.choices [i]  )

      def setAnswer(self,answer):
          self.answer=answer
          aList=[]
          answeri=self.answer.split(',')
          aList.append(choice)
          
          
a=Question()
a.setQuestion('Who is the prime minister of the UK')
a.displayQuestion()
a.setAnswer('T.May')
a.putResponse('T.Maty')
print(a.checkAnswer())
