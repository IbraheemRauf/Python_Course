#ISDISJOINT       agr dono set mese koi aik element bhi same nhi hoga to true return hoga
                   #agr kuch same hoga to false return hoaga
set1 = {"pak","china","india","eng","uk"}
set2 = {"ukraine","russia","malysia","france","uk"}
print( set1.isdisjoint(set2))


#ISSUPERSET       agr set3 ke elements set4 me honge to set3 superset consider hoga 
                #note: set4 me agr set3 ke ilawa bhi elements honge to false notsuperset

set3 = {1,2,3,4,5,6,7}
set4 = {3,4,5}
print ( set3.issuperset(set4))   


print ( set4.issubset(set3) )    #mtlb set 4 beta ha set 3 ka

#ADD

pk1={1,2,3,4}
pk1.add(5)
print(pk1)

#remove
cities = {"tokyo","madrid","berlin","egypt"}
cities.remove("tokyo")
print(cities) 
#agr hum tokyo2 to nikalen ge to REMOVE error through kre ga 
#agr hum chahty hn ke error ho or wo show na ho to hum DISCARD use krty hn

#pop 
#random element ko remove kr deta ha lkn bad me show bhi krta ha 
dj = {2,4,6,8,10}
pkl =dj.pop()
print (dj)
# print(pkl)   #show kre ga konsi value pop ha


#DEL
# qw= {3,22,2,2,2244}
# del qw
# print (qw) #print nhi hoga error aye ga kuke humne qw delete ikrdia ha 

#clear
otp = {2,3,4,5,6,7}
tea = otp.clear()
print (otp)