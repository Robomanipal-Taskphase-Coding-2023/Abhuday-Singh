import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn import preprocessing
import seaborn as sns

data = pd.read_csv("/Users/abhudaysingh/Downloads/weatherAUS.csv")
X = data.drop('Date', axis=1)
correlation_matrix = X.corr()
# Visualize the correlation matrix using a heatmap
plt.figure(figsize=(12, 10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
plt.title('Correlation Matrix')
plt.show()

X = X.drop('Pressure9am',axis =1)

print(X.head())
print(X.shape)

X_scaled = preprocessing.scale(X.T)
num_components = min(X.shape[0], X.shape[1])  

pca = PCA(n_components=num_components)
X_pca = pca.fit_transform(X_scaled)
per_var = np.round(pca.explained_variance_ratio_* 100, decimals=1)

labels = ['PC' + str(x) for x in range(1, len(per_var)+1)]
 
plt.bar(x=range(1,len(per_var)+1), height=per_var, tick_label=labels)
plt.ylabel('Percentage of Explained Variance')
plt.xlabel('Principal Component')
plt.title('Screen Plot')
plt.show()

plt.plot(range(1,22),pca.explained_variance_ratio_.cumsum(),marker = 'o')
plt.xlabel("no. of components")
plt.ylabel("cumulative explained variance")
plt.show()

pca1 = PCA(n_components=2)
pca.fit(X_pca)
pca.transform(X_pca)

def kmeans(data, k, nstart):
    np.random.seed(0)
    centers = data[np.random.choice(range(len(data)), k, replace=False)]
    for _ in range(nstart):
        distances = np.linalg.norm(data[:, np.newaxis] - centers, axis=2)
        labels = np.argmin(distances, axis=1)
        new_centers = np.array([data[labels == i].mean(axis=0) for i in range(k)])
        if np.all(centers == new_centers):
            break
        centers = new_centers

    wcss = 0
    for i in range(k):
        cluster_points = data[labels == i]
        wcss += np.sum(np.linalg.norm(cluster_points - centers[i], axis=1)**2)
    
    return labels, wcss

def plot_wcss(data, max_k, nstart):
    wcss_values = []
    
    for k in range(1, max_k + 1):
        _, wcss = kmeans(data, k, nstart)
        wcss_values.append(wcss)
    
    # Plotting the Elbow Method
    plt.plot(range(1, max_k + 1), wcss_values, marker='o')
    plt.title('Elbow Method For Optimal k')
    plt.xlabel('Number of Clusters (k)')
    plt.ylabel('WCSS')
    plt.show()

plot_wcss(pca.transform(X_pca),20,25)

c1,wcss1 = kmeans(pca.transform(X_pca),2,25)
plt.scatter(pca.transform(X_pca)[:, 0], pca.transform(X_pca)[:, 1], c=c1)
plt.show()
print("The Within-Cluster Sum of Square is",wcss1)
