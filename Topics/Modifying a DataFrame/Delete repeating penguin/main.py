# your code here. The dataset is already loaded, the variable that contains the DataFrame is called penguins_example
'''
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
plt.close()

for i in range(10):
    plt.figure(i)

plt.close(1)
plt.show()
'''

'''
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10)
y = x

fig1 = plt.figure(1)
fig2 = plt.figure(2)

plt.plot(x,y)
plt.show()
'''

'''
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10)
y = x

fig, axes = plt.subplots(3, 3, figsize=(10, 16))
axes[1,1].plot(x,y)
plt.show()
'''
import numpy as np
array = np.array([[67, 234, 33, 65],
                  [333, 4, 7, 909],
                  [4, 1, 0, 121],
                  [72, 23, 53, 96],
                  [19, 87, 76, 65]])

print(array[::2, ::3])
print(array[3, ::2])
print(array[:2, :2])
print(array[1:4, -1])
print(array[::2, 3])

array = np.linspace(20, 42, num=11)
print(array[4])

import matplotlib.pyplot as plt

payment_method = ['Debit', 'Credit', 'Cash', 'Other']
statistics = [48, 33, 9, 10]
colors = ['lightblue', 'yellowgreen', 'coral', 'gold']

# YOUR CODE HERE #
plt.barh(payment_method,statistics,color=colors)
plt.xlabel('Number of transactions (%)')
plt.ylabel('Methods')
plt.title('Preferred payment methods in 2014')
plt.show()
