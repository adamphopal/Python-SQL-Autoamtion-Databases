import pandas as pd

excel_file = 'output.csv'
df = pd.read_csv(excel_file)
#print(df)
print(df.head(3))
#print(df.loc[:,'title'])
#print(df.loc[:,'link'])
#print(df.iloc[:,0])


#df.to_csv("trump.csv")
#print(df)
