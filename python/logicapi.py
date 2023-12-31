from tkinter import * 
from tkinter import messagebox
from tkinter import ttk
import sqlite3
import bcrypt


class logicap:
    
    def __init__(self) -> None:
        pass
    
    
    #conexion 
    
    def conexionBD(self):
        
        try:
            conexion= sqlite3.connect("C:/Users/india/Downloads/PROYECTO INTEGRADOR.db")
            print("conectado a la base BD")
            return conexion
        
        except sqlite3.OperationalError:
            print("no se pudo conectar")
            
            
    def guardarcliente (self,nom,pro,can):
        
       conx=self.conexionBD()
       
       if(nom == "" or pro=="" or can ==""):
           messagebox.showwarning("aviso","fomulario incompleto")
           
       else:
           
           cursor=conx.cursor()
           datos=(nom,pro,can)
           qrisert="insert into clientes (nombre,producto,cantidad) values (?,?,?)"
           
           cursor.execute(qrisert,datos)
           conx.commit()
           conx.close
           messagebox.showinfo("exito","usuario guardado")
           
    def guardarempleado (self,nom1,area,pue):
        
       conx=self.conexionBD()
       
       if(nom1 == "" or area==""  or pue==""):
           messagebox.showwarning("aguas","fomulario incompleto")
           
       else:
           
           cursor=conx.cursor()
           datos=(nom1,area,pue)
           qrisert="insert into empleados (nombre,area,puesto) values (?,?,?)"
           
           cursor.execute(qrisert,datos)
           conx.commit()
           conx.close
           messagebox.showinfo("exito","usuario guardado")
           
           
           
    def guardarprovedor (self,nom2,pro2,can2):
        
       conx=self.conexionBD()
       
       if(nom2 == "" or pro2=="" or can2 ==""):
           messagebox.showwarning("aguas","fomulario incompleto")
           
       else:
           
           cursor=conx.cursor()
           datos=(nom2,pro2,can2)
           qrisert="insert into provedores (nombrep,productop,cantidadp) values (?,?,?)"
           
           cursor.execute(qrisert,datos)
           conx.commit()
           conx.close
           messagebox.showinfo("exito","usuario guardado")
           
           
           
    def registraentrada (self,nom3,area2,serie,can3,fecha):
        
       conx=self.conexionBD()
       
       if(nom3 == "" or area2=="" or serie =="" or can3 =="" or fecha =="" ):
           messagebox.showwarning("aviso","fomulario incompleto")
           
       else:
           
           cursor=conx.cursor()
           datos=(nom3,area2,serie,can3,fecha)
           qrisert="insert into entradas (nombre,area,serie,cantidad,fecha) values (?,?,?,?,?)"
           
           cursor.execute(qrisert,datos)
           conx.commit()
           conx.close
           messagebox.showinfo("exito","usuario guardado")

