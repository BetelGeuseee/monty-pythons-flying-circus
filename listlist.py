
value=[1,2,3,4,5]

value2=value
print(value)
print(value2)

value2.append(7)
print(value2)
print(value)

value3=value2.copy()
value3.append(8)
print(value3)
print(value2)