import pandas as pd
a1=pd.read_excel('a1.xlsx')
a2=pd.read_excel('a2.xlsx')
a3=pd.read_excel('a3.xlsx')
a4=pd.read_excel('a4.xlsx')
for i in range(1,38):
    t1=a1.loc[i]
    t2=a2.loc[i]
    t3=a3.loc[i]
    t4=a4.loc[i]
    t1.rename(1)
    t2.rename(2)
    t3.rename(3)
    t4.rename(4)
    t1.to_excel('xlss/'+str(i)+'-1.xlsx')
    t2.to_excel('xlss/'+str(i)+'-2.xlsx')
    t3.to_excel('xlss/'+str(i)+'-3.xlsx')
    t4.to_excel('xlss/'+str(i)+'-4.xlsx')