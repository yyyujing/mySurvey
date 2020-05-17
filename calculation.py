import pandas as pd
import numpy as np

df = pd.read_csv('/Users/yujing/Desktop/results_transform.csv')



def calculation (df, name):
    subDF = df.loc[:,df.columns.str.contains(name)]
    mean = subDF.mean(axis=1,skipna = True)
    return mean


name1 = 'C1'
meanC1 = calculation(df,name1)
#print(meanC1)

name2 = 'C2'
meanC2 = calculation(df,name2)

name3= 'S1'
meanS1 = calculation(df,name3)

name4='S2'



#calculate personality traits
p1DF = df.loc[:,df.columns.str.contains('P1')]

exDF = p1DF.loc[:,p1DF.columns.str.contains('001')|p1DF.columns.str.contains('006')|p1DF.columns.str.contains('011')|p1DF.columns.str.contains('016') \
                  | p1DF.columns.str.contains('021')| p1DF.columns.str.contains('026')|p1DF.columns.str.contains('031')|p1DF.columns.str.contains('036')]
#print(exDF)
meanEx = exDF.mean(axis=1, skipna = True)

agDF = p1DF.loc[:,p1DF.columns.str.contains('002')|p1DF.columns.str.contains('007')|p1DF.columns.str.contains('012')|p1DF.columns.str.contains('017') \
                  | p1DF.columns.str.contains('022')| p1DF.columns.str.contains('027')|p1DF.columns.str.contains('032')|p1DF.columns.str.contains('037') | p1DF.columns.str.contains('042') ]
meanAg = agDF.mean(axis=1, skipna = True)

neDF = p1DF.loc[:,p1DF.columns.str.contains('004')|p1DF.columns.str.contains('009')|p1DF.columns.str.contains('014')|p1DF.columns.str.contains('019') \
                  | p1DF.columns.str.contains('024')| p1DF.columns.str.contains('029')|p1DF.columns.str.contains('034')|p1DF.columns.str.contains('039')]
meanNe = neDF.mean(axis=1, skipna = True)

opDF = p1DF.loc[:,p1DF.columns.str.contains('005')|p1DF.columns.str.contains('010')|p1DF.columns.str.contains('015')|p1DF.columns.str.contains('020') \
                  | p1DF.columns.str.contains('025')| p1DF.columns.str.contains('030')|p1DF.columns.str.contains('035')|p1DF.columns.str.contains('040') | p1DF.columns.str.contains('041') | p1DF.columns.str.contains('044')]
meanOp = opDF.mean(axis=1, skipna = True)

coDF = p1DF.loc[:,p1DF.columns.str.contains('003')|p1DF.columns.str.contains('008')|p1DF.columns.str.contains('013')|p1DF.columns.str.contains('018') \
                  | p1DF.columns.str.contains('023')| p1DF.columns.str.contains('028')|p1DF.columns.str.contains('033')|p1DF.columns.str.contains('038') | p1DF.columns.str.contains('043') ]
meanCo = coDF.mean(axis=1, skipna = True)


#calculate social media usage preference

soDF = df.loc[:,df.columns.str.contains('SO1')]

boDF = soDF.loc[:,soDF.columns.str.contains('001')|soDF.columns.str.contains('002')|soDF.columns.str.contains('003')|soDF.columns.str.contains('004') |\
    soDF.columns.str.contains('005')| soDF.columns.str.contains('008')|soDF.columns.str.contains('007')]
meanBo = boDF.mean(axis=1, skipna = True)

brDF = soDF.loc[:,soDF.columns.str.contains('006')|soDF.columns.str.contains('009')|soDF.columns.str.contains('010')|soDF.columns.str.contains('011') |\
    soDF.columns.str.contains('013')]
meanBr = brDF.mean(axis=1, skipna =True)

conDF = soDF.loc[:,soDF.columns.str.contains('012')|soDF.columns.str.contains('015')]
meanCon = conDF.mean(axis=1, skipna= True)

saDF = soDF.loc[:,soDF.columns.str.contains('014')| soDF.columns.str.contains('016')|soDF.columns.str.contains('017')]
meanSa = saDF.mean(axis=1, skipna= True)


name4 = 'SO2'
meanSO2 = calculation(df,name4)

name5 = 'PR1'
meanPR1 = calculation(df,name5)

name6 = 'PR2'
meanPR2 = calculation(df,name6)


#combine the results into a whole data frame
a= df.loc[:,'id']
resultDF = pd.DataFrame(a, columns=['id'])
resultDF['C1'] = meanC1
resultDF['C2'] = meanC2
resultDF['P1EX']=meanEx
resultDF['P1AG']=meanAg
resultDF['P1CO']=meanCo
resultDF['P1NE']=meanNe
resultDF['P1OP']=meanOp
resultDF['S1']=meanS1
resultDF['SO1BO']=meanBo
resultDF['SO1BR']=meanBr
resultDF['SO1CON']=meanCon
resultDF['SO1ST']=meanSa
resultDF['SO2']=meanSO2
resultDF['PR1'] = meanPR1
resultDF['PR2']=meanPR2

print(resultDF)

df_clean = pd.read_csv('/Users/yujing/Desktop/results_clean.csv')
df_select = df_clean[['D1','D2','D3','D4','D5','D6']]
df_new = pd.concat([df_select,resultDF],axis=1)

resultDF.to_csv('/Users/yujing/Desktop/results_calculation.csv', encoding='utf-8', index=False)








df_new.to_csv('/Users/yujing/Desktop/results_new.csv', encoding='utf-8', index=False)