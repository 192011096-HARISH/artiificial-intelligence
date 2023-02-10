import numpy as np
import pandas as pd
from sklearn import metrics 
df=pd.read_csv("PlayTennis.csv")
value=['Outlook','Temprature','Humidity','Wind']
df
from sklearn import preprocessing
string_to_int= preprocessing.LabelEncoder()                    
df=df.apply(string_to_int.fit_transform) 
df

feature_cols = ['Outlook','Temperature','Humidity','Wind']
X = df[feature_cols]                             
y = df.PlayTennis
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30) 
from sklearn.tree import DecisionTreeClassifier                             # import the classifier
classifier =DecisionTreeClassifier(criterion="entropy", random_state=100)     # create a classifier object
classifier.fit(X_train, y_train)  
y_pred= classifier.predict(X_test)  
from sklearn.metrics import accuracy_score
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
from sklearn.metrics import classification_report, confusion_matrix  
print(confusion_matrix(y_test, y_pred))  
print(classification_report(y_test, y_pred)) 
