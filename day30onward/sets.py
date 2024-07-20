#SETS
#1) sets are unordered when print
#2) duplicate items are shown at once only
#3) to show empty set type use set()

s = {2,3,3,32,4,False,4,"charlie",42}
print (s)    #sets are unordered when print

info = { }            #wrong approch
print(type(info))     #dict

info2 = set()       #right approch
print(type(info2))    #set

#to access  values in set
for values in s:
    print (values )
    