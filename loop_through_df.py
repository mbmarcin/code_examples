from datetime import datetime

start = datetime.now()
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randint(0, 10, size=(100000, 4)), columns=list('ABCD'))


def loop_with_for(df):
    temp = 0
    for index in range(len(df)):
        temp += df['A'].iloc[index] + df['B'].iloc[index]
    return temp


def loop_with_iterrows(df):
    temp = 0
    for _, row in df.iterrows():
        temp += row.A + row.B
    return temp


def loop_with_itertuples(df):
    temp = 0
    for row_tuple in df.itertuples():
        temp += row_tuple.A + row_tuple.B
        print(row_tuple)
    return temp


def loop_with_zip(df):
    temp = 0
    for a, b in zip(df['A'], df['B']):
        temp += a + b
    return temp


def using_apply(df):
    return df.apply(lambda x: x['A'] + x['B'], axis=1).sum()


def using_apply(df):
    return df.apply(lambda x: x['A'] + x['B'] + x['C'] + x['D'], axis=1).sum()


def using_apply_unpack(df):
    return df[['A', 'B', 'C', 'D']].apply(lambda x: sum([*x]), axis=1).sum()


def using_pandas_builtin(df):
    return (df['A'] + df['B']).sum()


# loop_with_itertuples(df)
# loop_with_zip(df)
# using_apply(df)
# using_pandas_builtin(df)

print(datetime.now() - start)
