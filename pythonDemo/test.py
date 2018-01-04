# encoding=utf-8
import matplotlib.pyplot as plt
import numpy as np

set1 = set()
print set1
s = {1, 3, 4}
s1 = {(1, 2), (2, 5)}
print s, s1
students = {"peter", "john"}
# students.remove("j")   #没有报错
print students

st1 = {"peter", "john", "tim"}
st2 = {"peter", "johnson", "tim"}
print st1.issuperset({"john"})
print st1.issubset(st2)
print ({1, 2} > {1, 2, 4})

d = {(1, 2):1, (3, 4):3}
print d
# fig1 = plt.figure()
# t1 = np.arange(0.0, 2.0, 0.1)
# t2 = np.arange(0.0, 2.0, 0.01)
#
# # note that plot returns a list of lines.  The "l1, = plot" usage
# # extracts the first element of the list into l1 using tuple
# # unpacking.  So l1 is a Line2D instance, not a sequence of lines
# l1, = plt.plot(t2, np.exp(-t2))
# l2, l3 = plt.plot(t2, np.sin(2 * np.pi * t2), '--go', t1, np.log(1 + t1), '.')
# l4, = plt.plot(t2, np.exp(-t2) * np.sin(2 * np.pi * t2), 'rs-.')
#
# plt.xlabel('time')
# plt.ylabel('volts')
# plt.title('Damped oscillation')
#
# plt.show()

import win32com.client as wincl
from tkinter import *


def text2Speech():
 text = e.get()
 speak = wincl.Dispatch("SAPI.SpVoice")
 speak.Speak(text)


#window configs
tts = Tk()
tts.wm_title("Text to Speech")
tts.geometry("225x105")
tts.config(background="#708090")


f=Frame(tts,height=280,width=500,bg="#bebebe")
f.grid(row=0,column=0,padx=10,pady=5)
lbl=Label(f,text="Enter your Text here : ")
lbl.grid(row=1,column=0,padx=10,pady=2)
e=Entry(f,width=30)
e.grid(row=2,column=0,padx=10,pady=2)
btn=Button(f,text="Speak",command=text2Speech)
btn.grid(row=3,column=0,padx=20,pady=10)
tts.mainloop()