from error import error
from Tkinter import *
import csv
import sqlite3
import datetime
a= str(datetime.date.today()) #for realtime date
time=(datetime.datetime.now()) #for realtime clock
class database(error):
    def __init__(self,dbname=":memory:"):
        '''creating the database'''
        self.dbname=dbname
        self.conn=sqlite3.connect(self.dbname)
        
        
    def cursor(self):
        """Return a cursor on the database"""
        
        return self.conn.cursor()
    
    def create_table(self):
        """Create database table for the waktu solat.
        Removes any existing data that might be in the 
        database."""
        self.conn.cursor()
        cursor = self.cursor()
        cursor.execute("DROP TABLE IF EXISTS likes")
        cursor.execute("""CREATE TABLE t117 (id,code,imsak,subuh,syuruk,zohor,asar,maghrib,isyak,solat_date text ,create_date,status);""")
       
    def query_JHR02(self, link="C:\Python27\Info_Waktu_Solat_-_2016.csv"):
        """query_JHR02  in the database"""
        b="JHR02"
        self.b=b
        cursor = self.cursor()
        self.link=link
        with open(self.link,'rb') as fin: 
        # csv.DictReader uses first line in file for column headings by default
            dr = csv.DictReader(fin) # comma is default delimiter, fin is iterable value =all values 
            to_db = [(i['id'], i['code'],i['imsak'], i['subuh'], i['syuruk'], i['zohor'], i['asar'], i['maghrib'], i['isyak'], i['solat_date'], i['create_date'], i['status']) for i in dr]
        #for i in dr, taking all values in dr transfer to to_db
        cursor.executemany("INSERT INTO t117 (id,code,imsak,subuh,syuruk,zohor,asar,maghrib,isyak,solat_date,create_date,status) VALUES (?,?,?,?,?,?,?,?,?,?,?,?);", to_db)#write to t116 table
        cursor.execute("select * from t117 where solat_date=:a and code=:b", {"a": a, "b": b})
        #self.row=row
        self.row=cursor.fetchone()
        if self.row: #good condition
         self.waktu=[self.row[2],self.row[3],self.row[4],self.row[5],self.row[6],self.row[7],self.row[8]]
         self.nama=["Imsak:","Subuh:","Syuruk:","Zohor:","Asar:","Maghrib:","Isyak:"]
        else:
          error.__init__(self,Tk)
        
        #print self.row
        
        #self.commit() #do not close yet, for future use 
        #cursor.execute("INSERT INTO likes (thing) VALUES (?)", (like, ))
        #self.commit()
        
    def query_JHR01(self, link="C:\Python27\Info_Waktu_Solat_-_2016.csv"):
        """query_JHR01  in the database"""
        b="JHR01"
        self.b=b
        cursor = self.cursor()
        self.link=link
        with open(self.link,'rb') as fin: 
        # csv.DictReader uses first line in file for column headings by default
            dr = csv.DictReader(fin) # comma is default delimiter, fin is iterable value =all values 
            to_db = [(i['id'], i['code'],i['imsak'], i['subuh'], i['syuruk'], i['zohor'], i['asar'], i['maghrib'], i['isyak'], i['solat_date'], i['create_date'], i['status']) for i in dr]
        #for i in dr, taking all values in dr transfer to to_db
        cursor.executemany("INSERT INTO t117 (id,code,imsak,subuh,syuruk,zohor,asar,maghrib,isyak,solat_date,create_date,status) VALUES (?,?,?,?,?,?,?,?,?,?,?,?);", to_db)#write to t116 table
        cursor.execute("select * from t117 where solat_date=:a and code=:b", {"a": a, "b": b})
        #self.row=row
        self.row=cursor.fetchone()
        if self.row: #good condition
         self.waktu=[self.row[2],self.row[3],self.row[4],self.row[5],self.row[6],self.row[7],self.row[8]]
         self.nama=["Imsak:","Subuh:","Syuruk:","Zohor:","Asar:","Maghrib:","Isyak:"]
        else:
          error.__init__(self,Tk)
       
    def query_JHR03(self, link="C:\Python27\Info_Waktu_Solat_-_2016.csv"):
        """query_JHR03  in the database"""
        b="JHR03"
        self.b=b
        cursor = self.cursor()
        self.link=link
        with open(self.link,'rb') as fin: 
        # csv.DictReader uses first line in file for column headings by default
            dr = csv.DictReader(fin) # comma is default delimiter, fin is iterable value =all values 
            to_db = [(i['id'], i['code'],i['imsak'], i['subuh'], i['syuruk'], i['zohor'], i['asar'], i['maghrib'], i['isyak'], i['solat_date'], i['create_date'], i['status']) for i in dr]
        #for i in dr, taking all values in dr transfer to to_db
        cursor.executemany("INSERT INTO t117 (id,code,imsak,subuh,syuruk,zohor,asar,maghrib,isyak,solat_date,create_date,status) VALUES (?,?,?,?,?,?,?,?,?,?,?,?);", to_db)#write to t116 table
        cursor.execute("select * from t117 where solat_date=:a and code=:b", {"a": a, "b": b})
        #self.row=row
        self.row=cursor.fetchone()
        if self.row: #good condition
         self.waktu=[self.row[2],self.row[3],self.row[4],self.row[5],self.row[6],self.row[7],self.row[8]]
         self.nama=["Imsak:","Subuh:","Syuruk:","Zohor:","Asar:","Maghrib:","Isyak:"]
        else:
          error.__init__(self,Tk)
          
    def query_JHR04(self, link="C:\Python27\Info_Waktu_Solat_-_2016.csv"):
        """query_JHR04  in the database"""
        b="JHR04"
        self.b=b
        cursor = self.cursor()
        self.link=link
        with open(self.link,'rb') as fin: 
        # csv.DictReader uses first line in file for column headings by default
            dr = csv.DictReader(fin) # comma is default delimiter, fin is iterable value =all values 
            to_db = [(i['id'], i['code'],i['imsak'], i['subuh'], i['syuruk'], i['zohor'], i['asar'], i['maghrib'], i['isyak'], i['solat_date'], i['create_date'], i['status']) for i in dr]
        #for i in dr, taking all values in dr transfer to to_db
        cursor.executemany("INSERT INTO t117 (id,code,imsak,subuh,syuruk,zohor,asar,maghrib,isyak,solat_date,create_date,status) VALUES (?,?,?,?,?,?,?,?,?,?,?,?);", to_db)#write to t116 table
        cursor.execute("select * from t117 where solat_date=:a and code=:b", {"a": a, "b": b})
        #self.row=row
        self.row=cursor.fetchone()
        if self.row: #good condition
         self.waktu=[self.row[2],self.row[3],self.row[4],self.row[5],self.row[6],self.row[7],self.row[8]]
         self.nama=["Imsak:","Subuh:","Syuruk:","Zohor:","Asar:","Maghrib:","Isyak:"]
        else:
          error.__init__(self,Tk)
