#3
def gcd(a,b):
  while b:
    a,b=b,a%b
  return a

print(gcd(10,20))
print(gcd(14,91))
print(gcd(91,14))
#4
def coprime(a,b):
  if gcd(a,b)==1:
    return True
  else:
    return False

print(coprime(10,20))
print(coprime(14,91))
print(coprime(91,14))

