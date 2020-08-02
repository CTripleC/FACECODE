
import pandas as pd
from collections import Counter

from pip._vendor.distlib.compat import raw_input

data=pd.read_csv('F:/python/FACECODE/templates/dataset.csv',sep=',',usecols=[2,5,10,13,14,15,16,17],encoding='windows-1252',names=None)
data1=pd.read_csv('F:/python/FACECODE/templates/dataset.csv',sep=',',usecols=[5,16],encoding='windows-1252',names=None)
df_li =data1.values.tolist()
names,products=[],[]
n=0
name=raw_input("请输入顾客名称：")

for i in range(len(data1)):
    if(df_li[i][0]==name):
        products.append(df_li[i][1])
        a={}
        for word in products:
          if products.count(word)>=1:
           a[word]=products.count(word)






# 饼状图
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False
label_list =a.keys()   # 各部分标签
size = a.values()    # 各部分大小
patches, l_text, p_text = plt.pie(size, labels=label_list, labeldistance=1.1, autopct="%1.1f%%", shadow=False, startangle=90, pctdistance=0.6)
plt.axis("equal")    # 设置横轴和纵轴大小相等，这样饼才是圆的
plt.legend()
plt.show()


# 条形图
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False
price = a.values()
n=len(a.values())
plt.barh(range(n), price, height=0.7, color='steelblue', alpha=0.8)      # 从下往上画
plt.yticks(range(n), a.keys())
plt.xlabel("购买数量")
plt.title("商品所属类型")
for x, y in enumerate(price):
    plt.text(y + 0.2, x - 0.1, '%s' % y)
plt.show()
