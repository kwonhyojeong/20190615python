import re
custlist = []
page = -1

def exe(choice):
    if choice == "I":
        insert_Data()
    elif choice == "C":
        curSearch()
    elif choice == "P":
        preSearch()
    elif choice == "N":
        nextSearch()
    elif choice == "U":
        updateData()
    elif choice == "D":
        deleteData()
    elif choice == "Q":
        quit()
    else:
        print("잘못 입력하였습니다.")

#고객정보 입력
def insert_Data():
    customer = {'name':'','sex':'',"email":'',"birthyear":''}
    print("고객정보 입력")

    #이름입력
    customer['name'] = input("이름 : ")

    #성별입력
    while True:
        customer['sex'] = input("성별 (M/F) : ")
        customer['sex'] = customer['sex'].upper()
        if customer['sex'] in ('M','F'):
            break
        else:
            print("m 또는 f 중 입력해주세요.")
        
    #이메일입력
    while True:
        regex = re.compile('^[a-z][a-z0-9]{4,15}@[a-zA-Z]{2,8}[.][a-zA-Z]{2,3}$')
        while True:
            customer['email'] = input("이메일 : ")
            golbang = regex.search(customer['email'])
            if golbang:
                break
            else:
                print("'@'를 포함한 정확한 이메일을 써주세요.")

        check = 0
        for i in custlist:
            if i['email'] == customer['email']:
                check = 1

        if check == 0:
            break
        print("중복되는 이메일이 있습니다.")

    #생년입력
    while True:
        customer['birthyear'] = input("생년 4자리 : ")
        if len(customer['birthyear']) == 4 and customer['birthyear'].isdigit():
            break

    print(customer) #입력값 확인
    custlist.append(customer)
    print(custlist) #리스트 입력값 확인
    global page
    page += 1 #페이지 최대값


def curSearch():
    global page
    print("현재 페이지는 %d 입니다"%page)
    
# def preSearch():
# def nextSearch():
# def updateData():
# def deleteData():


# 시작
while True:
    choice = input(''' 다음 중에서 하실 일을 골라주세요 : 
    I - 고객정보 입력
    C - 현재 고객정보 조회
    P - 이전 고객정보 조회
    N - 다음 고객정보 조회
    U - 고객정보 수정
    D - 고객정보 삭제
    Q - 프로그램 종료
    ''')
    choice = choice.upper()

    exe(choice)