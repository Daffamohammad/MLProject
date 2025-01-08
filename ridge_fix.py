# -*- coding: utf-8 -*-
"""Ridge FIX

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1pa9FKNBZhg9XNeGSKhQKA20bINmVx57o

## Setup - Data Collecting ##
"""

from google.colab import drive
drive.mount('/content/drive', force_remount=False)

import pandas as pd
data= pd.read_csv('/content/drive/MyDrive/Dataset/kurs.csv')
data.head()

"""## Data Preprocessing ##"""

data['Date'] = pd.to_datetime(data['Date'], format='%m/%d/%Y')

if data['Rate'].dtype == object:
    data['Rate'] = data['Rate'].str.replace(',', '').astype(float)
else:
    data['Rate'] = data['Rate'].astype(float)

data = data.drop(columns=[col for col in data.columns if "NO" in col])

data.info()
data.head()

"""### Data Exploration ###"""

from matplotlib import pyplot as plt
import seaborn as sns
def _plot_series(series, series_name, series_index=0):
  palette = list(sns.palettes.mpl_palette('Dark2'))
  xs = series['Date']
  ys = series['Rate']

  plt.plot(xs, ys, label=series_name, color=palette[series_index % len(palette)])

fig, ax = plt.subplots(figsize=(14, 7), layout='constrained')
df_sorted = data.sort_values('Date', ascending=True)
_plot_series(df_sorted, '')
sns.despine(fig=fig, ax=ax)
plt.xlabel('Date')
_ = plt.ylabel('Rate')

data['Rate'].describe()

"""## Features ##"""

for lag in (1, 7, 21, 30):
    data[f'Lag_{lag}'] = data ['Rate'].shift(lag)
data.dropna(inplace=True)

"""## Model Prep ##"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
from datetime import datetime

data.set_index('Date', inplace=True)
all_dates = pd.date_range(start=data.index.min(), end=data.index.max(), freq='D')
df = data.reindex(all_dates)

for lag in   (1, 7, 21, 30):
    data[f'Lag_{lag}'] = data['Rate'].shift(lag)

data = data.dropna().reset_index()
data.rename(columns={'index': 'Date'}, inplace=True)
data.dropna(inplace=True)

split_date = datetime(2023,1,2)
train_data = data[data['Date'] <= split_date]
test_data = data[data['Date'] > split_date]


print(f"Training data: {train_data['Date'].min()} to {train_data['Date'].max()}")
print(f"Testing data: {test_data['Date'].min()} to {test_data['Date'].max()}")
print(f"Training data size: {len(train_data)}")
print(f"Testing data size: {len(test_data)}")


X_train = train_data.drop(['Rate', 'Date'], axis=1)
y_train = train_data['Rate']
X_test = test_data.drop(['Rate', 'Date'], axis=1)
y_test = test_data['Rate']

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

"""## Model Training and Evaluation ##"""

from sklearn.linear_model import Ridge

model= Ridge(alpha=200.0)
model.fit(X_train_scaled, y_train)
y_pred = model.predict(X_test_scaled)

"""### Evaluation ###"""

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"Mean Squared Error: {mse:.2f}")
print(f"R2 Score: {r2:.2f}")

###############################################################
coefficients = model.coef_
intercept = model.intercept_

print("Coefficients:")
for i, col in enumerate(X_train.columns):
    print(f"{col}: {coefficients[i]:.2f}")

print(f"Intercept: {intercept:.2f}")

from sklearn.model_selection import cross_val_score, KFold
kf = KFold(n_splits=5, shuffle=True, random_state=42)
scores = cross_val_score(model, X_train_scaled, y_train, cv=kf, scoring='neg_mean_squared_error')

mse_cv = -scores.mean()
print(f"Cross-Validated Mean Squared Error: {mse_cv:.2f}")

from statsmodels.stats.stattools import durbin_watson
residuals = y_test - y_pred
dw_stat = durbin_watson(residuals)
print(f"Durbin-Watson Statistic: {dw_stat}")

import matplotlib.pyplot as plt

plt.figure(figsize=(8, 6))
plt.scatter(y_pred, y_test - y_pred)
plt.axhline(y=0, color='r', linestyle='--')
plt.xlabel("Predicted Values")
plt.ylabel("Residuals")
plt.title("Residual Plot")
plt.show()

"""## Visualization ##"""

import matplotlib.pyplot as plt


print(f"Length of test_data['Date']: {len(test_data['Date'])}")
print(f"Length of y_test: {len(y_test)}")
print(f"Length of y_pred: {len(y_pred)}")


y_test_sliced = y_test[:len(test_data['Date'])]
y_pred_sliced = y_pred[:len(test_data['Date'])]


plt.figure(figsize=(14, 7))
plt.plot(test_data['Date'], y_test_sliced, label='Aktual', color='blue', marker='o', markersize=3)
plt.plot(test_data['Date'], y_pred_sliced, label='Prediksi', color='orange', marker='x', markersize=3)


plt.xlabel('Date', fontsize=12)
plt.ylabel('Kurs', fontsize=12)
plt.title('Aktual vs. Prediksi', fontsize=14)
plt.legend()
plt.grid(True)

plt.xticks(rotation=45)
plt.tight_layout()


plt.show()

plt.figure(figsize=(20, 7))

plt.plot(train_data['Date'], y_train, label='Training Data', color='green', marker='o', markersize=3)


plt.plot(test_data['Date'], y_test, label='Actual', color='blue', marker='o', markersize=3)

plt.plot(test_data['Date'], y_pred, label='Predicted', color='orange', marker='x', markersize=3)

plt.xlabel('Date', fontsize=12)
plt.ylabel('Kurs', fontsize=12)
plt.title('Training, Actual vs. Predicted', fontsize=14)
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()