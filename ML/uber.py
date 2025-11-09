
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from math import radians, sin, cos, asin, sqrt



df = pd.read_csv("/content/uber.csv")
df.head()





df = df.dropna()

# convert datetime
df['pickup_datetime'] = pd.to_datetime(df['pickup_datetime'])

# extract parts
df['pickup_hour'] = df['pickup_datetime'].dt.hour
df['pickup_month'] = df['pickup_datetime'].dt.month
df['pickup_weekday'] = df['pickup_datetime'].dt.weekday

# haversine distance
def haversine(lat1, lon1, lat2, lon2):
    lat1, lon1, lat2, lon2 = map(np.radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = np.sin(dlat/2)**2 + np.cos(lat1)*np.cos(lat2)*(np.sin(dlon/2)**2)
    return 6371 * 2 * np.arcsin(np.sqrt(a))

df['distance_km'] = haversine(
    df['pickup_latitude'], df['pickup_longitude'],
    df['dropoff_latitude'], df['dropoff_longitude']
)

# final clean filters
df = df[(df['fare_amount'] > 0) & (df['fare_amount'] < 200)]
df = df[(df['distance_km'] > 0) & (df['distance_km'] < 100)]
df = df[(df['passenger_count'] >= 1) & (df['passenger_count'] <= 6)]







X = df[['distance_km', 'passenger_count']]
y = df['fare_amount']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)








# scale ONLY distance + passenger_count for LR
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Linear Regression
lr = LinearRegression()
lr.fit(X_train_scaled, y_train)
y_pred_lr = lr.predict(X_test_scaled)

# Random Forest (no scaling needed)
rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)
y_pred_rf = rf.predict(X_test)






def predict_fare(distance_km, passenger_count):
    inp = pd.DataFrame([{
        "distance_km": distance_km,
        "passenger_count": passenger_count
    }])

    # LR uses scaled input
    lr_pred = lr.predict(scaler.transform(inp))[0]

    # RF uses raw input
    rf_pred = rf.predict(inp)[0]

    return lr_pred, rf_pred





print("Enter values to predict Uber fare:")

d = float(input("Distance (km): "))
p = int(input("Passenger count: "))

fare_lr, fare_rf = predict_fare(d, p)

print("\n=== PREDICTED FARE ===")
print(f"Linear Regression: ${fare_lr:.2f}")
print(f"Random Forest:     ${fare_rf:.2f}")