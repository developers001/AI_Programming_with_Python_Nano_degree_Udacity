def check(y):
    for i in y:
        if(i=="1" or i=="2" or i=="3" or i=="4" or i=="5" or i=="6" or i=="7" or i=="7" or i=="8" or i=="9" ):
            return True
            break
            

def check1(z):
    for i in z:   
        if(i=="#" or i=="$" or i=="@"):
            return True
            break
        else:
            return False

def check2(z):
    for i in z:   
        if i.isalpha():
            return True
            break
        else:
            return False
            

x=input("enter the password:")
o=len(x)
if( (check2(x)  and check(x)) and (check1(x) and (o>=6 and o<=16))):
    print("you succsefully build a password")
else:
    print("enter valid password")







