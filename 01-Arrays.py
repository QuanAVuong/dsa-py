lItems = ["string", 3984, [True, False], {"float": 1.4, "fraction": 1/5}]

print("3 =>", lItems[2])

lItems[0] = "Hello World"
print("6 =>", lItems[0])

for item in lItems:
  print("9 =>", item)


for i in range(len(lItems)):
  print("13:", lItems[i])