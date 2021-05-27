from funct import Base64, ASCII
from tkinter import *

root = Tk()

root.geometry('500x270')
root.resizable(0,0)
root.title("Python Mini project")

Label(root, text ='MESSAGE ENCODER-DECODER', font = 'arial 18 bold').place(x=60, y = 10)


Text = StringVar()
private_key = StringVar()
mode = StringVar()
Result = StringVar()

def Encode(key,message):
    enc=""

    for i in range(len(message)):
        key_c = key[i % len(key)]
        enc= enc+(chr((ord(message[i]) + ord(key_c)) % 128))
    return Base64(enc)

def Decode(key,message):
    dec=[]
    
    message = ASCII(message)
    for i in range(len(message)):
        key_c = key[i % len(key)]
        dec.append(chr((128 + ord(message[i])- ord(key_c)) % 128))
    
    return "".join(dec)

def Mode():
    if(mode.get() == 'e'):
        Result.set(Encode(private_key.get(), Text.get()))
    elif(mode.get() == 'd'):
        Result.set(Decode(private_key.get(), Text.get()))
    else:
        Result.set('Invalid Mode')

def Reset():
    Text.set("")
    private_key.set("")
    mode.set("")
    Result.set("")

Label(root, font= 'arial 12 bold', text='MESSAGE').place(x= 60,y=60)
Entry(root, font = 'arial 10', textvariable = Text, bg = 'ghost white').place(x=290, y = 60)

Label(root, font = 'arial 12 bold', text ='KEY').place(x=60, y = 90)
Entry(root, font = 'arial 10', textvariable = private_key , bg ='ghost white').place(x=290, y = 90)

Label(root, font = 'arial 12 bold', text ='MODE(e-encode, d-decode)').place(x=60, y = 120)
Entry(root, font = 'arial 10', textvariable = mode , bg= 'ghost white').place(x=290, y = 120)
Entry(root, font = 'arial 10 bold', textvariable = Result, bg ='ghost white').place(x=290, y = 150)


Button(root, font = 'arial 10 bold' ,text ='RESET' ,width =6, command = Reset,bg = 'LimeGreen').place(x=150, y = 190)

Button(root, font = 'arial 10 bold',text= 'RESULT' , width = 6, command = Mode,bg = 'LightGray').place(x=260, y = 190)

root.mainloop()