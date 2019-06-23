import random as r

# for i in range(5):
#     lotto = [0,0,0,0,0,0]
#     for j in range(6):
#         num = 0
#         while(num in lotto):
#             num = r.randint(1,45)
#         lotto[j] = num
#     print("로또 : ",sorted(lotto))

for i in range(1, 6):
    print("로또 :",sorted(r.sample(range(1, 46),6)))