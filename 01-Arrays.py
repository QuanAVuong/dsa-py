lItems = ["string", 3984, [True, False], {"float": 1.4, "fraction": 1/5}]

print("3 =>", lItems[2])

lItems[0] = "Hello World"
print("6 =>", lItems[0])

for item in lItems:
  print("9 =>", item)


for i in range(len(lItems)):
  print("13 =>", lItems[i])

# 4.6.1. Common Sequence Operations
# https://docs.python.org/3/library/stdtypes.html
print("16 =>", lItems[0:2])
print("17 =>", lItems[:2])
print("18 =>", lItems[:])
print("19 =>", lItems[:-1])
print("20 =>", lItems[-2:])
print("21 =>", lItems[::2])
print("21 =>", lItems[::-1])
