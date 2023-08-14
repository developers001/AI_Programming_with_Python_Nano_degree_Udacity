lst=[1,2,3,4,5]
sum=0
for i in lst:
    sum=i+sum
print("SUM :" + str(sum))
print("MAX :" +str(max(lst)))
print("MIN :" +str(min(lst)))
avg=sum/len(lst)
print("MEAN :" +str(avg))
