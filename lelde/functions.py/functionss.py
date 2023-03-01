#1

def SumTwoNumbers():
    print(3+5)
     #funkcijai obligati jabut iekavam beigas
SumTwoNumbers()    


#2


def SumTwoNumbers(a,b):
    return a+b
   
SumTwoNumbers(10, 20)




#3

def SumTwoNumbers(x, y):
  return x+y
  
n1=int(input('Choose number one: '))
n2=int(input('Choose number two: '))
result = SumTwoNumbers(n1,n2)
print(result)



#4

def PrintNiceShapes():
   print('=======')
   print('<<<<<<')
   print('=======')

   
name = input('What is your name?: ')
PrintNiceShapes()
age = input('How old are you?: ')
PrintNiceShapes()
drink = input('What is yout favorite drink?: ')
PrintNiceShapes()
print(f'Hello {name}! You are {age} y.o.\nYour favorite drink is {drink}.')