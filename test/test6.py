import random as r
import time as t
count = 0
a = r.randint(1,100)

input("시작!")
start = t.time()
while True:
    b = int(input("1~100사이 숫자를 입력하세요.\n"))
    count += 1
    if a == b:
        print("정답입니다.")
        break
    elif a < b:
        print("더 작은 숫자를 입력하세요")
        
    elif a > b:
        print("더 큰 숫자를 입력하세요.")

end = t.time()
t = end - start
print("%d회만에 정답을 맞추었습니다."%count)
print("걸린 시간은 {:.0f}초 입니다.".format(t))