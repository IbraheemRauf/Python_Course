
# 1)List bracket type: [ ] 
# 2)List are mutable: elements can be added, removed and be replaced 
# 3)Both int and string can be in a same list 
# 4)Slicing can be done in string

######program to input movie names and store them in a list
# list = []
# mov1 = list.append(input("movie 1"))
# mov2 = list.append(input("movie 2"))
# mov3 = list.append(input("movie 3"))
# print (list)

######marks concept  INEDX concept
# marks = [ "oaksitan ", 9 ,5,7, True , "ibraheem","islam","kabootar"]
# print(len(marks))  #4
# print(marks[1:3])
# print(marks[0:4])
# print(marks[0:3 ])
# print(marks[-4 ])  #print (marks[len(marks)-4])      4-4   0

# if "ibraheem" in marks :      #to find somwething in list
#     print ("YES")
# else :
#     print ("NO")

# if "heem" in "ibraheem":
#         print ("YES")
# else :
#     print ("NO")

#######USE OF JUMP INDEX 
# veggies = ["apple","banana","cucumber","dragon fruit","elvish","fuji apple"]
# print ( len(veggies ) )
# print ( veggies[:])
# print ( veggies [0:7:2])    #agr hum 1 ka jump den ge to koi farq nhi pare ga , agr 2 ka jump den ge to 1 value chor kr agli value likhen ge b

########LIST COMPRESSEION
# List = [Expression(item) for item in iterable if Condition]

# Expression: It is the item which is being iterated.

# Iterable: It can be list, tuples, dictionaries, sets, and even in arrays and strings.

# Condition: Condition checks if the item should be added to the new list or not.
# list = ["paksitan","indai", "france","japan","germany","england","france","afganistan","america","iarn","wazeristan","chicago"]
# listwithletter_i = [item for item in list if "i" in item]
# print (listwithletter_i)


#######new qqqqq
listofnumbers =[i for i in range(100) if i%2==0]
print(listofnumbers)