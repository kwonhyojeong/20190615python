import time, random


n = 1
w = ["사과","바나나","복숭아","자두","딸기","포도","수박","참외",'앵두','멜론','망고']
q = random.choice(w)
w2 = []

while True:
    print("1. 단문연습 2. 타자게임 3. 종료하기")
    menu = input("메뉴를 선택하세요 \n")

    #문장연습
    if menu == '1':
        f = open("./python_basic/word.txt",'r')
        line = 1
        #w.clear() 기존 문제 제거하고 추가하기
        while line:
            line = f.readline().replace("\n","")
            if not(line == ''):
                w2.append(line)
        print(w2)

        input("단문연습 시작!")
        start = time.time()
        while n <= 5:
            print("* 문제",n)
            print(line)
            x = input()
            if w2 == x:
                print("통과!")
                n += 1
                w2 = random.choice(line)
            else:
                print("오타! 재도전!")

        end = time.time()
        t = end - start
        print("타자시간 : {:.0f}초".format(t))
        

    #단어연습
    elif menu == '2':
        input("단어연습 시작!")
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

    # 종료하기    
    elif menu == '3':
        break

f.close()