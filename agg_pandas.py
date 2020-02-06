def top(df, n=5, column='tip_pct'):
	return df.sort_values(by=column)[-n:]

top(tips, n=6)


tips.groupby(['smoker', 'day']).apply(top, n=1, column='total_bill')




grouped.agg({'tip_pct' : ['min', 'max', 'mean', 'std'],'size' : 'sum'})
grouped.agg({'tip' : np.max, 'size' : 'sum'})




functions = ['count', 'mean', 'max']
result = grouped['tip_pct', 'total_bill'].agg(functions)


grouped_pct.agg([('foo', 'mean'), ('bar', np.std)])


def norm_total(group):
group['normed_total'] = group.total / group.total.sum()
return group
results = count_subset.groupby('tz').apply(norm_total)
