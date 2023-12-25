#  write your code here 
import pandas as pd

df = pd.read_csv(
    r'D:\Projects\Nobel Laureates\Topics\Handling missing values\Handle missing values\data\dataset\input.txt')
# print(df.head())
# print(df.shape)
df.dropna(axis='columns', thresh=13, inplace=True)
# print(df.head())
for col in df.columns:
    m = df[col].median()
    df[col].fillna(m, inplace=True)
print(df.head())
