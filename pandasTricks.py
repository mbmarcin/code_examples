#Logical operations
data[data['column_1']=='french']
data[(data['column_1']=='french') & (data['year_born']==1990)]
data[(data['column_1']=='french') & (data['year_born']==1990) & ~(data['city']=='London')]
data[data['column_1'].isin(['french', 'english'])]


#Updating the data
data.loc[8, 'column_1'] = 'english'
data.loc[data['column_1']=='french', 'column_1'] = 'French'


"""
tqdm, the one and only
When working with large datasets, pandas can take some time running .map(), .apply(), .applymap() operations. tqdm is a very useful package that helps predict when theses operations will finish executing (yes I lied, I said we would use only pandas).
"""
from tqdm import tqdm_notebook
tqdm_notebook().pandas()
data['column_1'].progress_map(lambda x: x.count('e'))


#Correlation and scatter matrices
data.corr()
data.corr().applymap(lambda x: int(x*100)/100)

pd.plotting.scatter_matrix(data, figsize=(12,8))
#-------------------------------------------------------------

#Grouping
data.groupby('column_1')['column_2'].apply(sum).reset_index()

#Iterating over rows
dictionary = {}

for i,row in data.iterrows():
  dictionary[row['column_1']] = row['column_2']


#select_dtypes
df.dtypes.value_counts()
df.select_dtypes(include=['float64', 'int64'])

#copy
import pandas as pd
df1 = pd.DataFrame({ 'a':[0,0,0], 'b': [1,1,1]})
df2 = df1
df2['a'] = df2['a'] + 1
df1.head()

df2 = df1.copy()

from copy import deepcopy
df2 = deepcopy(df1)

#map
level_map = {1: 'high', 2: 'medium', 3: 'low'}
df['c_level'] = df['c'].map(level_map)

#apply czy nie apply?
def rule(x, y):
    if x == 'high' and y > 10:
         return 1
    else:
         return 0
df = pd.DataFrame({ 'c1':[ 'high' ,'high', 'low', 'low'], 'c2': [0, 23, 17, 4]})
df['new'] = df.apply(lambda x: rule(x['c1'], x['c2']), axis =  1)
df.head()

df['maximum'] = df.apply(lambda x: max(x['c1'], x['c2']), axis = 1)

df['maximum'] = df[['c1','c2']].max(axis =1)

"""
Wniosek: Nie używaj apply, jeśli możesz wykonać tę samą pracę z innymi wbudowanymi funkcjami (często są szybsze). Na przykład, jeśli chcesz zaokrąglić kolumnę „c” do liczb całkowitych, wykonaj round(df['c'], 0) lub df['c'].round(0), zamiast używać funkcji: df.apply(lambda x: round(x['c'], 0), axis = 1).
"""


#Liczniki wartości
df['c'].value_counts()
df['c'].value_counts().reset_index()
df['c'].value_counts().reset_index().sort_values(by='index')

#Liczba brakujących wartości
import pandas as pd
import numpy as np
df = pd.DataFrame({ 'id': [1,2,3], 'c1':[0,0,np.nan], 'c2': [np.nan,1,1]})
df = df[['id', 'c1', 'c2']]
df['num_nulls'] = df[['c1', 'c2']].isnull().sum(axis=1)
df.head()

#Wybierz wiersze z określonymi identyfikatorami
df_filter = df['ID'].isin(['A001','C022',...])
df[df_filter]


"""
Percentyle
Masz kolumnę liczbową i chcesz sklasyfikować wartości w tej kolumnie w grupy, powiedzmy najwyższe 5% w grupie 1, 5–20% w grupie 2, 20%-50% w grupie 3, 50% w grupie 4. Oczywiście, możesz to zrobić za pomocą pandas.cut, ale chciałbym zaproponować inne rozwiązanie:
"""
import numpy as np
cut_points = [np.percentile(df['c'], i) for i in [50, 80, 95]]
df['group'] = 1
for i in range(3):
    df['group'] = df['group'] + (df['c'] < cut_points[i])
# or <= cut_points[i]


#to_csv
print(df[:5].to_csv())
float_format='%.0f'
