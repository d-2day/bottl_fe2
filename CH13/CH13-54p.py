import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_excel('일일환율표.xlsx')

plt.bar(df.통화표시, df.매매기준율)
plt.title('2019/7/23 rate')
plt.show()
