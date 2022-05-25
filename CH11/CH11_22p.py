import csv

with open('temper.csv','r',newline='') as f_in:
    with open('temper-m.csv','w',newline='') as f_out:
        data=csv.reader(f_in)
        outcsv=csv.writer(f_out)
        header=next(data)
        header[3]="중간기온(℃)"
        outcsv.writerow(header)

        for row in data:
            if not row: break
            row[3]=str(round(float(row[4])+float(row[5])))
            outcsv.writerow(row)
                       
