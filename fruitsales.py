# add your code here
import pandas as pd

df_myvar=pd.DataFrame({'Apples':['35', '41'],
              'Bananas':['21', '34']}, 
              index=['2017 Sales', '2018 Sales'])

df_myvar.to_csv("fruit.csv")

print(df_myvar)