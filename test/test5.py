import time as t

input("엔터를 누르고 2초를 셉니다.")
a = t.time()
input("2초 후에 다시 엔터를 누릅니다.")
b = t.time()

c = b - a

print("실제시간 : %.2f"%c)
print("차이 : %.2f 초"%(abs(c-2)))