s = c = 0
for i in range (1, 501,2):
    if i % 3 == 0:
        print(i)
        s += i
        c += 1
print(c,s)
