(firstName,
 lastName,
 fullName,
 space,
 hello) = ("Richard",
           "Scarfino",
           "Richard, Scarfino",
           " ",
           "Hello, World!")

print(type(hello)), print(space + hello)

statement = fullName + space + "displayed: " + hello + space + "to the console"

print(statement)