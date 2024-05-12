import tkinter 


class Login:
    def __init__(self,root):

        self.label = tkinter.Label(root,text="write this person name:",bg="Violet",font=("Goudy Stout",7),cursor="heart")
        self.label.grid(row=0,column=0)
        self.label2 = tkinter.Label(root,text="write a few cute words about her/him<3",bg="Violet",font=("Goudy Stout",7),cursor="heart")
        self.label2.grid(row=1,column=0)
        self.entry = tkinter.Entry(root,bg="Violet",font=("Arial Rounded MT",8),cursor="heart")
        self.entry.grid(row=0,column=1,padx=30,pady=50)
        self.entry2 = tkinter.Entry(root,bg="Violet",font=("Arial Rounded MT",8),cursor="heart")
        self.entry2.grid(row=1,column=1,padx=30,pady=50)
        self.button = tkinter.Button(root,text="send her/him!(✿◠‿◠)",bg="LightSkyBlue",font=("Forte",12),cursor="crosshair")
        self.button.grid(row=2,columnspan=4,padx=20,pady=40)
        
if __name__=="__main__":
    root =  tkinter.Tk()
    login = Login(root)
    root.title("cuties menu(^◕.◕^)❤️")




    root.mainloop()




































