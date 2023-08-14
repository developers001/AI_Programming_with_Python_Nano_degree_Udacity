st={}
d1 = {'a':100, 'b':200, 'c':300}
d2 = {'a':300, 'b':200, 'd':400}
for key1,value1 in d1.items():
    for key2,value2 in d2.items():
        if key1==key2:
            st[key1]=value1+value2
        if key1!=key2:
            st[key1]=value1
            st[key2]=value2
print("Counter("+str(st)+")")

