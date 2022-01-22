name = ""

print(name.capitalize())
name1 = "pakanei"
name2 = "tea shop"
name3 = "petanu"
print(name1.capitalize() + name2.capitalize()
      + name3.capitalize())


firstString = "der FluSS"
secondString = "der Fluss"

# ß is equivalent to ss
if firstString.casefold() == secondString.casefold():
    print('The strings same.')
else:
    print('The strings are not same.')


# Will tell if it is ending with the given string or not

message = 'Ayayyo vadamma sukibhava'

# check if the message ends with sukibhava
print(message.endswith('sukibhava'))



