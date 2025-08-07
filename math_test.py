import random
import time

MAX_VALUE = 10
MIN_VALUE = 1
OPERANDS = ["+" , "-" , "*"]

def generate_problem():
    left = random.randint(MIN_VALUE, MAX_VALUE)
    right = random.randint(MIN_VALUE, MAX_VALUE)
    operand = random.choice(OPERANDS)

    problem = str(left)+" "+ operand +" "+str(right)
    solution = str(eval(problem))

    return problem, solution

wrong = 0
input("Press Enter to start test")
print("-----------------------------")
start_time = time.time()
for i in range(10):
    qn, ans = generate_problem()
    while True:
        answer=input("Problem #"+str(i+1)+" : "+qn+" = ")
        if answer != ans:
            wrong += 1 
        else:
            break
           
end_time = time.time()

print("-----------------------------")
print("You have "+str(wrong)+" incorrect attempt(s)..")
total_time = end_time - start_time
print("Time taken : "+str(round(total_time,1))+"seconds.")