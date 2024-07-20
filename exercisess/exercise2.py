listofquestions = ["who is the prime miniter of pakistan?  ","who is the cm of punjab?  ","who won 2024 t20 world cup?  "]
listofanswers = [ "imran khan", "maryam nawaz", "india"]
a1 = "5crore"
a2 = "10crore"
a3 = "20000000000000000000crore"



print("KON BANE GA CRORE PATII".center(100))

name  = input("ENTER YOUR NAME : ")
print("welcome to KBC.",name," I am sure that you know all the rules of KBC by MUHAMMAD IBRAHHEM , here is your first question" )

pk1 = input(listofquestions[0].capitalize())
if pk1.lower() == listofanswers[0]:
    print ("->Correct answer , you won ".capitalize(),a1,"pkr".capitalize())
    pk2 = input(listofquestions[1].capitalize())
    if pk2.lower() == listofanswers[1]:
        print ("->Correct answer , you won ",a2,"pkr")
    else :
        print ("Better luck next time ".capitalize())

    pk3 = input(listofquestions[2].capitalize())     
    if pk3.lower() == listofanswers[2]:
        print ("->Correct answer , you won ".capitalize(),a3,"pkr".capitalize())
    else :
        print ("Better luck next time ".capitalize())
else :    
    print ("inod tm se na ho pae ga ".capitalize())



