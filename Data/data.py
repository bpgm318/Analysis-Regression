import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')
import statistics

df = pd.read_csv('SnowData.csv')

#Means

aprilMean = df.April.mean()
mayMean = df.May.mean()
juneMean = df.June.mean()

#Standard Deviations

aprilStd = df.April.std()
mayStd = df.May.std()
juneStd = df.June.std()

#Variations (square of std)

aprilVar = (aprilStd)**2
mayVar = (mayStd)**2
juneVar = (juneStd)**2

#Medians

aprilMed = statistics.median(df.April)
mayMed = statistics.median(df.May)
juneMed = statistics.median(df.June)

#Store Statistics in dataframe

stats = {'Month': ['April', 'May', 'June'],
          'Mean': [aprilMean, mayMean, juneMean],
         'Median' : [aprilMed, mayMed, juneMed],
         'Standard Deviation': [aprilStd, mayStd, juneStd],
         'Variance': [aprilVar, mayVar, juneVar]
          }

dfStats = pd.DataFrame(stats)

print(dfStats)


plt.xlabel('Year')
plt.ylabel('Snow (Million Square Kilometers)')
plt.title('Snowfall')
plt.plot(df.Year,df.April, color = 'b')
plt.plot(df.Year,df.May, color = 'g')
plt.plot(df.Year,df.June, color = 'r')
plt.legend()
plt.show()

