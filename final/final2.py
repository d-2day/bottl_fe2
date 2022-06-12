import pandas as pd
grade_data=[[23,31,47],[32,33,21],[21,24,32]]
df=pd.DataFrame(grade_data,columns=['반응','분리','환경'],index=['수호','성진','준수'])
print(df)
t1,t2,t3=df.sum(axis=1)
df['총점']=[t1,t2,t3]
print(df)
df.to_excel('final2.xlsx',index=False)
