name = "Jahel"
lastName = "Chacon"
edad = 25
print(name, lastName)

fullName = name + " " + lastName
print("Nombre completo -> ", fullName)

quote = "La vida es muy corta para no disfrutarla"
print('"',quote,'"')

# Format 
template = "Hola, mi nombre es " + name + " y mi apellido es " + lastName
print(template)

templateFormat = "Hola, mi nombre es {} y mi apellido es {}".format(name,lastName)
print(templateFormat)

templateF = f"Hola, mi nombre es {name} {lastName} y mi edad es {edad}"
print(templateF)