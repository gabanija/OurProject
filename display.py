from database import database
from Tkinter import *
import datetime
a= str(datetime.date.today()) #for realtime date
time=(datetime.datetime.now()) #for realtime clock

class display(database):
    
    def __init__(self,master):
        self.master=master 
        master.title("Waktu Solat")
        database.__init__(self)
        database.create_table(self)
        database.query_JHR02(self)
        self.Button1=Button(master,text="+",command=self.data_entry)
        self.Button1.pack()
        self.Labelh=Label(master,text="{} Johor Bahru\nKota Tinggi,Mersing".format(time.strftime("%Y-%m-%d %H:%M")))#variable time is defined without second 
        self.Labelh.pack()
        self.Labela=Label(master,text="{}{}".format(self.nama[0],self.waktu[0]),anchor=W,justify=LEFT)
        self.Labela.pack()
        self.Labelb=Label(master,text="{}{}".format(self.nama[1],self.waktu[1]),anchor=W,justify=LEFT)
        self.Labelb.pack()
        self.Labelc=Label(master,text="{}{}".format(self.nama[2],self.waktu[2]),anchor=W,justify=LEFT)
        self.Labelc.pack()
        self.Labeld=Label(master,text="{}{}".format(self.nama[3],self.waktu[3]),anchor=W,justify=LEFT)
        self.Labeld.pack()
        self.Labele=Label(master,text="{}{}".format(self.nama[4],self.waktu[4]),anchor=W,justify=LEFT)
        self.Labele.pack()
        self.Labelf=Label(master,text="{}{}".format(self.nama[5],self.waktu[5]),anchor=W,justify=LEFT)
        self.Labelf.pack()
        self.Labelg=Label(master,text="{}{}".format(self.nama[6],self.waktu[6]),anchor=W,justify=LEFT)
        self.Labelg.pack()
        
        
    def data_entry(self):
        self.var1=IntVar()
        self.var2=IntVar()
        self.var3=IntVar()
        JHR01=Tk()
        self.JHR01=JHR01
        self.radio1=Radiobutton(JHR01,text="JHR01",variable=self.var1,value=1,command=self.JHR1)
        self.radio1.pack()
        self.radio2=Radiobutton(JHR01,text="JHR03",variable=self.var2,value=2,command=self.JHR3)
        self.radio2.pack()
        self.radio3=Radiobutton(JHR01,text="JHR04",variable=self.var3,value=3,command=self.JHR4)
        self.radio3.pack()
        self.master.withdraw()
        self.JHR01.mainloop()
        
    def JHR1(self):
        
        JHR1=Tk()
        self.JHR1=JHR1
        database.__init__(self)
        database.create_table(self)
        database.query_JHR01(self)
        self.Button1=Button(JHR1,text="<<",command=self.backJHR1)
        self.Button1.pack()
        self.Labelh=Label(JHR1,text="{} Pulau Aur,Pemanggil".format(time.strftime("%Y-%m-%d %H:%M")))#variable time is defined without second 
        self.Labelh.pack()
        self.Labela=Label(JHR1,text="{}{}".format(self.nama[0],self.waktu[0]),anchor=W,justify=LEFT)
        self.Labela.pack()
        self.Labelb=Label(JHR1,text="{}{}".format(self.nama[1],self.waktu[1]),anchor=W,justify=LEFT)
        self.Labelb.pack()
        self.Labelc=Label(JHR1,text="{}{}".format(self.nama[2],self.waktu[2]),anchor=W,justify=LEFT)
        self.Labelc.pack()
        self.Labeld=Label(JHR1,text="{}{}".format(self.nama[3],self.waktu[3]),anchor=W,justify=LEFT)
        self.Labeld.pack()
        self.Labele=Label(JHR1,text="{}{}".format(self.nama[4],self.waktu[4]),anchor=W,justify=LEFT)
        self.Labele.pack()
        self.Labelf=Label(JHR1,text="{}{}".format(self.nama[5],self.waktu[5]),anchor=W,justify=LEFT)
        self.Labelf.pack()
        self.Labelg=Label(JHR1,text="{}{}".format(self.nama[6],self.waktu[6]),anchor=W,justify=LEFT)
        self.Labelg.pack()
        self.JHR01.destroy()
        self.JHR1.mainloop()
        
    def JHR3(self):
        JHR3=Tk()
        self.JHR3=JHR3
        database.__init__(self)
        database.create_table(self)
        database.query_JHR03(self)
        self.Button1=Button(JHR3,text="<<",command=self.backJHR3)
        self.Button1.pack()
        self.Labelh=Label(JHR3,text="{} Kluang,Pontian".format(time.strftime("%Y-%m-%d %H:%M")))#variable time is defined without second 
        self.Labelh.pack()
        self.Labela=Label(JHR3,text="{}{}".format(self.nama[0],self.waktu[0]),anchor=W,justify=LEFT)
        self.Labela.pack()
        self.Labelb=Label(JHR3,text="{}{}".format(self.nama[1],self.waktu[1]),anchor=W,justify=LEFT)
        self.Labelb.pack()
        self.Labelc=Label(JHR3,text="{}{}".format(self.nama[2],self.waktu[2]),anchor=W,justify=LEFT)
        self.Labelc.pack()
        self.Labeld=Label(JHR3,text="{}{}".format(self.nama[3],self.waktu[3]),anchor=W,justify=LEFT)
        self.Labeld.pack()
        self.Labele=Label(JHR3,text="{}{}".format(self.nama[4],self.waktu[4]),anchor=W,justify=LEFT)
        self.Labele.pack()
        self.Labelf=Label(JHR3,text="{}{}".format(self.nama[5],self.waktu[5]),anchor=W,justify=LEFT)
        self.Labelf.pack()
        self.Labelg=Label(JHR3,text="{}{}".format(self.nama[6],self.waktu[6]),anchor=W,justify=LEFT)
        self.Labelg.pack()
        self.JHR01.destroy()
        self.JHR3.mainloop()
        
    def JHR4(self):
        JHR4=Tk()
        self.JHR4=JHR4
        database.__init__(self)
        database.create_table(self)
        database.query_JHR04(self)
        self.Button1=Button(JHR4,text="<<",command=self.backJHR4)
        self.Button1.pack()
        self.Labelh=Label(JHR4,text="{} Batu Pahat,Muar\nSegamat,Gemas".format(time.strftime("%Y-%m-%d %H:%M")))#variable time is defined without second 
        self.Labelh.pack()
        self.Labela=Label(JHR4,text="{}{}".format(self.nama[0],self.waktu[0]),anchor=W,justify=LEFT)
        self.Labela.pack()
        self.Labelb=Label(JHR4,text="{}{}".format(self.nama[1],self.waktu[1]),anchor=W,justify=LEFT)
        self.Labelb.pack()
        self.Labelc=Label(JHR4,text="{}{}".format(self.nama[2],self.waktu[2]),anchor=W,justify=LEFT)
        self.Labelc.pack()
        self.Labeld=Label(JHR4,text="{}{}".format(self.nama[3],self.waktu[3]),anchor=W,justify=LEFT)
        self.Labeld.pack()
        self.Labele=Label(JHR4,text="{}{}".format(self.nama[4],self.waktu[4]),anchor=W,justify=LEFT)
        self.Labele.pack()
        self.Labelf=Label(JHR4,text="{}{}".format(self.nama[5],self.waktu[5]),anchor=W,justify=LEFT)
        self.Labelf.pack()
        self.Labelg=Label(JHR4,text="{}{}".format(self.nama[6],self.waktu[6]),anchor=W,justify=LEFT)
        self.Labelg.pack()
        self.JHR01.destroy()
        self.JHR4.mainloop()
        
    def backJHR1(self):
        self.master.deiconify()
        self.JHR1.destroy()
        
        
    def backJHR3(self):
        self.master.deiconify()
        self.JHR3.destroy()
        
        
    def backJHR4(self):
        self.master.deiconify()
        self.JHR4.destroy()
