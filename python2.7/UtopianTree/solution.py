def GetTreeHeight(a):
    result = 1
    if (a == 0):
      return result

    for x in range(1, a + 1):
        if (x % 2 == 0):
            result = result + 1
	else:
	    result = result * 2
    return result

numberOfTests = input()
tests = []
for x in range(0, numberOfTests):
    tests.append(input())

for y in range(0, len(tests)):
    print GetTreeHeight(tests[y])
