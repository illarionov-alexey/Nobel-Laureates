import pandas as pd
df = pd.read_csv(r'D:\Projects\Nobel Laureates\Topics\Summarizing numeric columns\Rock or Mine\data\dataset\input.txt',index_col=0)
#print(df.head())
R = df.loc[ df['labels'] == 'R','null_deg'].median()
M = df.loc[ df['labels'] == 'M','null_deg'].median()
print(f'M = {M:.3f} R = {R:.3f}')
#  write your code here

