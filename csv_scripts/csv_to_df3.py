import pandas as pd

excel_file = 'python_github.csv'
df = pd.read_csv(excel_file)
print(df)
print(df.head(5))
#print(df.loc[:,'Name'])
#print(df.loc[:,'Link'])
#print(df.iloc[:,0])


#df.to_csv("trump.csv")
#print(df)
