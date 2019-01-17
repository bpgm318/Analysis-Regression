import numpy as np
from sklearn.linear_model import LinearRegression
from data import df
import matplotlib.pyplot as plt

year = np.array(df.Year).reshape(-1,1)




regApr = LinearRegression()
regApr.fit(year,df.April)

regMay = LinearRegression()
regMay.fit(year,df.May)

regJune = LinearRegression()
regJune.fit(year,df.June)

labels = ['April', 'May', 'June']

plt.xlabel('Year')
plt.ylabel('Snow (Million Square Kilometers)')
plt.title('Regression')
plt.plot(df.Year, regApr.predict(df.Year[:, np.newaxis]), 'b')
plt.plot(df.Year, regMay.predict(df.Year[:, np.newaxis]), 'g')
plt.plot(df.Year, regJune.predict(df.Year[:, np.newaxis]), 'r')
plt.legend(labels)
plt.show()
