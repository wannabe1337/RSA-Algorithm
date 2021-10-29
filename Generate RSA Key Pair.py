import random,time
from tqdm.auto import tqdm

def GeneratePrime():
	n=random.randint(20,70)
	#print(n)
	
	#Generating nth row of pascal's triangle
	line = [1]
	for j in range(n):             
		line.append(int(line[j]*(n-j)//(j+1)))             
	#print(line)
	
	# AKS Primality test 
	l=int(n/2)+1
	l=n-l+1
	for k in line[1:-l]:
		if(k%n!=0):
			return 0
	return n


##########################################################################################
# Generating 2 primes using 'GeneratePrime()' function

bar=tqdm(total=2,position=0,leave=False)

primes=[]
for i in range(2):
	bar.set_description('Generating Two Large Primes...')
	
	val=0
	while(val==0):
		val=GeneratePrime()
	primes.append(val)
	
	bar.update()
	time.sleep(0.05)
print('\nTwo large primes are : ',primes)


##########################################################################################
# RSA Algorithms
p=primes[0]
q=primes[1]

n=p*q
print('N = ',n)
# no. of coprime with n under n (i.e. Euler's Totient Function [Phi])
Phi=(p-1)*(q-1)	# A Co-prime number is a set of numbers or integers which have only 1 as their common factor
print('Phi = ',Phi)


##########################################################################################
# choose encryption key e such that 1<e<phi and co-prime with n and phi

def Choose_e():
	
	#Program to verify co-prime
	def gcd(p,q):
	# find the gcd of two positive integers. | Euclid's Algorithm
	    while(q!=0):
	        p,q = q,p%q
	    return p
	def is_coprime(x,y):
   		return gcd(x,y)==1

	e=random.randint(1,Phi)
	if(is_coprime(e,n) and is_coprime(e,Phi)):
		return e
	else:
		return 0

print('\nFinding enKey using Euclid\'s Algo and is_coprime()...')
e=0
while(e==0):
	e=Choose_e()

enKey=e
print('enKey = ',e)

##########################################################################################
# choose decryption key d such that d*e(mod phi)=1

	#Extended Euclidean Algorithm to find multiplicative inverse modulo
def eea(a,b):
    if(a%b==0):
        return(b,0,1)
    else:
        gcd,s,t = eea(b,a%b)
        s = s-((a//b) * t)
        return(gcd,t,s)


	#Multiplicative Inverse
def mult_inv(e,Phi):
    gcd,d,_=eea(e,Phi)
    if(gcd!=1):
        return None
    else:
        if(d<0):
            d=d%Phi
        return d

print('\nFinding deKey using EEA and mult_inv()...')
deKey=mult_inv(e,Phi)

print('deKey = ',deKey)

#########################################################################################
print()
print(f'Private Key = ({enKey},{n})')
print(f'Public Key = ({deKey},{n})')
