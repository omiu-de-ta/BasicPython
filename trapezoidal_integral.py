from math import sin,pi,exp,sqrt

def cacl(f,a=0,b=1,N=100):

    h=(b-a)/N
    daikei=0
    s=0

    for k in range(1,N+1):
        daikei=0.5*h*(f(a+(k-1)*h)+f(a+k*h))
        s+=daikei
    return s

def f(x):
    return sin(x)

def g(x):
    return 4/ (1+x**2)

def h(x):
    return sqrt(pi)* exp(-x**2)

print(cacl(f,0,pi/2,50))

print(cacl(g,0,1,100))

print(cacl(h,-100,100,1000))



# print(sin(0))
# >>> 0
# -----------
