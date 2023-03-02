str1="Hi! I am {} and I am from {}"
name="Harshita"
place="West Bengal"
print(str1.format(name,place))

str1="Hi! I am {0} and I am from {1}"
name="Harshita"
place="West Bengal"
print(str1.format(name,place))

str1="Hi! I am {} and I am from {}"
name="Harshita"
place="West Bengal"
print(str1.format(name,place))
print(f"Hi! I am {name} and I am from {place}")

price=10000.9999
print(f"The price is {price:.2f} ")
print(f"My name is {{name}} and I am from {{place}}")
print(f"{100*100}")