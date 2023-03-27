import sys
import re

def encrypt(input, rounds, roundkeys):
	#TODO: Implement encryption of "input" in "rounds" rounds, using round keys "roundkeys"
        input_left=input[:len(input)//2]
        input_right=input[len(input)//2:]
        
        key_number=0
        #print(input_left)
        #print(input_right)
        
        while rounds>1:
                
                #print("input left is "+ str(input_left))
                #print("input right is "+ str(input_right))
                #print("key is "+str(roundkeys[key_number]))
                #print("rounds is"+str(rounds))

                xor_up = bitwise_and(input_right,roundkeys[key_number])
                xor_up = xor_up.replace("b","0")
                xor_up = fix_length(xor_up)
                #print("xor up is"+str(xor_up))
           
            
                xor_result = xor(xor_up, input_left)
                #print("xor result iss "+xor_result)
                xor_result = xor_result.replace("b","0")
                #print("xor result issss "+xor_result)
                xor_result = fix_length(xor_result)
                #print("xor result is"+str(xor_result))

                input_left  = input_right
                input_right = xor_result
                rounds=rounds-1
                key_number=key_number+1

        #print("no switch")
        #print("input right is"+str(input_right))
        #print("input left is"+str(input_left))
        xor_up = bitwise_and(input_right,roundkeys[key_number])
        xor_up = xor_up.replace("b","0")
        xor_up = fix_length(xor_up)

        #print("xor_up is" + str(xor_up))
        
        xor_result = xor(xor_up, input_left)
        xor_result = xor_result.replace("b","0")
        xor_result = fix_length(xor_result)
        
        #print("last xor_result is"+xor_result)
        result = xor_result+input_right
        return result
    

def decrypt(input, rounds, roundkeys):
	#TODO: Implement decryption of "input" in "rounds" rounds, using round keys "roundkeys"
        
        back_left =input[:len(input)//2]
        back_right=input[len(input)//2:]

        key_number = rounds-1
        
        
        while key_number >= 0:
                
                key = roundkeys[key_number]
                
                #print("key is "+key)
                #print("back_right is "+back_right)
                xor_up = bitwise_and(key,back_right)
                xor_up = xor_up.replace("b","0")
                xor_up = fix_length(xor_up)
                
                #print("xor_up is" + xor_up)
                #print("back left is"+back_left)
                
                ###########||start from here next time
                xor_left= find_xor_left(xor_up,back_left)
                #print("xor_left is" + xor_left)
                #print("----")

                if key_number >0:
                                
                        back_left =  back_right
                        back_right = xor_left
                        key_number=key_number-1
                else:
                        return xor_left+back_right
        #key = roundkeys[key_number-1]
        #xor_up = bitwise_and(key,back_right)
        #xor_up = xor_up.replace("b","0")
        #xor_up = fix_length(xor_up)

        #print(xor_up)

        #xor_left= find_xor_left(xor_up,back_left)
         
        #result = xor_left+back_right 

        #return result

def xor(a,b):
    """
    xor calculate the xor of a and b
    """
    y=int(a,2) ^ int(b,2)
    result=bin(y)
    return result

def bitwise_and(a,b):
    """
    bitwise_and function to calculate the and of a and b
    """
    x_l = a
    x_r = b

    bitwise_and = int(x_l,2) & int(x_r,2)
    bitwise_and_result = bin(bitwise_and)
    return bitwise_and_result
    
    
def fix_length(x):

    """
    helping function to fix bitwise_and function output result.
    """
    
    if(len(x)<4):
        to_be_append=4-len(x)
        for i in range(to_be_append):
                x="0"+x
    if(len(x)>4):
        subtract = len(x)-4
        x=x[subtract:]
            
    return x
def find_xor_left(xor_up, back_left):

    """
    function to help find the one input of xor gate, another input is already known.    
    """
    #print("enter xor up")
    #print("xor up is:"+xor_up)
    #print("back_left is:"+back_left)
    a=''
    b=''
    c=''
    d=''
    #print(xor_up[0])
    #print(back_left[0])
    
    if xor_up[0]=='0' and back_left[0]=='0':
        a='0'
    if xor_up[0]=='0' and back_left[0]=='1':
        a='1'
    if xor_up[0]=='1' and back_left[0]=='1':
        a='0'
    if xor_up[0]=='1' and back_left[0]=='0':
        a='1'

    if xor_up[1]=='0' and back_left[1]=='0':
        b='0'
    if xor_up[1]=='0' and back_left[1]=='1':
        b='1'
    if xor_up[1]=='1' and back_left[1]=='1':
        b='0'
    if xor_up[1]=='1' and back_left[1]=='0':
        b='1'


    if xor_up[2]=='0' and back_left[2]=='0':
        c='0'
    if xor_up[2]=='0' and back_left[2]=='1':
        c='1'
    if xor_up[2]=='1' and back_left[2]=='1':
        c='0'
    if xor_up[2]=='1' and back_left[2]=='0':
        c='1'

    if xor_up[3]=='0' and back_left[3]=='0':
        d='0'
    if xor_up[3]=='0' and back_left[3]=='1':
        d='1'
    if xor_up[3]=='1' and back_left[3]=='1':
        d='0'
    if xor_up[3]=='1' and back_left[3]=='0':
        d='1'
    return a+b+c+d
    
        
opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]
args = [arg for arg in sys.argv[1:] if not arg.startswith("-")]
#print(args)
c = re.compile('^[01]{8}$')
try:
	input=args.pop(0)
except IndexError:
	raise SystemExit("Usage: {sys.argv[0]} [-d] input rounds roundkey1 roundkey2 ...")
if not c.search(input):
	raise SystemExit("input is not a valid bit string")

try:
	rounds=int(args.pop(0))
except IndexError:
	raise SystemExit("Usage: {sys.argv[0]} [-d] input rounds roundkey1 roundkey2 ...")
except ValueError:
	raise SystemExit("rounds is not a valid number")

if(len(args)<rounds):
	raise SystemExit("Usage: {sys.argv[0]} [-d] input rounds roundkey1 roundkey2 ...")

roundkeys=args
c = re.compile('^[01]{4}$')
if not all(c.search(elem) for elem in roundkeys):
	raise SystemExit("round key is not a valid bit string")

if "-d" in opts:
	result = decrypt(input,rounds,roundkeys)
else:
	result = encrypt(input,rounds,roundkeys)

print (result)
