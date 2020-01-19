import pandas as pd

df = pd.DataFrame({'foo': ['one', 'kl'],
                   'bar': ['A', 'B'],
                   'baz': [1, 3],
                   'zoo': [2, 3]})

vb = {'x': df.iloc[:1, 3].to_list()}
vb_ = {'c': df.iloc[:1, 2].to_list()}

print(
    {**vb, **vb_}
)
