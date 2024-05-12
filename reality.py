import tkinter

root =  tkinter.Tk()

root.resizable(width=False,height=False)

root.geometry("400x500")

hi = tkinter.StringVar()

def show():
    data = hi.get()
    print(data)

    
button = tkinter.Button(root,text="idc",command=show)
button.pack()

entry = tkinter.Entry(root,textvariable=hi)
entry.pack()



root.mainloop()




































