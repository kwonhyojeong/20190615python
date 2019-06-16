coffee={'아메리카노':2500,'카페라떼':3000,'카푸치노':3500}
for i in coffee:
    print(i,end=" ")
order = input("\n 선택 : ")
if order not in coffee:
    print("잘못된 입력입니다.")
for k,v in coffee.items():
    if k == order:
        print(v)