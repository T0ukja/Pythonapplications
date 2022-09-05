from tkinter import *
import threading
import time
from playsound import playsound
window=Tk()

def sound(morse_code):
    print(morse_code)
    for char in morse_code:
            if char == '-':
                playsound('line.wav', block=False)
                time.sleep(0.15)
            elif char == '.':
                playsound('dot.wav', block=False)
                time.sleep(0.15)
            elif char == '|':
                continue
            time.sleep(0.05)
             
def morse(txt):

    encrypt = {'A':'.-', 'B':'-...', 'C':'-.-.',
               'D':'-..', 'E':'.', 'F':'..-.',
               'G':'--.', 'H':'....', 'I':'..',
               'J':'.---', 'K':'-.-', 'L':'.-..',
               'M':'--', 'N':'-.', 'O':'---',
               'P':'.--.', 'Q':'--.-', 'R':'.-.',
               'S':'...', 'T':'-', 'U':'..-',
               'V':'...-', 'W':'.--', 'X':'-..-',
               'Y':'-.--', 'Z':'--..', ' ':'.....'}
    decrypt = {w: a for a, w in encrypt.items()}
    
    if '-' in txt:
        arvo = ''.join(decrypt[i] for i in txt.split())
        lbl3.configure(text=arvo)
        txtfld.delete(0, END)
    arvo = ' '.join(encrypt[i] for i in txt.upper())
    lbl3.configure(text=arvo)
    txtfld.delete(0, END)


window.title("Morse Coder")
txtfld=Entry(window, text="give text", bd=5)
txtfld.place(x=80, y=70)
lbl=Label(window, text="Morse Coder", fg='red', font=("Helvetica", 15))
lbl.place(x=80, y=20)
btn=Button(window, text="Generate text to Morse code", fg='blue', command=lambda: morse(txtfld.get()))
btn.place(x=70, y=100)
btn=Button(window, text="Generate Morse code to text", fg='blue',command=lambda: morse(txtfld.get())
)
btn.place(x=70, y=130)
btn=Button(window, text="Play sound", fg='blue', command=lambda:sound(lbl3.cget("text")))
btn.place(x=110, y=160)
lbl3 = Message(window, text="translated text will be here")
lbl3.place(x=40, y=190, width=200, height=60)
window.geometry("300x250")
window.mainloop()
