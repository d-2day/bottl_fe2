items=input("Enter items: ").split()
ilen=len(items)
sum=0
for n in range(0,ilen):
    sum+=int(items[n])
avg=round(sum/ilen)
print("{}개 수의 합계: {}, 평군: {}".format(ilen,sum,avg))
