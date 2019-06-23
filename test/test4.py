import random as r
z = ['+','-','*','/']

count = 0
for i in range(0,10):
    a = r.randint(1,50)
    b = r.randint(1,50)
    c = r.choice(z)
    quiz = str(a)+c+str(b)
    print(quiz+'=',end="")
    # print(eval(quiz))
    d = int(input(""))
    if int(eval(quiz)) == d:
        print("정답!")
        count += 1
    else:
        print("오답!")

print("%d개 맞음"%count)