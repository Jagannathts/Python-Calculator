#!/usr/bin/env python
# coding: utf-8

# In[2]:


from tkinter import *

loop=Tk()
equation=""
loop.title('Home Page')
Label(loop,text='Calculator').grid(row=0,column=0)

bt1=Button(loop,text='1',command=lambda:show("1"))
bt1.grid(row=6,column=1)
bt2=Button(loop,text='2',command=lambda:show("2"))
bt2.grid(row=6,column=2)
bt3=Button(loop,text='3',command=lambda:show("3"))
bt3.grid(row=6,column=3)
bt4=Button(loop,text='/',command=lambda:show("/"))
bt4.grid(row=6,column=4)
bt5=Button(loop,text='4',command=lambda:show("4"))
bt5.grid(row=7,column=1)
bt6=Button(loop,text='5',command=lambda:show("5"))
bt6.grid(row=7,column=2)
bt7=Button(loop,text='6',command=lambda:show("6"))
bt7.grid(row=7,column=3)
bt8=Button(loop,text='*',command=lambda:show("*"))
bt8.grid(row=7,column=4)           
bt9=Button(loop,text='7',command=lambda:show("7"))
bt9.grid(row=8,column=1)
bt10=Button(loop,text='8',command=lambda:show("8"))
bt10.grid(row=8,column=2)
bt11=Button(loop,text='9',command=lambda:show("9"))
bt11.grid(row=8,column=3)
bt12=Button(loop,text='+',command=lambda:show("+"))
bt12.grid(row=8,column=4)
bt13=Button(loop,text='0',command=lambda:show("0"))
bt13.grid(row=9,column=1)
bt14=Button(loop,text='.',command=lambda:show("."))
bt14.grid(row=9,column=2)
bt15=Button(loop,text='=',command=lambda:show(calculate()))
bt15.grid(row=9,column=3)
bt16=Button(loop,text='-',command=lambda:show("-"))
bt16.grid(row=9,column=4)
bt17=Button(loop,text='Clear',command=lambda:show(clear()))
bt17.grid(row=9,column=5)

label_result=(Label(loop,width=5,height=2,text="",font=("arial",30)))
label_result.grid(row=1,column=0)

lb1=Label(loop)
lb1.grid(row=2,column=2)

def show(value):
    global equation
    equation=equation+value
    label_result.config(text=equation)
    
def clear():
    global equation
    equation=""
    label_result.config(text=equation)
    
def calculate():
    global equation
    result=""
    
    if equation !="":
        result=eval(equation)
        label_result.config(text=result)

loop.mainloop()


# In[ ]:




