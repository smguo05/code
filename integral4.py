import random
from math import sin
from math import pi


N = 10**5
a_max = -N
dx = pi/(2*N)
a = []

for i in range (0, N+1):
    a.append(2*sin(i*dx)+5)
    if a_max < a[i]:
        a_max = a[i]
  
def get_area(n):
    inside = 0
    for i in range(0, n):
        x = random.random()*(pi/2)+(pi/2)
        y = random.random()*7
        if y <= (2*sin(x)+5): 
            inside += 1
    integral = (inside/N)*(pi/2)*(a_max)
    return integral

print(get_area(N))
print(a_max)


