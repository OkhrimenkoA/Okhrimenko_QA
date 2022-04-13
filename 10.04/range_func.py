# range(start, stop, step)
# range(start, stop)      step = 1
# range(start)            start = 0, step = 1

# range(1, 10, 2)          1, 3, 5, 7, 9

for i in range(25):
    print(i, end=' ')
print()

j = 0
for _ in range(10):
    print(j**2, end=' ')
    j += 1
print()