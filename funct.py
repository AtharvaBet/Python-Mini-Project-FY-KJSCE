from table import b64table
def DecimalToBinary(n):
    a=""
    for i in range(8):
        a= a+ str(n%2)
        n=n//2
    a=a[::-1]    
    return a

def BinarytoDecimal(n):
    n=n[::-1]
    a=0
    for i in range(8):
        if (n[i]=='1'):
            a+=pow(2,i)
    return a

def get_key(n):
    for key, value in b64table.items():
         if n == value:
             return key
 
def Base64(s):
    binstr=""   
    for i in range(len(s)):
        binstr= binstr + DecimalToBinary(ord(s[i]))
    
    bin_6bit=[binstr[x:x+6] for x in range(0,len(binstr),6)]
    padding = int((6-len(bin_6bit[-1])%6)/2)
    if padding==3:
        padding =0
    while len(bin_6bit[-1])!=6:
        bin_6bit[-1]=bin_6bit[-1]+'0'
    ans=""
    for i in range(len(bin_6bit)):
        ans=ans+b64table[bin_6bit[i]]

    while padding>0:
        ans=ans+'='
        padding-=1
    return ans

def ASCII(s):
    binstr=""
    padding = 0
    for i in range(len(s)):
        if s[i] == '=':
            padding+=1
    s= s[:len(s)-padding]

    for i in range(len(s)):
        binstr= binstr + str(get_key(s[i]))
    
    bin_6bit=[binstr[x:x+8] for x in range(0,len(binstr),8)]
    ans=''
    if padding>0:
        bin_6bit.pop()
    
    for i in range(len(bin_6bit)):
        bin_6bit[i] = chr(BinarytoDecimal(bin_6bit[i]))
        ans += bin_6bit[i]
        
    return ans