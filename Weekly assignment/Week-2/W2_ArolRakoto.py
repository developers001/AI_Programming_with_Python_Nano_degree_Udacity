def number(a, b):
  # All input are number
  if isinstance(a, (int, float)) and isinstance(b, (int,float)):
    if b !=0:
      print((a+b),(a-b),(b+b),(round((a/b)*100,2),"%"))
    else:
      print("operations are not applicable")
  # All input are string  
  elif isinstance(a, (str)) and isinstance(b, (str)):
    print("{} {},Other operations are not applicable".format(a,b))
  # All input are number and string
  else:
    print(str(a)+str(b), str(b)*2)
    

number(2,3)
number('Hi', "Raju")
number(2,"Raju")