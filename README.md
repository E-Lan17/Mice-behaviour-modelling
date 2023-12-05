# Mice-behaviour-modelling
Mice behaviour modelling using ML and DL

The objective is to predict at what time of day (day/night) behaviors took place, based on recording of the mouse's activities over 24 hours.

Example of results of Elbow Method for the the K-means :
![Cluster](https://github.com/E-Lan17/Mice-behaviour-modelling/assets/81633998/d56c6a4e-70c0-4b58-a9d7-a0aafcbdb58e)

Example of cluster obtain with mice activities
![clustering 2](https://github.com/E-Lan17/Mice-behaviour-modelling/assets/81633998/d1bf158b-1525-49a0-86fc-4a35dc4f6aa0)

Example of selected parameters for each models and their predictions and accuracies : 

Data preprocessing :
    min_df : 0.000000 (0.000000 percent)
    Token max features : 2663.00 
    Duration: 0:00:00.148078 

Decision Tree Classifier : 
    {'Estimator__criterion': 'gini', 'Estimator__random_state': 42, 'Estimator__splitter': 'random', 'Selected_features__k': 'all'}
    Final cross_val_score on test data : 0.63 accuracy with a standard deviation of 0.02
    Duration: 0:00:40.740478 

K-Nearest Neighbors (K-NN) : 
    {'Estimator__algorithm': 'kd_tree', 'Estimator__metric': 'minkowski', 'Estimator__n_neighbors': 50, 'Estimator__p': 1.5, 'Estimator__weights': 'uniform', 'Selected_features__k': 'all'}
    Final cross_val_score on test data : 0.60 accuracy with a standard deviation of 0.01
    Duration: 0:12:33.730200 

Logistic Regression : 
    {'Estimator__C': 0.15, 'Estimator__max_iter': 2000, 'Estimator__random_state': 42, 'Estimator__solver': 'lbfgs', 'Selected_features__k': 'all'}
    Final cross_val_score on test data : 0.61 accuracy with a standard deviation of 0.01
    Duration: 0:00:03.913113 

Naive Bayes : 
    {'Selected_features__k': 'all'}
    Final cross_val_score on test data : 0.60 accuracy with a standard deviation of 0.01
    Duration: 0:00:03.385314 

Random Forest Classifier : 
    {'Estimator__criterion': 'gini', 'Estimator__n_estimators': 2663, 'Estimator__random_state': 42, 'Selected_features__k': 'all'}
    Final cross_val_score on test data : 0.61 accuracy with a standard deviation of 0.01
    Duration: 0:32:07.544594 

Support Vector Machine : 
    {'Estimator__degree': 2, 'Estimator__gamma': 'auto', 'Estimator__kernel': 'rbf', 'Estimator__random_state': 42, 'Selected_features__k': 'all'}
    Final cross_val_score on test data : 0.60 accuracy with a standard deviation of 0.00
    Duration: 0:05:23.375127 

Total Duration : 0:50:52.842306 
