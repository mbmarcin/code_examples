# Given a pandas dataframe containing a pandas series/column of tuples B, 
# we want to extract B into B1 and B2 and assign them into separate pandas series

# Method 1: (faster)
# use pd.Series.tolist() method to return a list of tuples 
# use pd.DataFrame on the resulting list to turn it into a new pd.DataFrame object, while specifying the original df index
# add to the original df 

import pandas as pd
import time 

# Put your dataframe here
df = pd.DataFrame({'A':[1,2], 'B':[(1,2), (3,4)]})  

print("Original Dataset")
print(df)

start = time.time()
df[['B1','B2']] = pd.DataFrame(df['B'].tolist(),index=df.index)
print("Method 1")
print("Time elapsed :" + str(time.time()-start))
print(df)


# Method 2: (more Pythonic but much slower for larger dataframes)
# use the pd.DataFram.apply method to the column with the pd.Series function

start = time.time()
df[['B1','B2']] = df['B'].apply(pd.Series)
print("Method 2")
print("Time elapsed :" + str(time.time()-start))
print(df)



#EXAMPLE

dta2 = {
    'a': [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 3],
    'b': [7, 7, 8, 8, 9, 9, 22, 22, 12, 12, 12, 12]
    #'c': [45, 34, 12, 45, 56, 67, 78, 34, 23, 34, 45, 23]
}
#
# df = pd.DataFrame(dta)
df2 = pd.DataFrame(dta2)

# change value per group
def first_last(group, col_qty):
    """
    :param group: group
    :param col_qty: num of col
    :return: first and last element df
    """
    lst = group.iloc[:, col_qty].to_list()
    #return pd.Series([lst[0], lst[len(lst) - 1]])--------> helpfuly
    return lst[0], lst[len(lst) - 1]


x = df2.groupby('a').apply(first_last, 1).reset_index()
x[['f', 'e']] = pd.DataFrame(x.iloc[:, 1].tolist(), index=x.index)

print(x)