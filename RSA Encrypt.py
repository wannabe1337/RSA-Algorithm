import time
from tqdm.auto import tqdm

e=int(input('Enter First Part Of Private Key : '))
n=int(input('Enter Second Part Of Private Key : '))
letters=' ABCEDFGHIJKLMNOPQRSTUVWXYZ'

text=input("Enter the text to encrypt : ")
text=text.upper()
ciphertext=[]

bar=tqdm(total=len(text),position=0,leave=False)
for p in text:
	
	bar.set_description('Encrypting {}'.format(p))
	bar.update()
	time.sleep(0.1)

	m= letters.find(p)
	c=(m**e)%n
	ciphertext.append(c)

print('\nEncrypted Message : ',ciphertext)
