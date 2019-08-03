import pandas as pd
from pandas import DataFrame, Series
import matplotlib.pyplot as plt
import matplotlib as mpl

df = pd.read_csv(r'movie/cine.csv',engine='python',encoding='utf-8')

temp = df.groupby('movieNm').sum()
temp = temp.sort_values(by='salesAmt', ascending=0)
temp = temp.iloc[:10]
print(temp)

mpl.rc('font', family='Malgun Gothic') #한글 폰트 설정
mpl.rcParams['font.size'] = 9
plt.pie(temp['salesAmt'], labels=temp.index, autopct='%.1f%%', shadow=True)
plt.title('총 매출액 상위 10개의 영화명(movieNm) 파이 차트')
plt.show()