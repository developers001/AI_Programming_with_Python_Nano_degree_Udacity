word=input("enter a word:")
score=0
for i in word:
    if i == 'A'or i =='E' or i=='I' or i== 'O' or i =='U' or i=='L' or i == 'N' or i=='R' or i =='S' or i=='T' or i == 'a'or i =='e' or i=='i' or i== 'o' or i =='u' or i=='l' or i == 'n' or i=='r' or i =='s' or i=='t':
        score= score+1
    elif i == 'D' or i == 'G' or i == 'd' or i == 'g' :
        score=score+2
    elif i == 'B' or i == 'C' or i == 'M' or i == 'P'or i == 'b' or i == 'c' or i == 'm' or i == 'o':    
        score=score+3
    elif i == 'F' or i == 'H' or i == 'V' or i == 'W' or i=='Y' or i == 'f' or i == 'h' or i == 'v' or i == 'w' or i=='y':    
        score=score+4
    elif i == 'K' or i=='k':    
        score=score+5
    elif i == 'J' or i == 'X' or i == 'j' or i == 'x':    
        score=score+8
    elif i == 'Q' or i == 'Z' or i == 'q' or i == 'z' :    
        score=score+10
    else:
        score=score+0

print("your score is "  + str(score))
    
     