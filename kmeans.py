import pandas as pd 
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from scipy.cluster.hierarchy import dendrogram,linkage,fcluster
df = pd.read_csv('sales.csv',encoding = 'latin1')
print('data loaded successfully!')
print(df.head())
print(df.describe)
print(df.shape)
numeric_cols=df.select_dtypes(include=['int64','float64']).columns
X=df[numeric_cols]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
wcss=[]
for i in range(1,11):
  kmeans=KMeans(n_clusters=i,random_state=42)
  kmeans.fit(X_scaled)
  wcss.append(kmeans.inertia_)

plt.figure(figsize=(8,6))
plt.plot(range(1,11),wcss,marker='o')
plt.title('Elbow Method')
plt.xlabel('clusters')
plt.ylabel('wcss')
plt.plot()
k=4
kmeans = KMeans(n_clusters=k,random_state=42)
df['KMeans-Cluster']=kmeans.fit_predict(X_scaled)
print("\nK-Means Clustering result:")
print(df.head())

linked = linkage(X_scaled, method='ward')

plt.figure(figsize=(10, 7))
dendrogram(linked, orientation='top', distance_sort='descending', show_leaf_counts=True)
plt.title('Hierarchical Clustering Dendrogram')
plt.show()

# Assign clusters (cut dendrogram at k clusters)
df['Hier_Cluster'] = fcluster(linked, k, criterion='maxclust')
print("\nHierarchical Clustering result:")
print(df.head())




