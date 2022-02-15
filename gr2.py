import matplotlib.pyplot as plt
import random
# x axis values

# corresponding y axis values
y = randomlist = []
for i in range(0,250):
    n = random.randint(1,100)
    randomlist.append(n)
    y = randomlist = []

x = (list(range(1, 251)))

for i in range(0,250):
    n = random.randint(1,100)
    randomlist.append(n)


plt.plot(x, y)

plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('1-100 random values')
plt.show()
