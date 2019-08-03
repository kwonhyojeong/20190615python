import pandas as pd
from pandas import DataFrame, Series
import matplotlib.pyplot as plt
import matplotlib as mpl

df = pd.read_csv(r'Movie/cine.csv',engine='python',encoding='utf-8')

print(df.head(20))
temp1 = df[df['movieNm'] == '나랏말싸미']
print(temp1)
temp2 = df[df['movieNm'] == '명탐정 코난: 감청의 권']
print(temp2)
mpl.rc('font', family='Malgun Gothic') #한글 폰트 설정
fig = plt.figure()
fig.set_size_inches(9.4,4.8)
#분할해 그리기 시작
axe = fig.add_subplot(1,2,1) #1행(row) 2열(column)중 첫 번째 subplot
axe.plot([str(x) for x in temp1['targetDt']], temp1['salesAmt'],label='나랏말싸미')
axe.set_title('나랏말싸미')
axe.set_xlabel('날짜')
axe.set_ylabel('매출액')
for tick in axe.xaxis.get_major_ticks():
    tick.label.set_fontsize(6) 
    tick.label.set_rotation(90)
axe = fig.add_subplot(1,2,2) #1행(row) 2열(column)중 두번째 subplot
axe.plot([str(x) for x in temp2['targetDt']], temp2['salesAmt'],label='명탐정 코난: 감청의 권')
axe.set_title('명탐정 코난: 감청의 권')
axe.set_xlabel('날짜')
axe.set_ylabel('매출액')
for tick in axe.xaxis.get_major_ticks():
    tick.label.set_fontsize(6) 
    tick.label.set_rotation(90)
plt.suptitle('나랏말싸미과 명탐정 코난: 감청의 권의 일별 매출액(salesAmt) 선 그래프')
#분할해 그리기 끝
plt.show()