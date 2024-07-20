tuple1 = (2,3,4,5,66,65,3,1,2,3,4,5,4,3,1,9)
#Count method
re = tuple1.count(4)
print(re)

#Index method
#The Index() method returns the first occurrence of the given element from the tuple
# Syntax:
# tuple.index(element, start, end) #agr start end specify krke index find krna ho
tuple = (0, 1, 2, 3, 2, 3, 1, 3, 2)
res = tuple.index(3)
print('First occurrence of 3 is', res)

tota = tuple.index(3,2,5) #ye baki sab accurence igonore krke bas start or end ki value me chez find kre ga or pori tuple me uska index dhond kr btae ga 
print (tota)
