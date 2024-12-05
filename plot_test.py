import pandas as pd
from matplotlib.pyplot import *
for i in range(1,37):
    a1=pd.read_excel('xlss/'+str(i)+'-1.xlsx')
    a2=pd.read_excel('xlss/'+str(i)+'-2.xlsx')
    a3=pd.read_excel('xlss/'+str(i)+'-3.xlsx')
    a4=pd.read_excel('xlss/'+str(i)+'-4.xlsx')
    t1=a1[i].to_list()
    t2=a2[i].to_list()
    t3=a3[i].to_list()
    t4=a4[i].to_list()

    figure(figsize=(15,10))
    rcParams.update({"font.size":15})
    rcParams['axes.unicode_minus'] = False
    rcParams['font.sans-serif'] = ['SimHei']
    m=['语','数','英','物','化','生史地','总']
    lst=[]
    lst.append(t1)
    lst.append(t2)
    lst.append(t3)
    lst.append(t4)
    print(lst)
    # cmepcos
    t=[]
    for i in range(2,len(lst[0])):
        if i%3==0:
            for j in range(4):
                t.append(lst[j][i])
            print(t)
            bar([i*0.2/3,2+i*0.2/3,4+i*0.2/3,6+i*0.2/3],t,0.2)
            t=[]
            
    legend(['语','数','英','物','化','生/史/地','总'])
    ylabel('年级排名')
    title(lst[0][1]+'成绩表')
    xticks([0.7, 2.7, 4.7, 6.7],['6月','9月','10月','11月'], rotation=30, fontsize=15)
    savefig('折线图/'+lst[0][1]+'.png')
    # show()
    cla()
    tit=['高二下期末, ', '高三九月月考, ', '高三十月月考, ', '高三上期中, ']
    with open('table/'+lst[0][1]+'.csv','w') as file:
        file.write('考试, 准考证号, 姓名, 语文得分, 语文校次, 语文班次, 数学得分, 数学校次, 数学班次, 英语得分, 英语校次, 英语班次, 物理得分, 物理校次, 物理班次, 化学得分, 化学校次, 化学班次, 生史地得分, 生史地校次, 生史地班次, 总分, 总分校次, 总分班次\n')
        for i in range(4):
            file.write(tit[i])
            for j in lst[i]:
                file.write(str(j))
                file.write(', ')
            file.write('\n')