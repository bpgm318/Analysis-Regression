from data import df
import numpy as np
import matplotlib.pyplot as plt

apr = np.array(df.April)
may = np.array(df.May)
june = np.array(df.June)
allData = np.concatenate((apr, may, june))

index = []
for i in range(135):
    index.append(i)




plt.xlabel('Point Index (Starting from First Year in April to Last Year in June)')
plt.ylabel('Snow (Million Square Kilometers)')
plt.plot(index, allData)
plt.show()