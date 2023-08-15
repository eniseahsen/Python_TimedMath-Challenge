import random
import time

OPERATORS = ["+","-","*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10


def generate_problem():
  left = random.randint(MIN_OPERAND,MAX_OPERAND)
  right = random.randint(MIN_OPERAND,MAX_OPERAND)
  operator = random.choice(OPERATORS)
  expr = str(left) + " " + operator + " " + str(right)
  answer = eval(expr) #eval fonksiyonu (evaulate) matematiksel işlem yapmak için kullanılır
  return expr,answer  #Fonksiyon, hem oluşturulan matematiksel ifadeyi (expr) hem de ifadenin hesaplanmış sonucunu (answer) bir demet (tuple) olarak döndürür.
 

#wrong = 0
input("Press enter to start!")
print("----------------------")

start_time = time.time() #süreyi başlatır
  
for i in range(TOTAL_PROBLEMS):
  expr,answer = generate_problem()
  while True: #sonsuz bir döngü başlatır
    guess= input("Problem #" + str(i+1) + " : " + expr + " = ")
    if guess == str(answer): #guess string answer ise integer değerinde olacağı için answer'ı stringe çevirdim
      break
    #else:
       #wrong +=1  
      
      
      
