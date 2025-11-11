import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error

df = pd.read_csv("Uber.csv")

df["pickup_datetime"] = pd.to_datetime(df["pickup_datetime"])
df.dropna(inplace=True)

q1 = df["fare_amount"].quantile(0.25)
q3 = df["fare_amount"].quantile(0.75)
iqr = q3 - q1
thr = 1.5
lb = q1 - thr * iqr
ub = q3 + thr * iqr
df_no = df[(df["fare_amount"] >= lb) & (df["fare_amount"] <= ub)]

sns.boxplot(x=df_no["fare_amount"])
plt.title("Fare Amount Distribution without Outliers")
plt.show()

df_no = df_no.select_dtypes(include=[np.number])

corr_m = df_no.corr()
sns.heatmap(corr_m, annot=True)
plt.title("Correlation Heatmap")
plt.show()

X = df_no[['pickup_longitude', 'pickup_latitude', 'dropoff_longitude', 'dropoff_latitude', 'passenger_count']]
y = df_no['fare_amount']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

lr_model = LinearRegression()
lr_model.fit(X_train, y_train)
y_pred_lr = lr_model.predict(X_test)
r2_lr = r2_score(y_test, y_pred_lr)
rmse_lr = np.sqrt(mean_squared_error(y_test, y_pred_lr))

rf_model = RandomForestRegressor(n_estimators=1, warm_start=True, random_state=42)
n_trees = 15
for i in range(1, n_trees + 1):
    rf_model.n_estimators = i
    rf_model.fit(X_train, y_train)
    print(f"Tree {i} trained")

y_pred_rf = rf_model.predict(X_test)
r2_rf = r2_score(y_test, y_pred_rf)
rmse_rf = np.sqrt(mean_squared_error(y_test, y_pred_rf))

print("Linear Regression R2:", r2_lr)
print("Linear Regression RMSE:", rmse_lr)
print("Random Forest Regression R2:", r2_rf)
print("Random Forest Regression RMSE:", rmse_rf)
