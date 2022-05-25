import pandas as pd

df=pd.read_csv('temper.csv',encoding='euc-kr')
df=df.rename(columns={'평균기온(°C)':'중간기온(°C)'})
df['중간기온(°C)']=round(((df['최저기온(°C)']+df['최고기온(°C)'])/2),2)
df.to_csv('temper-m.csv',index=False,encoding='euc-kr')
