import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import RobustScaler

pd.set_option('float_format', '{:f}'.format)

# Use the same random seed to get the same result
np.random.seed(32)

#StandardScaler for Gaussian distributions
df = pd.DataFrame({
    'col1': np.random.normal(5, 2, 30000),
    'col2': np.random.normal(20, 5, 30000),
    'col3': np.random.normal(-5, 3, 30000)
})

col_names = df.columns
features = df[col_names]

scaler = StandardScaler().fit(features.values)
features = scaler.transform(features.values)
scaled_features = pd.DataFrame(features, columns = col_names)
print('Check if mean is ~ 0 and std ~ 1',scaled_features.describe())

fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(10, 5))

ax1.set_title('Before Scaling')
sns.kdeplot(df, ax=ax1, lw = 3)
ax2.set_title('After Standard Scaler')
sns.kdeplot(scaled_features, ax=ax2, lw = 3)
plt.tight_layout()
plt.show()

#MinMaxScaler for non-Gaussian distributions
df = pd.DataFrame({
    # positive skew
    'col1': np.random.chisquare(8, 1000),
    # negative skew 
    'col2': np.random.beta(8, 2, 1000) * 40,
    # no skew - Gaussian distribution
    'col3': np.random.normal(50, 3, 1000)
})

col_names = df.columns
features = df[col_names]

scaler = MinMaxScaler().fit(features.values)
features = scaler.transform(features.values)
scaled_features = pd.DataFrame(features, columns = col_names)
scaled_features.head()

fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(10, 5))

ax1.set_title('Before Scaling')
sns.kdeplot(df, ax=ax1, lw = 3)
ax2.set_title('After MinMax Scaler')
sns.kdeplot(scaled_features, ax=ax2, lw = 3)
plt.tight_layout()
plt.show()


#Comparing StandardScaler, MinMaxScaler, and RobustScaler for Gaussian distributions with outliers
df = pd.DataFrame({
    #Normal Distribution with lower outliers
    'col1': np.concatenate([np.random.normal(20, 2, 1000), np.random.normal(3, 1, 25)]),
    #Normal Distribution with higher outliers
    'col2': np.concatenate([np.random.normal(55, 3, 1000), np.random.normal(70, 2, 25)]),
})

df.head()

#StandardScaler
col_names = df.columns
features = df[col_names]
scaler = StandardScaler().fit(features.values)
features = scaler.transform(features.values)
standard_scaler = pd.DataFrame(features, columns = col_names)

#MinMaxScaler
col_names = df.columns
features = df[col_names]
scaler = MinMaxScaler().fit(features.values)
features = scaler.transform(features.values)
min_max_scaler = pd.DataFrame(features, columns = col_names)

#RobustScaler
col_names = df.columns
features = df[col_names]
scaler = RobustScaler().fit(features.values)
features = scaler.transform(features.values)
robust_scaler = pd.DataFrame(features, columns = col_names)

fig, (ax1, ax2, ax3, ax4) = plt.subplots(ncols=4, figsize=(15, 7))

ax1.set_title('Before Scaling')
sns.kdeplot(df, ax=ax1, lw = 3)

ax2.set_title('After Standard Scaler')
sns.kdeplot(standard_scaler, ax=ax2, lw = 3)

ax3.set_title('After MinMax Scaler')
sns.kdeplot(min_max_scaler, ax=ax3, lw = 3)

ax4.set_title('After Robust Scaler')
sns.kdeplot(robust_scaler, ax=ax4, lw = 3)
plt.tight_layout()
plt.show()