def fun(temp_a,temp_b): #take two strings and do the functions
    if (temp_a.isnumeric() and temp_b.isnumeric()):
        a= int(temp_a)
        b=int(temp_b)
        if b!=0:
            percent=a/b*100
        else:
            percent = 0
        print("{}\n{}\n{}\n{}%".format(a+b, a-b, a*b, int(percent)))
    elif (temp_a.isalpha() and temp_b.isalpha()):
        a=temp_a
        b=temp_b
        print(a+b)
        print("Other operations are not applicable")
    else:
        print(temp_a+temp_b)
        if (temp_a.isnumeric()):
            a=int(temp_a)
            print(a*temp_b)
        else:
            b=int(temp_b)
            print(b*temp_a)

x=input("enter input1: ")
y=input("enter input2: ")
fun(x,y)
