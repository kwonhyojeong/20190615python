sum = 0
for i in range(1,11):
    if i % 2 != 0: continue
    sum += i
    print(sum)
print(sum)



# marks = [90,25,67,45,80]
# for num in range(len(marks)):
#     if marks[num]<60:
#         continue
#     print("%d 번 학생 축하합니다. 합격입니다."%(num+1))