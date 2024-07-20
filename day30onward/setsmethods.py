city1 = {"tokyo","berlin", "madrid","manchester"}
city2 = {"uk","finland", "poland","manchester"}

print (city1.intersection(city2))  #ye bas usi time intersection print krta ha , no future implimentation
city1.intersection_update(city2)    #ye update kredta ha set hamesha ke , future tak update rhta ha
print (city1)


pak1 = {1,2,3,4,5}
pak2 = {4,5,6,7,8}

print(pak1.union(pak2))      #similar opposite
pak1.update(pak2)
print(pak1)


 
gb1 = {"a","b","c","d","e","f","g","h"}
gb2 = {"f","g","h","i","j","k","l","m"}
print (gb1.symmetric_difference(gb2))     #jo chezen common nhi hoti wo ati han , common chezen cacel hoajati
