

x, y, z, n = [int(input()) for _ in range(4)]

myList = [[x, y, z] for x in range(x) for y in range(y)
          for z in range(z) if x + y + z != n]

print(myList)
