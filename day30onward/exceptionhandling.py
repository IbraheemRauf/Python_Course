# a = input("ENTER A NUMBER : ")
# print (f"Multication table for {a} is :")
# try:               #agr error aye ga to direct except pr chla jae ga    
#     for i in range(1,11):
#         print (f"{int(a)} x {i} = {int(a)*i}")
# except :
#     print ("Invalid Input")

try:
    num = int(input("enter a integer: "))
except ValueError:
    print("number  is not an integer,")
except IndexError:
    print("number  is not an integer,")
