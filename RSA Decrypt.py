import time
from tqdm.auto import tqdm

d=int(input('Enter First Part Of Public Key : '))
n=int(input('Enter Second Part Of Public Key : '))
letters=' ABCEDFGHIJKLMNOPQRSTUVWXYZ'

cipher=input("Enter the Cipher-Text to decrypt : ").split(', ')
text=''

bar=tqdm(total=len(cipher),position=0,leave=False)
for c in cipher:
	bar.set_description('Decrypting {}'.format(c))
	bar.update()
	time.sleep(0.1)

	m=(int(c)**d)%n
	p=letters[m]
	text+=p

print('\nDecrypted Message : ',text)
