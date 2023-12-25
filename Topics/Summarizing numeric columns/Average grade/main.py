# your code here. The DataFrame is already loaded as grades
#import pandas as pd
#dic = {'Student': ['Ann', 'Bob'], 'Algebra': [10, 8], 'Ph': [1, 2]}
#grades = pd.DataFrame(dic)
print(grades.mean(axis=1,numeric_only=True))
