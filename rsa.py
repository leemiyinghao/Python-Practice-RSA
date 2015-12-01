import random, math

class isPrime:
    List_Prime = [2]
    def __init__(self, Number):
        self.Find_Prime(Number)
        return self.Check_Prime(Number)
        
    def Find_Prime(self, Number):
        limit = int(math.sqrt(Number)//1)
        for number in range(2, limit):
            for checkprime in range(0,len(List_Prime)):
                if number%List_Prime[checkprime] == 0:
                    break
            List_Prime.append(number)
            continue
        
    def Check_Prime(self, Number):
        for number in range(0,len(List_Prime)):
            if Number%List_Prime[number] == 0:
                return False
                break
        return True
        
def genPrime(start, end):
   while True:
      num = random.randint(start, end)
      if isPrime(num):
         return num
class RSA:
   def __init__(self):
      self.genKey()
   def genKey(self):
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
      #save public and private key
      self.publicKey = {'N':n,'e':e}
      self.privateKey = {'N':n, 'd':d}
   def encode(self, plainNumber):
      return plainNumber**self.publicKey['e'] % self.publicKey['N']
   def decode(self, cipherNumber):
      return cipherNumber**self.privateKey['d'] % self.publicKey['N']

#let's encrypt
rsa = RSA() #init a RSA object
plainNumber = 42 #the answer to the meaning of life, the universe, and everything
cipherNumber = rsa.encode(plainNumber) #calling RSA object to encode
replainNumber = rsa.decode(cipherNumber) #calling RSA object to decode
print("plainNumber:", plainNumber)
print("cipherNumber:", cipherNumber)
print("replainNumber:",int(replainNumber))
