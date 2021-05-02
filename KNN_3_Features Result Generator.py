import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.model_selection import cross_val_score


from sklearn.neighbors import KNeighborsClassifier
#from sklearn.discriminant_analysis import LinearDiscriminantAnalysis 
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.model_selection import cross_val_score
#from sklearn.tree import DecisionTreeClassifier
#from sklearn.svm import SVC
#from sklearn.linear_model import LogisticRegression



dataset = pd.read_csv("iris.csv")

all_columns = ['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']
resultsArra = []

neighborsNumber=4
test_sizeNumber=0.7

count=1
for a in all_columns:
  for b in all_columns:
      for c in all_columns:    
          if a!=b and b!=c and a!=c :
              feature_columns = [a,b,c]
              print("Featured Columns : ",feature_columns)
              print(count)
              count=count+1
              X = dataset[feature_columns].values
              y = dataset['Species'].values
              # Apply numerical encoding to convert alphabetical names
              le = LabelEncoder()
              y = le.fit_transform(y)
              # Divide the dataset in testing and training vectors for cross-validation
              X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = test_sizeNumber, random_state = 0)
              # Instantiate learning model (k = 3)
              classifier = KNeighborsClassifier(n_neighbors=neighborsNumber)
              # Fitting the model
              classifier.fit(X_train, y_train)
              # Predicting the Test set results
              y_pred = classifier.predict(X_test)
              
              classifier = KNeighborsClassifier(n_neighbors=neighborsNumber)
              #classifier = LinearDiscriminantAnalysis()
              #classifier = DecisionTreeClassifier()
              #classifier = SVC(gamma = 'auto')
              #classifier = LogisticRegression()
              # Fitting the model
              classifier.fit(X_train, y_train)
              
              # Predicting the Test set results
              y_pred = classifier.predict(X_test)
              
              # View the accuracy of the model
              accuracy = accuracy_score(y_test, y_pred)*100
              print('Accuracy of our model is equal ' + str(round(accuracy, 2)) + ' %.')
              
              a_temp =""
              b_temp =""
              c_temp =""
              if a== "SepalLengthCm":
                  a_temp="SL"
              if a== "SepalWidthCm":
                  a_temp="SW"
              if a== "PetalLengthCm":
                  a_temp="PL"
              if a== "PetalWidthCm":
                  a_temp="PW"
              
              if b== "SepalLengthCm":
                  b_temp="SL"
              if b== "SepalWidthCm":
                  b_temp="SW"
              if b== "PetalLengthCm":
                  b_temp="PL"
              if b== "PetalWidthCm":
                  b_temp="PW"
                  
              if c== "SepalLengthCm":
                  c_temp="SL"
              if c== "SepalWidthCm":
                  c_temp="SW"
              if c== "PetalLengthCm":
                  c_temp="PL"
              if c== "PetalWidthCm":
                  c_temp="PW"
              
                  
              tempArr =  [a_temp,b_temp,c_temp,round(accuracy, 3)]
          
              resultsArra.append(tempArr)

#NOW WRITING ON CSV FILE

with open('3FeatureResults/Resut_with_n_'+str(neighborsNumber)+'_testSize_'+str(test_sizeNumber)+'_3_features.csv', mode='w',newline='') as csv_file:
    fieldnames = ['Feature A', 'Feature B','Feature C' ,'Accuracy']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
    writer.writeheader()
    for row in resultsArra:
        #writer.writerow({row[]})
        writer.writerow({'Feature A': row[0], 'Feature B': row[1],'Feature C': row[2], 'Accuracy': row[3]})
        #print(row[0])
        
