import re


class Customer:
    
    custlist = []
    page = -1

    def __init__(self):
        while True:
            self.exe(self.firstinput())

    def firstinput(self):
        print('''
        I - 고객정보 입력
        C - 현재 고객정보 조회
        P - 이전 고객정보 조회
        N - 다음 고객정보 조회
        U - 고객정보 수정
        D - 고객정보 삭제
        Q - 프로그램 종료
        ''')
        choice = input("다음 중에서 하실 일을 골라주세요 : ").upper()
        return choice
        
    def exe(self, choice):
        if choice == "I":
            self.insert_Data()
        elif choice == "C":
            self.curSearch()
        elif choice == "P":
            self.preSearch()
        elif choice == "N":
            self.nextSearch()
        elif choice == "U":
            self.updateData()
        elif choice == "D":
            self.deleteData()
        elif choice == "Q":
            quit()
        else:
            print("잘못 입력하였습니다.")

    #고객정보 입력
    def insert_Data(self):
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
                print("m/M 또는 f/F 중 입력해주세요.")
            
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
            for i in self.custlist:
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
        self.custlist.append(customer)
        print(self.custlist) #리스트 입력값 확인
        
        self.page = len(self.custlist)-1
        print(self.page)

    #현재 페이지
    def curSearch(self):
        if self.page == -1:
            print("입력된 데이터가 없습니다.")
        elif self.page >= 0:
            print("현재 페이지는 %d 입니다"%(self.page + 1))
            print(self.custlist[self.page])
            # print(custlist)

    #이전페이지    
    def preSearch(self):
        print("이전 페이지로 이동합니다.")
        if self.page == -1:
            print("입력된 데이터가 없습니다.")
        elif self.page <= 0:
            print("이전 페이지가 없습니다.")
        elif self.page > 0:
            self.page -= 1
            print("현재 페이지는 %d 입니다"%(self.page + 1))
            print(self.custlist[self.page])
        
    #다음페이지
    def nextSearch(self):
        print("다음 페이지로 이동합니다.")
        if self.page == -1:
            print("입력된 데이터가 없습니다.")
        elif self.page >= len(self.custlist)-1:
            print("다음 페이지가 없습니다.")
            print(self.page)
        elif self.page < len(self.custlist)-1:
            self.page += 1
            print("현재 페이지는 %d 입니다"%(self.page + 1))
            print(self.custlist[self.page])

    #수정
    def updateData(self):
        up_email = input("수정할 고객의 이메일 주소를 입력해주세요.\n")
        idx = -1

        for i in range(0,len(self.custlist)):
            if self.custlist[i]['email'] == up_email:
                idx = i

        if idx == -1:
            print("등록되지 않은 이메일입니다.")

        print("""
            name
            sex
            birthyear
            exit
            """)
        choice = input("수정할 고객 정보를 입력해주세요 : ")

        if choice in ('name','sex','birthyear'):
            self.custlist[idx][choice] = input('수정할 {}을 입력하세요.'.format(choice))
            print("수정되었습니다.")
            print(self.custlist)
            self.page = len(self.custlist)-1
            print(self.page)
            pass
        elif choice == 'exit':
            pass
        else:
            print("잘못된 입력입니다.")

    # 삭제
    def deleteData(self):
        del_email = input("삭제할 고객의 이메일 주소를 입력해주세요.\n")
        del_ok = 0
        
        for i in range(0,len(self.custlist)):
            if self.custlist[i]['email'] == del_email:
                print("{} 고객님의 정보가 삭제되었습니다.".format(self.custlist[i]['name']))
                del self.custlist[i]
                print(self.custlist)
                self.page = len(self.custlist)-1
                print(self.page)
                del_ok = 1
                break
        if del_ok == 0:
            print("등록되지 않은 이메일입니다.")

# 시작
a = Customer()