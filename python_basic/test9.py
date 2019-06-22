import time
import random

n = 1
w = ["사과","바나나","복숭아","자두","딸기","포도","수박","참외",'앵두','멜론','망고']
q = random.choice(w)

input("타자연습 시작!")
start = time.time()
while n <= 5:
    print("*문제",n)
    print(q)
    x = input()
    if q == x:
        print("통과!")
        n += 1
        q = random.choice(w)
    else:
        print("오타! 재도전!")

end = time.time()
t = end - start
print("타자시간 : {:.0f}초".format(t))