base = 2
digits = "0123456789ABCDEF"

for i in digits[:base]:
     for j in digits[:base]:
          x = str(i) + str(j)
          print(x, end=" ")
     print()
     
