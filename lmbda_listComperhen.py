def custom_rating(genre,rating):
    if 'Thriller' in genre:
        return min(10,rating+1)
    elif 'Comedy' in genre:
        return max(0,rating-1)
    else:
        return rating
        
df['CustomRating'] = df.apply(lambda x: custom_rating(x['Genre'],x['Rating']),axis=1)

df.apply(lambda x: func(x['col1'],x['col2']),axis=1)

#--------------------------------------------------------------------------------------------------

# Single condition: dataframe with all movies rated greater than 8
df_gt_8 = df[df['Rating']>8]
# Multiple conditions: AND - dataframe with all movies rated greater than 8 and having more than 100000 votes
And_df = df[(df['Rating']>8) & (df['Votes']>100000)]
# Multiple conditions: OR - dataframe with all movies rated greater than 8 or having a metascore more than 90
Or_df = df[(df['Rating']>8) | (df['Metascore']>80)]
# Multiple conditions: NOT - dataframe with all emovies rated greater than 8 or having a metascore more than 90 have to be excluded
Not_df = df[~((df['Rating']>8) | (df['Metascore']>80))]



#create a new column
df['num_words_title'] = df.apply(lambda x : len(x['Title'].split(" ")),axis=1)
#simple filter on new column
new_df = df[df['num_words_title']>=4]

new_df = df[df.apply(lambda x : len(x['Title'].split(" "))>=4,axis=1)]

year_revenue_dict = df.groupby(['Year']).agg({'Rev_M':np.mean}).to_dict()['Rev_M']
def bool_provider(revenue, year):
    return revenue<year_revenue_dict[year]
    
new_df = df[df.apply(lambda x : bool_provider(x['Rev_M'],x['Year']),axis=1)]

df['Price'] = df.apply(lambda x: int(x['Price'].replace(',', '')),axis=1)



#One-Line List Comprehension
x = [1,2,3,4]
out = []
for item in x:
    out.append(item**2)
print(out)
[1, 4, 9, 16]

# vs.

x = [1,2,3,4]
out = [item**2 for item in x]
print(out)
[1, 4, 9, 16]


df.drop([c for c in df.columns if c.startswith('temp_')], axis=1, inplace=True)
// or
df = df[[c for c in df.columns if not c.startswith('temp_')]]

# 2 examples

l = list()

for i in range(1,101):
    if i % 15 == 0:
        l.append('fizz')
    elif i % 5 == 0:
        l.append('fizz2')
    elif i % 3 == 0:
        l.append('fizz3')
    else:
        l.append(i)
        
listA = ['fizz' i % 15 == 0 else 'fizz2' if i % 5 == 0 else 'fizz3' i % 3 == 0 else i for i in range(1,101)]


#Lambda Functions
double = lambda x: x * 2
print(double(5))

add = lambda x, y : x + y   
print add(2, 3) # Output: 5


#Map and Filter
# Map
seq = [1, 2, 3, 4, 5]
result = list(map(lambda var: var*2, seq))
print(result)
[2, 4, 6, 8, 10]


def multiply2(x):
  return x * 2
map(multiply2, [1, 2, 3, 4])  # Output [2, 4, 6, 8]
map(lambda x : x*2, [1, 2, 3, 4]) #Output [2, 4, 6, 8]

Iterating Over a Dictionary Using Map and Lambda
dict_a = [{'name': 'python', 'points': 10}, {'name': 'java', 'points': 8}]
map(lambda x : x['name'], dict_a) # Output: ['python', 'java']
map(lambda x : x['points']*10,  dict_a) # Output: [100, 80]
map(lambda x : x['name'] == "python", dict_a) # Output: [True, False]

list_a = [1, 2, 3]
list_b = [10, 20, 30]
map(lambda x, y: x + y, list_a, list_b) # Output: [11, 22, 33]

map_output = map(lambda x: x*2, [1, 2, 3, 4])
print(map_output) # Output: map object: <map object at 0x04D6BAB0>
list_map_output = list(map_output)
print(list_map_output) # Output: [2, 4, 6, 8]

# Filter
seq = [1, 2, 3, 4, 5]
result = list(filter(lambda x: x > 2, seq))
print(result)
[3, 4, 5]

a = [1, 2, 3, 4, 5, 6]
filter(lambda x : x % 2 == 0, a) # Output: [2, 4, 6]

dict_a = [{ ' name ' : ' python ' , ' points ' : 10 }, { ' name ' : ' java ' , ' points ' : 8 }]
filter ( lambda  x : x [ ' name ' ] ==  ' python ' , dict_a) # Wyjście: [{'name': 'python', 'points': 10}]


list_a = [1, 2, 3, 4, 5]
filter_obj =  filter ( lambda  x : x %  2  ==  0 , list_a) # obiekt filtru <filtr na 0x4e45890>
even_num =  list (filter_obj) # Konwertuje obiekt filer na listę
print (even_num) # Wyjście: [2, 4]
