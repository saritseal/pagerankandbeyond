from sklearn.linear_model import LinearRegression
import sklearn.datasets as ds 
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
from scipy.stats import binom


data = sns.load_dataset('iris')
sns.pairplot(data, hue='species')


rng = np.random.RandomState(123)

rng.seed(10)

beta_dis = rng.beta(10, 100, (100, 2))
x, y = beta_dis[:, 0], beta_dis[:, 1]

sns.pairplot(pd.DataFrame(beta_dis))

plt.hist(x, x.shape[0])
plt.hist(y)

binomial_dist = rng.binomial(50, 0.5, 1000000)

plt.hist(binomial_dist)


x = np.abs(2.5 * rng.randn(100) + 3)

y = np.abs(2 * x -10)

sns.scatterplot(x, y)

model = LinearRegression(fit_intercept=True, normalize=True, n_jobs=1)
lr_esti = model.fit(x[:, np.newaxis], y)

t = np.linspace(0, 5, len(x))
pred = lr_esti.predict(t[:, np.newaxis])

plt.scatter(x, y)
plt.plot(t[:, np.newaxis], pred)

from sklearn.datasets import load_boston  

boston = load_boston()
boston.keys()
boston.data
boston.feature_names

df = pd.DataFrame(boston.data, columns=boston.feature_names)
df.head()

df['TGT']=boston.target

boston.feature_names

X = pd.DataFrame(np.c_[df['LSTAT'], df['RM']], columns = ['LSTAT', 'RM'])
Y = boston['TGT']

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=.2, random_state= 5)
boston_housing = model.fit(X_train, Y_train)

Yhat_train = boston_housing.predict(X_train)
rmse = np.sqrt(mean_squared_error(Y_train, Yhat_train))
r2 = r2_score(Y_train, Yhat_train)
print("train", rmse, r2)

Yhat_test = boston_housing.predict(X_test)
rmse = np.sqrt(mean_squared_error(Y_test, Yhat_test))
r2 = r2_score(Y_test, Yhat_test)
print("test", rmse, r2)

X = pd.DataFrame(np.c_[df['LSTAT'], df['RM']], columns = ['LSTAT', 'RM'])
Y = boston['TGT']

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from sklearn.metrics import accuracy_score

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=.2, random_state= 5, shuffle=True)
boston_housing = model.fit(X_train, Y_train)

Yhat_train = boston_housing.predict(X_train)
rmse = np.sqrt(mean_squared_error(Y_train, Yhat_train))
r2 = r2_score(Y_train, Yhat_train)
print("train", rmse, r2)
print("train-acc", accuracy_score(Y_train, Yhat_train))

Yhat_test = boston_housing.predict(X_test)
rmse = np.sqrt(mean_squared_error(Y_test, Yhat_test))
r2 = r2_score(Y_test, Yhat_test)
print("test", rmse, r2)

plt.scatter(X_train['LSTAT'], Y_train, c='r')
plt.scatter(X_train['RM'], Y_train, c='g')
plt.scatter(X_test['LSTAT'], Y_test, c='b')
plt.scatter(X_test['RM'], Y_test, c='w')




if __name__ == '__main__':
    pass
















