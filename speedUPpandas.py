SPEED UP PANDAS


import seaborn as sns
import pandas as pd

data = sns.load_dataset('iris')

print(data.head())

#------------------------------------------------------

CLASSIC PANDAS LOOP

import seaborn as sns
import time

data = sns.load_dataset('iris')

def compute_class(petal_length):
    if petal_length <= 2:
        return 1
    elif 2 < petal_length < 5:
        return 2
    else:
        return 3

start = time.time()

class_list = list()

for i in range(len(data)):
    petal_length = data.iloc[i]['petal_length']
    class_num = compute_class(petal_length)
    class_list.append(class_num)

end = time.time()
print("For-loop run time = {}".format(end - start))

#------------------------------------------------------

#Looping with .iterrows()

import seaborn as sns
import time

data = sns.load_dataset('iris')

def compute_class(petal_length):
    if petal_length <= 2:
        return 1
    elif 2 < petal_length < 5:
        return 2
    else:
        return 3

start = time.time()

class_list = list()
for index, data_row in data.iterrows():
    petal_length = data_row['petal_length']
    class_num = compute_class(petal_length)
    class_list.append(class_num)

end = time.time()
print("Iterrows run time = {}".format(end - start))

#------------------------------------------------------------

#Dropping loops completely with .apply()
import seaborn as sns
import time

data = sns.load_dataset('iris')

def compute_class(petal_length):
    if petal_length <= 2:
        return 1
    elif 2 < petal_length < 5:
        return 2
    else:
        return 3

start = time.time()

class_list = data.apply(lambda row: compute_class(row['petal_length']), axis=1)

end = time.time()
print(".apply() run time = {}".format(end - start))

#----------------------------------------------------------------------
#The final cut
import seaborn as sns
import time
import pandas as pd

data = sns.load_dataset('iris')

start = time.time()

class_list = pd.cut(x=data.petal_length,
                   bins=[0, 2, 5, 100],
                   include_lowest=True,
                   labels=[1, 2, 3]).astype(int)

end = time.time()
print(".cut() run time = {}".format(end - start))









































