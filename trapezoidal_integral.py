from math import sin,pi
a=0
b=pi/2
N=100
h=(b-a)/N
daikei=0
s=0
for k in range(1,N+1):
    daikei=0.5*h*(sin(a+(k-1)*h)+sin(a+k*h))
    s+=daikei
print(s)



# print(sin(0))
# >>> 0
# -----------
