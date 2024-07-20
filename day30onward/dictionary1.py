# 1. Dictionary are using key value pairs to store values
# 2. They are made by using s1={ "key": "value", "key": "value" } syntax
# 3. you can get all keys of dictionary by s1. keys[]
# 4. you can get all values of dictionary by using s1.values[]
# 5. you can get all pairs of dictionary by s1.items[]
# 6. you can get the value of an item by using s1['key'] and 
# it will return the value. s1.get( "key") will also return the value but it wont throw an error in case there is no value/key available in the dictionary




# dic = {
#     "name":"ibraheem",
#     "class":"ics 1",
#     "country":"pakistan",
#     "city":"lahore"
# }
# print (dic["class"])

dic1 ={
    1:"zakir",
    2:"aslam",
    3:"binod",
    4:"rauf",
    5:"rauf5",
    6:"rauf6"
}
# print (dic1[2])           #thros error if the values doesnot exist       #same use 
# print (dic1.get(7))       #doesnot thros error, thros NONE if error exsit#same use

# print (dic1[4])
# print(len(dic1))
# print (dic1.values())
# print (dic1.keys()) 
for key in dic1.keys():
    print("The value corresponding to {key}is {dic1[key]}")

