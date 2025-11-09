import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans



Cell 2 — Load & pick numeric features


# Change path if needed (e.g., '/content/sales_data_sample.csv')
df = pd.read_csv('/content/sales_data_sample.csv', encoding='ISO-8859-1')

# Select a compact, useful numeric set
features = ['SALES', 'PRICEEACH', 'QUANTITYORDERED', 'MSRP']
X = df[features].dropna().copy()

# Scale
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)





Cell 3 — Elbow method (auto-suggest K)


inertias = []
K = range(1, 11)
for k in K:
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    km.fit(X_scaled)
    inertias.append(km.inertia_)

plt.plot(K, inertias, 'o-')
plt.xlabel('k'); plt.ylabel('WCSS (inertia)'); plt.title('Elbow Method')
plt.show()

# Simple knee heuristic (largest relative drop)
drops = np.diff(inertias)
rel_drop = -drops / np.array(inertias[:-1])
optimal_k = 1 + np.argmax(rel_drop) + 1  # +1 for diff shift, +1 because k starts at 1
print("Suggested k (elbow):", optimal_k)



Cell 4 — Fit K-Means with chosen K and inspect



k = optimal_k  # or set manually, e.g., k = 3
kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
labels = kmeans.fit_predict(X_scaled)

X_out = X.copy()
X_out['Cluster'] = labels
print(X_out['Cluster'].value_counts().sort_index())

# Cluster centers (back to original scale)
centers = pd.DataFrame(
    scaler.inverse_transform(kmeans.cluster_centers_),
    columns=features
)
print("\nCluster Centers (original scale):\n", centers.round(2))




Cell 5 — Quick 2D plot (SALES vs PRICEEACH)



plt.scatter(X['SALES'], X['PRICEEACH'], c=labels, s=15)
plt.xlabel('SALES'); plt.ylabel('PRICEEACH'); plt.title('K-Means Clusters')
plt.show()