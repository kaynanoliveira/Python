# Implementar uma solução em Python para estudar o comportamento de uma série temporal com Regressão Linear.

import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

x = np.array([5, 10, 15, 20, 25, 30]).reshape((-1, 1))
y = np.array([6, 12, 14, 23, 27, 32])

model = LinearRegression().fit(x, y)

y_pred = model.predict(x)
print("Dados do Teste:", y, sep='\n')
print("Dados de Predição:", y_pred, sep='\n')

plt.scatter(x, y,c="blue")
plt.plot(x, y_pred,c="red")
plt.legend('Predição','Real')
plt.show()