fruits = {}

fruits["apple"] = 30
fruits["banana"] = 10
fruits["mango"] = 100

print(fruits)
print(fruits["mango"])

fruits["mango"] = 120
print(fruits["mango"])

fruits[33] = "Shaq"
print(fruits)


for key, value in fruits.items():
	print(key, " <- KEY", "Value -> ", value)

print(fruits)
del fruits["mango"]
print(fruits)