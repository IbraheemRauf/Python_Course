#Strings are immuteable      POINT TO BE NOTED 
 #asal value change nhi hogi jo a ki ha bs wo 
 #  value change hogi jis pr operation apply hoga wo cahnge hogi
a = "Harry????? ????? ?harry??? ??harry? ??"
print(len(a))
print( a )
#LOWER
print( a.lower() )
#UPPER
print( a.upper() ) 
#RSTRIP
print( a.rstrip("?") )   #sirf end wali chez trim krts| shrow wali nhi
#REPLACE
print( a.replace("Harry","john ibraheem"))
#SPLIT
print( a.split(" ")) #is function se list bn jati h jidhr jidhr space ho.
#CAPITALIZE
blogHeading= "introduction to js"
print( blogHeading.capitalize()) #only 1st character upper case ,,,all the other lower casew
#CENTRE
str1= "welcome to the console"
print( len(str1))
print( len( str1.center(30))) 
#COUNT
print( a.count("harry"))  #ye count krta ha ke specific word kitni dfa ha"also case sensitive bhi ha 
#ENDSWITH + starts with
print( a.endswith("?")) #ye btata ha ke particular chez usi pr end horhi ha ke nnhi tru falese
#FIND
pkr= "he is apple a honest. he is very a wealthy" 
print( pkr.find("a") )  #ye specific word ki location ka index find krta ha agr hum koi aise value den jo exist na krti ho te ye -1 retuen krta ha 
#INDEX

#agr hum chahty hm ke -1 ki jagh ERROR return ho to hum index ka use krty . APPROXIMATELY similar use 
#ISALNAM
pop = "islovepakitanbczof14AUGUST"
print( pop.isalnum())  # isalnum include a-z,A-Z,0-9 true ...all ther(punctuatuion ,cahracteerr) things return false
#ISALPHA
pip= "islovepakitanbczofAUGYUST"
print( pip.isalpha())  #include a-z,A-Z true  ,.all ther(number,punctuatuion ,cahracteerr) things return false
#ISLOWER
print( pip.islower())   #agr sab kuch lower case hoga to TRUE return kre ga 
#ISPRINTABLE
newstring = "here is written my name \n name "
print( newstring.isprintable()) #is code me escape sequence ha \n ha jo not printable  ha is wjh se FALSE answer hoga
#ISTITTLE
str5="World Health Organization"  #agr title ka 1st word lower case hoga to ye falese return kare ga , agr upper case huwa to true return kre ga 
print( str5.istitle())
#TITLE
str7="world health organization"   
print( str7.title())        #firts words ko capital krdeta
#ISSAPCE
str6=" "         #agr sirf space hogi to true retur kre ga otherwise false
print(str6.isspace())
#SWAPCASE
str8= "World Health Organization"
print(str8.swapcase()) #lower ko capital or capital ko lower krta ha 

