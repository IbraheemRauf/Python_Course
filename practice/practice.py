print ("Kaun Banega Crorepati".center(100))
name = input("Enter your name : ")
print (f"Welcome {name} , This game is coded by IBRAHEEM who is a very energetic python learner. Below is your FIRST QUESTION:")

questions = [ "What is the real name of POMO? ", "Who loves KFC even after the Palestine conflict?","Who is the PM Pakistan?"]
answers =["x","y", "z"]

a = "5 crore"
b= "10 crore"
c = "1500 crore"

ans1 = input(questions[0])
if ans1.lower() == answers[0] :
    print (f"YOU WON {a} pkr")
    ans2 = input(questions[1])
    if ans2.lower() == answers[1] :
        print (f"YOU WON {b} pkr")
        ans3 = input(questions[2])
        if ans3.lower() == answers[2] :
            print (f"YOU WON {c} pkr")
        else :
            print (f"you lose , you take home only {c}")
    else:
        print (f"you lose , you take home only {b}")
else :
    print (f"you lose , you take home only {a}")