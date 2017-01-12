from Tkinter import *
class error(Tk):
    def __init__(self, *args, **kwargs):
        
        master=Tk()
        self.master=master
        master.title("error!!!")
        self.Button1=Button(master,text="please check your time & date", command=self.close)
        self.Button1.pack()
        master.mainloop()    
    def close(self):
        self.master.destroy()
