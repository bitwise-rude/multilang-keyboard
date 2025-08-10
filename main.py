import tkinter as tk
from googletrans import Translator
from pynput import keyboard
import pyautogui,threading,pyperclip,time




root = tk.Tk()
root.title("Multilanguage-Typer")
tk.Label(text="Welcome, contact Meyan on how to use it",font=["Algerain",17]).pack()

def trans(thing,src="en",d="en"):
    tr = Translator()
    return tr.translate(thing,src=src,dest=d).text

def write(types):
    global little,am
    am=True
    pyautogui.hotkey("ctrl","a")
    pyautogui.hotkey("delete")
    little= types
    pyperclip.copy(types)
    pyautogui.hotkey("ctrl","v")
    pyautogui.press("enter")
    am=False


def show(thing):
    pyautogui.alert(str(thing))

running =True
recent_value = pyperclip.paste()
def checker():
    global recent_value
    while running:
        if TURN:
            tmp_value = pyperclip.paste()
            if tmp_value != recent_value and  tmp_value != little :
                print("HI")
                recent_value = tmp_value
                show(trans(recent_value,src="it",d="en"))
            time.sleep(0.1)

listening = False
string = ""
little=""
am = False
TURN = False
def key(key):
    if TURN:
        global string,listening
        
        if str(key)=="Key.insert" :
            listening = not listening
            print("NOW")
            if string:
                write(trans(string,src="en",d="it"))
                string = ""
        else:
            if listening:
                ll = str(key)
                if ll =="Key.space":
                    ll = " "
                elif ll=="Key.backspace":
                    string=string[:-1]
                    ll=""
                else:
                    ll=ll[1:]
                    ll= ll[:-1]
                
                string = string + ll

def turn():
    global TURN
    if not TURN:
        btn['text']="Press to turn OFF the app"
        btn['fg'] = "green"
    else:
        btn['text']="Press to turn ON the app"
        btn['fg'] = "red"
    TURN=not TURN

btn = tk.Button(text="Press to turn ON the app",fg='red',font=["Elephant",14],command=turn)
btn.pack(pady=50)
tk.Label(text="MADE BY MEYAN ADHIKARI FOR MANOHAR").pack(side="bottom")

threading.Thread(target=checker).start()
languages = ["ar"]
listener = keyboard.Listener(
        on_press=key) 
listener.start()

root.mainloop()
running = False
