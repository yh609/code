"""
Template file for ECMM462 coursework
Academic Year: 2022/23
Version: 2
Author: Diego Marmsoler
"""
import sys
import re
import random

#Alice
rightsalice = {}
alicemaxprio = ''
alicemaxcat = []
alicecurrentprio = ''
alicecurrentcat = []
document1=['l',  ['A','B']]
document2=['h', ['C']]
document3=['h', ['B']]
file1 = open('alice.txt', 'r')
lines = file1.readlines()
if (len(lines)!=3):
	raise SystemExit("Wrong file format")

c = re.compile('^([wra]?),([wra]?),([wra]?)$')
result=c.search(lines[0])
if (not result):
	raise SystemExit("Wrong file format")
rightsalice[1]=result.group(1)
rightsalice[2]=result.group(2)
rightsalice[3]=result.group(3)

prio = lines[1].strip().split(":")
if (len(prio)!=2):
	raise SystemExit("Wrong file format")

if (prio[0]=='h' or prio[0]=='l'):
	alicemaxprio=prio[0]
else:
	raise SystemExit("Wrong file format")

cat = prio[1].split(",")
for c in cat:
	if (c == 'A' or c == 'B' or c =='C'):
		alicemaxcat.append(c)

prio = lines[2].strip().split(":")
if (len(prio)!=2):
	raise SystemExit("Wrong file format")

if (prio[0]=='h' or prio[0]=='l'):
	alicecurrentprio=prio[0]
else:
	raise SystemExit("Wrong file format")

cat = prio[1].split(",")
for c in cat:
	if (c == 'A' or c == 'B' or c =='C'):
		alicecurrentcat.append(c)

#Bob
rightsbob = {}
bobmaxprio = ''
bobmaxcat = []
bobcurrentprio = ''
bobcurrentcat = []

file1 = open('bob.txt', 'r')
lines = file1.readlines()
if (len(lines)!=3):
	raise SystemExit("Wrong file format")

c = re.compile('^([wra]?),([wra]?),([wra]?)$')
result=c.search(lines[0])
if (not result):
	raise SystemExit("Wrong file format")
rightsbob[1]=result.group(1)
rightsbob[2]=result.group(2)
rightsbob[3]=result.group(3)

prio = lines[1].strip().split(":")
if (len(prio)!=2):
	raise SystemExit("Wrong file format")

if (prio[0]=='h' or prio[0]=='l'):
	bobmaxprio=prio[0]
else:
	raise SystemExit("Wrong file format")

cat = prio[1].split(",")
for c in cat:
	if (c == 'A' or c == 'B' or c =='C'):
		bobmaxcat.append(c)

prio = lines[2].strip().split(":")
if (len(prio)!=2):
	raise SystemExit("Wrong file format")

if (prio[0]=='h' or prio[0]=='l'):
	bobcurrentprio=prio[0]
else:
	raise SystemExit("Wrong file format")

cat = prio[1].split(",")
for c in cat:
	if (c == 'A' or c == 'B' or c =='C'):
		bobcurrentcat.append(c)

#Charlie
rightscharlie = {}
charliemaxprio = ''
charliemaxcat = []
charliecurrentprio = ''
charliecurrentcat = []

file1 = open('charlie.txt', 'r')
lines = file1.readlines()
if (len(lines)!=3):
	raise SystemExit("Wrong file format")

c = re.compile('^([wra]?),([wra]?),([wra]?)$')
result=c.search(lines[0])
if (not result):
	raise SystemExit("Wrong file format")
rightscharlie[1]=result.group(1)
rightscharlie[2]=result.group(2)
rightscharlie[3]=result.group(3)

prio = lines[1].strip().split(":")
if (len(prio)!=2):
	raise SystemExit("Wrong file format")

if (prio[0]=='h' or prio[0]=='l'):
	charliemaxprio=prio[0]
else:
	raise SystemExit("Wrong file format")

cat = prio[1].split(",")
for c in cat:
	if (c == 'A' or c == 'B' or c =='C'):
		charliemaxcat.append(c)

prio = lines[2].strip().split(":")
if (len(prio)!=2):
	raise SystemExit("Wrong file format")

if (prio[0]=='h' or prio[0]=='l'):
	charliecurrentprio=prio[0]
else:
	raise SystemExit("Wrong file format")

cat = prio[1].split(",")
for c in cat:
	if (c == 'A' or c == 'B' or c =='C'):
		charliecurrentcat.append(c)

#MAIN
def ssc(alice, bob, charlie):
	# print("enter ssc")
	number=0
	alice_object=list(alice)[0]
	# print("alice object is "+alice_object)
	alice_document=''
	if alice_object=="1":
		alice_document=document1
	if alice_object=="2":
		alice_document=document2
	if alice_object=="3":
		alice_document=document3

	# print("alice document is ")
	# print(alice_document)
	
	alice_right=list(alice.values())
	# print("alice right is")
	# print(alice_right)
	if alice_right[0]=='a':
		number=number+1
	decide1 = 0

	if alice_right[0]=='r' or alice_right[0]=='w':
		# print("alice right is r or w")
		#看一下fs(s)是否 dom fo(o):
		fs=[alicemaxprio,alicemaxcat]
		# print(fs)
	
		if (fs[0]=='h' and alice_document[0]=='h') or (fs[0]=='h' and alice_document[0]=='l'):
			decide1=0.5
		
		contain=True
		for i in alice_document[1]:
			if i not in fs[1]:
				contain=False

	if decide1==0.5 and contain==True:
		# print("alice number +1")
		number=number+1

	# print(" ")
	bob_object = list(bob)[0]
	bob_right = list(bob.values())
	if bob_right[0]=='a':
		number=number+1
	
	decide2=0
	bob_document=''
	if bob_object=="1":
		bob_document=document1
	if bob_object=="2":
		bob_document=document2
	if bob_object=="3":
		bob_document=document3
	if bob_right[0]=='r' or bob_right[0]=='w':
		# print("Bob right for r or w")
		fsb=[bobmaxprio,bobmaxcat]
		# print(fsb)
		# print(bob_do/cument)
		if (fsb[0]=='h' and bob_document[0]=='h') or (fsb[0]=='h' and bob_document[0]=='l'):
			decide2=0.5
		
		contain2=True
		for i in bob_document[1]:
			if i not in fsb[1]:
				contain2=False
	if decide2==0.5 and contain2==True:
		# print("Bob number +1")
		number=number+1


	charlie_object = list(charlie)[0]
	charlie_right  = list(charlie.values())

	charlie_document=''
	if charlie_object=="1":
		charlie_document=document1
	if charlie_object=="2":
		charlie_document=document2
	if charlie_object=="3":
		charlie_document=document3
	# print(" ")
	# print("charline document is")
	# print(charlie_document)
	
	# print("charline right is")
	# print(charlie_right)
	decide3=0
	if charlie_right[0]=='a':
		number=number+1
	if charlie_right[0]=='r' or charlie_right[0]=='w':
		# print("charlie right for r or w")
		fsc=[charliemaxprio,charliemaxcat]	
		if (fsc[0]=='h' and charlie_document[0]=='h') or (fsc[0]=='h' and charlie_document[0]=='l'):
			decide3=0.5
		
		contain3=True
		for i in charlie_document[1]:
			if i not in fsc[1]:
				contain3=False

	if decide3==0.5 and contain3==True:
		# print("charline number +1")
		number=number+1

	# print(" ")
	# print("number is"+str(number))
	if number==3:
		return True
	else:
		return False
	#TODO: Implement check for simple security condition
	#"alice", "bob", and "charlie" contain the currently executed rights
	#In addition, the following global variables can be used (similar for bob and charlie)
	#"rightsalice" contains the access control matrix for Alice
	#"alicemaxprio" contains the maximum security level for Alice
	#"alicemaxcat" contains the maximum security categories for Alice
	#"alicecurrentprio" contains the current security level for Alice
	#"alicecurrentcat" contains the current security categories for Alice	


def star(alice, bob, charlie):
	#TODO: Implement check for star property
	#"alice", "bob", and "charlie" contain the currently executed rights；
	#In addition, the following global variables can be used (similar for bob and charlie)
	#"rightsalice" contains the access control matrix for Alice
	#"alicemaxprio" contains the maximum security level for Alice
	#"alicemaxcat" contains the maximum security categories for Alice
	#"alicecurrentprio" contains the current security level for Alice
	#"alicecurrentcat" contains the current security categories for Alice	
	return False

def ds(alice, bob, charlie):
	#TODO: Implement check for discretionary security condition
	#"alice", "bob", and "charlie" contain the currently executed rights
	#In addition, the following global variables can be used (similar for bob and charlie)
	#"rightsalice" contains the access control matrix for Alice
	#"alicemaxprio" contains the maximum security level for Alice
	#"alicemaxcat" contains the maximum security categories for Alice
	#"alicecurrentprio" contains the current security level for Alice
	#"alicecurrentcat" contains the current security categories for Alice	
	return False

alice = {}
bob = {}
charlie = {}
c = re.compile('^([ABC]):([123]):([rwa])$')
args=sys.argv[1:]
# print("args is")
# print(args)
# print("length of args is")
# print(len(args))
while (len(args)>0):
	input=args.pop(0)
	# print("single args is ",end=' ')
	# print(input)
	# print("----")
	result=c.search(input)
	# print("search result is :", end=' ')
	# print(result)
	# print("result group 1 is:", end=' ')
	# print(result.group(1))
	# print()
	# print("result group 2 is:", end=' ')
	# print(result.group(2))
	# print()
	# print("result group 3 is:", end=' ')
	# print(result.group(3))
	# print()
	if (not result):
		raise SystemExit("Usage: blpcheck.py [ABC]:[123]:[rwa] ...")
	if (result.group(1)=='A'):
		if result.group(2) in alice:
			raise SystemExit("duplicate entry")
		alice[result.group(2)]=result.group(3) # 这里设置alice{1:a}
	if (result.group(1)=='B'):
		if result.group(2) in bob:
			raise SystemExit("duplicate entry")
		bob[result.group(2)]=result.group(3)
	if (result.group(1)=='C'):
		if result.group(2) in charlie:
			raise SystemExit("duplicate entry")
		charlie[result.group(2)]=result.group(3)

	# print(alice)
	# print(bob)
	# print(charlie)

print ("SSC: ", "Yes" if ssc(alice, bob, charlie) else "No")
print ("Star: ", "Yes" if star(alice, bob, charlie) else "No")
print ("DS: ", "Yes" if ds(alice, bob, charlie) else "No")
