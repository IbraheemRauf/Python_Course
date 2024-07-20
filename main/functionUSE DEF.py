def isgreater(a,b,c):
    if a>b and a>c :
        print (a,"is the greatest among the three values.")
    elif b>a and b>c :
        print (b,"is the greatest among the three values.")
    else :
        print (c,"is the greatest among the three values.")   
q1= int(input ( "firts value :")) 
q2= int(input ( "second value :")) 
q3= int(input ( "third value :")) 
isgreater(q1,q2,q3)
