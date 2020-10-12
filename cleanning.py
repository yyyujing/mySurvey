import pandas as pd
import numpy as np
df = pd.read_csv('/Users/yujing/Desktop/results-survey281339.csv')
#df.info()
#print(df.head(9))
#print(df ['id'])



#print (df.columns.get_loc("id"))  #get column index by column name

df1 = df[df.columns[0:df.columns.get_loc("FC1")]] #choose the columns before FC1

#print (df1.head())

df2 = df1.dropna(how='all',axis=1)
print (df2.head())
for col in df2.columns:
    print (col)  # print all the elements in the df2. columns object


df2.dropna(subset=['D1'],inplace=True) #drop the empty rows in the column D1
print(df2.head())
#print(df2.shape) 15*135

df3 = df2.drop(['submitdate','lastpage','startlanguage','startdate','datestamp','refurl','CF2'],axis=1)

print(df3.head())

print(type(df3.iloc[0]['C1[SQ001]']))

#df3.loc[df3['D1']=='Male','D1']= 0 #update
#df3.loc[df3['D1']=='Female','D1']= 1 #update

df3.to_csv('/Users/yujing/Desktop/results_clean.csv', encoding='utf-8', index=False) #aviod adding the index when writing to csv