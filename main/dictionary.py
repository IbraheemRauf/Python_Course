info = {
    "NAME ": "IBRAHEEM",
    "AGE": 18,
    "SCHOOL": "LIAQUAT FOUNADTION",
    "COLLEGE" : "SUPERIOR GROUP OF COLLEGES ",
    "Subjects": ["English","Math","Physics"], #we can also give LIST in dictionary
    "Topics": ("Adjective","Trignometry","Gravitational Force"), #we can also give TUPLE in dictionary
    67 : "MY NAME IS LAKHAN",
    54 : 33,

}
print (info)
print(type(info))
print (info["Subjects"])  #we can also print separate selective values 
print (info["NAME "])
print (info["COLLEGE"])
print (info[54])