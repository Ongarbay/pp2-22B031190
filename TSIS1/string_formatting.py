#ex47
price = 49
txt = "The price is {} dollars"
print(txt.format(price))
#ex48
txt = "The price is {:.2f} dollars"
#ex49
quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))
#ex50
quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))
#ex51
age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
#ex52
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))