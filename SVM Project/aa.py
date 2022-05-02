# %%
import pandas as pd

# %%
data = pd.read_csv('dataset.csv')

# %%
print("Data: ")
print(data.head())

# %%
print("Check for null values if any")
print(data.isna().sum())

# %%
print(data.info())

# %%
X = data.iloc[:,:-1]
y = data.iloc[:,-1]

# %%
from sklearn.model_selection import train_test_split

# %%
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=109)

# %%
from sklearn import svm

# %%
clf = svm.SVC(kernel='linear')
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

# %%
from sklearn import metrics

print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

# %%



