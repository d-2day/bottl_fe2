with open('temper.csv','r',newline='') as f_in:
    with open('temper-m.csv','w',newline='') as f_out:
        header=f_in.readline()
        new_header=header.replace("평균","중간")
        f_out.write(new_header)
        for row in f_in:
            if row=='\r\n': break
            rowLst=row.split(',')
            rowLst[3]=str(round((float(rowLst[4])+float(rowLst[5]))/2,2))
            f_out.write(','.join(rowLst))
