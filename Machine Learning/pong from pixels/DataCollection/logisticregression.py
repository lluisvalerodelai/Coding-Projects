import numpy as np
import random as r
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler


X = np.load(r'C:\Users\35840\Desktop\Luis Code\train\imgs.npy')
y = np.load(r'C:\Users\35840\Desktop\Luis Code\train\presses.npy')

scaler = MinMaxScaler().fit(X, y)

scaler.transform(X)

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=123)
x_train, x_test, y_train, y_test = np.array(x_train), np.array(x_test), np.array(y_train), np.array(y_test)



logreg = LogisticRegression(solver='lbfgs')

logreg.max_iter = 10000

logreg.fit(x_train, y_train.T)


def predict(X):
    return logreg.predict(X)



