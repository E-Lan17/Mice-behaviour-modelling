# K-Means Clustering

# Importing the libraries
from datetime import datetime
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Create a timer :       
start_time = datetime.now()

# Importing the Cluster_data.csv
dataset = pd.read_csv('Cluster_data.csv')
# print(dataset)

## Frequency encoding :
    
# size of each category (number of time each activity appears) :
encoding = dataset.groupby('Activities').size()
# print(encoding)

# get frequency of each category, add it to dataframe and replace the order of index :
encoding = encoding/len(dataset)
dataset['Encode'] = dataset.Activities.map(encoding)
dataset = dataset[["Duration", "Activities", "Encode", "Day"]]
#print(dataset)

# Select the column the dataset
X = dataset.iloc[:,[2, 3]].values


wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 42)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)
plt.plot(range(1, 11), wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()



# Number of cluster :
N = 2

# Training the K-Means model on the dataset
kmeans = KMeans(n_clusters = N, init = 'k-means++', random_state = 42)
y_kmeans = kmeans.fit_predict(X)

# Visualising the clusters
plt.scatter(X[y_kmeans == 0, 0], X[y_kmeans == 0, 1], s = 100, c = 'red', label = 'Cluster 1')
plt.scatter(X[y_kmeans == 1, 0], X[y_kmeans == 1, 1], s = 100, c = 'blue', label = 'Cluster 2')
plt.scatter(X[y_kmeans == 2, 0], X[y_kmeans == 2, 1], s = 100, c = 'green', label = 'Cluster 3')
plt.scatter(X[y_kmeans == 3, 0], X[y_kmeans == 3, 1], s = 100, c = 'cyan', label = 'Cluster 4')
plt.scatter(X[y_kmeans == 4, 0], X[y_kmeans == 4, 1], s = 100, c = 'magenta', label = 'Cluster 5')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s = 300, c = 'yellow', label = 'Centroids')
plt.title('Clusters of activities')
#plt.xlabel('Annual Income (k$)')
#plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.show()

#Add the cluster to the dataset and display the activities by cluster :
cluster_map = dataseret
cluster_map['cluster'] = y_kmeans
df_cluster = pd.DataFrame()

for i in range(N) :
    df_cluster = df_cluster.append(cluster_map[cluster_map.cluster == i])

# Create a dictionary with the sorted activities with value 0 for each key :
dict_cluster = { i : None for i in range(N) }
for i in range(len(df_cluster)) :
        if dict_cluster[df_cluster.iloc[i,4]] == None :
            dict_cluster[df_cluster.iloc[i,4]] = df_cluster.iloc[i,1]
        if df_cluster.iloc[i,1] not in dict_cluster[df_cluster.iloc[i,4]] :  
            dict_cluster[df_cluster.iloc[i,4]] = dict_cluster[df_cluster.iloc[i,4]] +" " + df_cluster.iloc[i,1]
                        
# Create new file with a dict .txt (change dict name):   
with open("Cluster.txt", 'w') as filehandle:  
    for key, value in dict_cluster.items():  
        filehandle.write('%s:%s\n' % (key, value))
 
# End timer and display it :
end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))
        
