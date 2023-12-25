#  write your code here 
import pandas as pd
df = pd.read_csv(r'D:\Projects\Nobel Laureates\Topics\Handling missing values\Replace with the mode\data\dataset\input.txt')
ml = df['location'].mode()[0]
df['location'].fillna(ml,inplace=True)
print(df.head())