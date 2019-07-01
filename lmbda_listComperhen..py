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






#Lambda Functions
double = lambda x: x * 2
print(double(5))


#Map and Filter
# Map
seq = [1, 2, 3, 4, 5]
result = list(map(lambda var: var*2, seq))
print(result)
[2, 4, 6, 8, 10]


# Filter
seq = [1, 2, 3, 4, 5]
result = list(filter(lambda x: x > 2, seq))
print(result)
[3, 4, 5]


