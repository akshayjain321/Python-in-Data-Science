import os
os.system('cls||clear')

import numpy as np
import pandas as pd

df = pd.read_csv('balance.txt', delimiter =' ')

print(df.head())

dates = pd.date_range('20240113', periods=6)
print(dates)

df = pd.DataFrame(np.random.randn(6,4), index=(dates    ), columns = ['A','B','C','DEFG'])
print(df)

data = { 'Stage': ['First', 'Seccond', 'Third', 'Fourth'],
        'Status': ['Begin', 'Accelerate', 'Slow down', 'Stop']
}

df = pd.DataFrame(data, index = (1,2,3,4))
print(df)

data1 = ('akshay', 'richa', 'reyan', 'dia')
series = pd.Series(data1, index = (1,2,3,4))
print(series)