import random, math

List_Prime = [2]

def isPrime(i):
    if i == 2 :   return True

    limit = int(math.sqrt(i)//1)

    if limit < List_Prime[len(List_Prime)-1]:
        for checkprime in range(0,len(List_Prime)):
            if List_Prime[checkprime] > limit: break
            if number%List_Prime[checkprime] == 0:
                return False
                break
            return True
            break
                                                            
    
    for number in range(List_Prime[len(List_Prime)-1], limit):
        for checkprime in range(0,len(List_Prime)):
            if number%List_Prime[checkprime] == 0:
                break
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
