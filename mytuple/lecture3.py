countries = ("pakistan","russia ","ukraine","united states","america")
print (type(countries))
warden = list (countries)
warden.append("afganistan")  #add item
warden.pop(0)   #remove item
warden[2] = "finland"
countries = tuple(warden)
print (countries )

#another method of merging tuple
pakistan = ("lahore ","karachi","isalambad")
india = ("delhi", "mumbai","up")
asia = pakistan + india
print (asia)
