import sqlite3

class Database:
    def __init__(self,database):
        self.database = database

    def add_employee(self,name,surname): # untested
        con = sqlite3.connect(self.database)
        cursor = con.cursor()
        cursor.execute("INSERT INTO employees(name,surname) VALUES (?,?)", [name,surname])
        cursor.execute("INSERT INTO availability(employee_id, day,start_time,end_time) VALUES ((SELECT eid FROM employees WHERE name=?),?,?,?)",[name,"none","none","none"])
        con.commit()
        con.close()
        return True
 
    def get_all_employees(self):
        con = sqlite3.connect(self.database)
        cursor = con.cursor()
        result = [list(tup) for tup in cursor.execute("SELECT name,surname FROM employees").fetchall()]
        con.close()
        return result

    def get_shift_info(self,name):
        con = sqlite3.connect(self.database)
        cursor = con.cursor()
        shift_data = [list(tup) for tup in cursor.execute("SELECT day,start_time,end_time FROM availability WHERE employee_id=(SELECT eid FROM employees WHERE name=?)",[name]).fetchall()]
        con.close()
        return shift_data
    
    def update_rota(self,name,to_time,from_time,day):
        con = sqlite3.connect(self.database)
        cursor = con.cursor()
        cursor.execute("UPDATE availability SET day=?,start_time=?,end_time=? WHERE employee_id=(SELECT eid FROM employees WHERE name=?)",[day,from_time,to_time,name])
        con.commit()
        con.close()
        return True
    
    def create_blank_shift(self,name):
        con = sqlite3.connect(self.database)
        cursor = con.cursor()
        cursor.execute("INSERT INTO availability(employee_id,day,start_time,end_time) VALUES ((SELECT eid FROM employees WHERE name=?),?,?,?)",[name,"none,","none","none"])
        con.commit()
        con.close()


