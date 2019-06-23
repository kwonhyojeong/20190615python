num=input("주민번호 입력 : ")
if num[7] == '1' or num[7] == '3' or num[7] == '5':
    print("남자")
elif num[7] == '2' or num[7] == '4' or num[7] == '6':
    print("여자")
else:
    print("입력이 잘못되었습니다.")