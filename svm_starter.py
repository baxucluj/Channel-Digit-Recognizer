import pandas as pd
import matplotlib.pyplot as plt  
from sklearn import svm
from sklearn import metrics
import joblib
import numpy as np
from sklearn.utils import shuffle


##Step 1: Get Data from CSV
dataframe = pd.read_csv("csv/dataset5labels.csv")
dataframe = dataframe.sample(frac=1).reset_index(drop=True)
print(dataframe)

##Step 2: Seperate Labels and Features
X = dataframe.drop(['label'],axis=1)
print(X)
Y = dataframe["label"]
print(Y)

X_train, Y_train = X[0:164], Y[0:164]
X_test, Y_test = X[164:], Y[164:]




##Step 3: Build a Model and Save it
model = svm.SVC(kernel="linear")
model.fit(X_train,Y_train)
joblib.dump(model,"model/svm_5label_linear")

##Step4 : Print Accuracy 
predction = model.predict(X_test)
#print(type(predction[0]))
print("Model Score/Accuracy is", metrics.accuracy_score(Y_test,predction))
#print(predction)