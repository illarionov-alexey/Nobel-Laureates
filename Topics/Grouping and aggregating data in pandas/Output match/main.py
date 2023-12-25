#  You can experiment here, it won’t be checked
import pandas as pd
df = pd.DataFrame({'A': ['a', 'b', 'c', 'a', 'b'], 'B': [3, 2, 1, 0, -1], 'C': [0.5, 0.8, 0.2, 0.5, 0.9]})
print(df.agg({'C': 'min'}))
print(df.B.agg('unique'))
print(df.groupby(['A']).agg({'B':'mean'}).max())
print(df.C.agg('nunique'))