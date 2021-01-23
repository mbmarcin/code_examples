from sklearn.datasets import load_boston
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Import data
boston = load_boston()
housing = pd.DataFrame(boston.data, columns=boston.feature_names)
housing['MEDV'] = boston.target
corr = housing.corr()
fig, ax = plt.subplots(figsize=(9,7))

# To make this look nicer slice off half of this since it duplicates information unecessarily otherwise
mask = np.zeros_like(corr, dtype=np.bool)  # returns an array of False values with same shape as corr dataframe
mask[np.triu_indices_from(mask)] = True  # creates a boolean mask by making half the zero values == True
ax = sns.heatmap(corr.round(2), mask=mask, ax=ax, annot=True, annot_kws={'fontsize':10}, cmap="RdYlGn")
ax.set_xticklabels(ax.xaxis.get_ticklabels(), fontsize=14)
ax.set_yticklabels(ax.yaxis.get_ticklabels(), fontsize=14);
