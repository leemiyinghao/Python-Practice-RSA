import random, math
def isPrime(i):
    limit = int(math.sqrt(i)//1)
    if i == 2 or i ==3:
        return True
    for number in range(2,limit+1):
        if i%number == 0:
            return False
            break
        if number == limit:
            return True
            break

def genPrime(start, end):
   while True:
      num = random.randint(start, end)
      if isPrime(num):
         return num

#p & q are two different prime
q = p = genPrime(50, 100)
while p == q:
   q = genPrime(50, 100)
n = p*q
r = (p-1)*(q-1)

#find an e is a coprime to r
e = 0
for num in range(2,r):
   if isPrime(num) and r%num != 0:
      e = num
      break

#find a modular multiplicative inverse of e
d = 0
for num in range(2,r):
   if (e*num)%r == 1:
      d = num

#let's encrypt
plainNumber = 42 #the answer to the meaning of life, the universe, and everything
cipherNumber = plainNumber**e%n
print("p=%d q=%d N=%d r=%d e=%d d=%d"%(p,q,n,r,e,d))
print("plainNumber:", plainNumber)
print("cipherNumber:", cipherNumber)
replainNumber = cipherNumber**d%n
print("replainNumber:",int(replainNumber))
