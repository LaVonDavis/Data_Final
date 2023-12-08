
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import pandas as pd

df = pd.read_csv('clean_COL.csv')
scaler = StandardScaler()


cols = [7, 8, 9, 10, 11, 12, 13, 14]

df_scaled = scaler.fit_transform(df[df.columns[cols]])
components = 3

#try making a new array and adding componetnts to it

pca = PCA(n_components=components)

df_pca = pca.fit_transform(df_scaled)

explained_variance_ratio = pca.explained_variance_ratio_
print("Explained Variance Ratios:", explained_variance_ratio)

plt.bar(range(1, components + 1), explained_variance_ratio)
plt.xlabel("Principal Component")
plt.ylabel("Explained Variance Ratio")
plt.title("Scree Plot")
plt.show()
