import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn import model_selection
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
names = ['sepal-length','sepal-width','petal-length','petal-width','class']

dataset = pd.read_csv(url,names=names)

array = dataset.values

#split training and test set

X = array[:,0:4]
Y = array[:,4]
validation_size = 0.2

X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size)

models = []
models.append(('KNN', KNeighborsClassifier()))
models.append(('SVM', SVC()))
names = []
results = []

for name, model in models:
  kfold = model_selection.KFold(n_splits=10)
  cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold)
  names.append(name)
  results.append(cv_results)

for index, result in enumerate(results):
  print(str(names[index])+"----"+str(result[0]))
	
