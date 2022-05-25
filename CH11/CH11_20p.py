f_in=open('temper.csv','r',newline='')
f_out=open('temper-m.csv','w',newline='')

header=f_in.readline()
new_header=header.replace("평균","중간")
f_out.write(new_header)

for row in f_in:
    if row=='\r\n': break
    rowLst=row.split(',')
    rowLst[3]=str(round((float(rowLst[4])+float(rowLst[5]))/2,2))
    f_out.write(','.join(rowLst))

f_in.close()
f_out.close()
