import pandas as pd

df = pd.DataFrame({'a': [1, 4], 'b': [2, 5]})

# your code here
df['c'] = [3,6]
df2 = pd.DataFrame({'a': [7], 'b': [8], 'c': [9]})
df = df.append(df2,ignore_index=True)
#print(df)