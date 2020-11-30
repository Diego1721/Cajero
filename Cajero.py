from tkinter import *
from tkinter import messagebox 
from tkinter import ttk
import tkinter as tk
import sqlite3
#------------------------Conexion--------------------------------------
DB_PATH= "Cliente"
class Manager(object):
	def __init__(self,database=None):
		if not database:
			database= ':memory:'
		self.miConexion= sqlite3.connect(database)
		self.miCursor= self.miConexion.cursor()
	def insert(self,obj):
		query="INSERT INTO Clientes VALUES ('{}','{}','{}','{}','{}','{}')".format(obj._Cuenta__Usuario,obj._Cuenta__Password,obj._Cuenta__Credito,obj._Cuenta__Saldo,obj._Cuenta__NombreU,obj._Cuenta__ApellidoU)
		self.miCursor.execute(query)
		self.miConexion.commit()
#--------------------Clase---------------------------------------------
miConexion2= sqlite3.connect("Cliente")
miCursor2= miConexion2.cursor()
class Cuenta(object):
	"Currency Model"
	objects= Manager(DB_PATH)
	def __init__(self,Usuario,Password,Credito,Saldo,NombreU,ApellidoU):
		self.__Usuario = Usuario
		self.__Password = Password
		self.__Credito = Credito
		self.__Saldo = Saldo
		self.__NombreU = NombreU
		self.__ApellidoU = ApellidoU
	def __repr__(self):
		return u'{}'.format(self.__NombreU)
#--------------Metodos--------------------------------------------------
class Metodos():
	def ValCod():
		if Caja2.get()=="":
			messagebox.showerror("Error","No puede dejar la casilla en blanco")
		else:
			miCursor2.execute("SELECT * FROM Clientes WHERE Password = "+ Caja2.get())
			miConexion2.commit()
			if not miCursor2.execute("SELECT * FROM Clientes WHERE Password = "+ Caja2.get()):
				messagebox.showwarning("Error","La contraseña no esta en el sistema")
			elif miCursor2.execute("SELECT * FROM Clientes WHERE Password = "+ Caja2.get()):
				for user in miCursor2.fetchall():
					messagebox.showinfo("Usuario encontrado","Bienvenido "+ user[4] +" "+ user[5])
					raiz2= Tk()
					raiz2.title("Menu Opciones")
					raiz2.iconbitmap("Bancolombia.ico")
					raiz2.geometry("250x150")
					BotonCon=Button(raiz2, text="Consultar Saldo", command=lambda:Metodos.ConsulSal(user[3],raiz2))
					BotonCon.place(x=10,y=10)
					BotonSac=Button(raiz2,text="Sacar Plata",command=lambda:Metodos.SacPlat(user[3],user[1],raiz2))
					BotonSac.place(x=170,y=10)
					BotonTran=Button(raiz2,text="Tranferencia",command=lambda:Metodos.Transferencia(user[3],user[1],raiz2))
					BotonTran.place(x=10,y=50)
					BotonCre=Button(raiz2,text="Pedir un Credito",command=lambda:Metodos.PedCre(user[2],user[3],user[1],raiz2))
					BotonCre.place(x=150,y=50)
					BotonSalir=Button(raiz2,text="Salir",command=lambda:raiz2.destroy())
					BotonSalir.place(x=210,y=110)
	def Transferencia(ob,passw,raiz2):
		raiz6=Tk()
		raiz6.title("Transferencia")
		raiz6.iconbitmap("Bancolombia.ico")
		raiz6.geometry("250x150")
		def is_valid_char(char):
    			return char in "ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz."
		validatecommandE = raiz6.register(is_valid_char)
		def is_valid_int(int):
				return int in "012345678910."
		validatecommand2E= raiz6.register(is_valid_int)
		LabelT=Label(raiz6,text="¿Cuanto desea transferir?")
		LabelT.grid(sticky="w",padx=50,pady=5)
		Caja4=Entry(raiz6,validate="key",validatecommand=(validatecommand2E,"%S"), width=15)
		Caja4.grid(sticky="w",padx=75,pady=5)
		LabelT2=Label(raiz6,text="¿A que cuenta desea transferir?")
		LabelT2.grid(sticky="w",padx=40,pady=5)
		Caja5=Entry(raiz6,validate="key",validatecommand=(validatecommand2E,"%S"), width=15)
		Caja5.grid(sticky="w",padx=75,pady=5)
		BotoTra=Button(raiz6,text="Validar",command=lambda:ValMon(ob,passw,raiz2))
		BotoTra.place(x=95,y=120)
		def ValMon(ob,passw,raiz2):
			trav=int(Caja4.get())
			if trav<=ob:
				tesVa=ob-trav
				miCursor2.execute("UPDATE Clientes SET Saldo = ? WHERE Password = ?",(tesVa,passw))
				miCursor2.execute("SELECT * FROM Clientes WHERE Password = ?",(Caja5.get(),))
				for user2 in miCursor2.fetchall():
					tav2= user2[3]+trav
					miCursor2.execute("UPDATE Clientes SET Saldo = ? WHERE Password = ?",(tav2,Caja5.get()))
				miConexion2.commit()
				messagebox.showinfo("Saldo nuevo","Su nuevo saldo es de: "+str(tesVa))
				messagebox.showinfo("Gracias","Si desea hacer mas transacciones ingrese de nuevo")
				raiz6.destroy()
				raiz2.destroy()
			else:
				messagebox.showerror("Error","Fondos Insuficientes")
				raiz6.destroy()
				raiz2.destroy()
	def PedCre(Cre,Sal,Passw,raiz2):
		raiz7=Tk()
		raiz7.title("Credito")
		raiz7.iconbitmap("Bancolombia.ico")
		raiz7.geometry("250x100")
		def is_valid_char(char):
    			return char in "ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz."
		validatecommandE = raiz7.register(is_valid_char)
		def is_valid_int(int):
				return int in "012345678910."
		validatecommand2E= raiz7.register(is_valid_int)
		LabelC=Label(raiz7,text="¿Cuanto credito desea solicitar?")
		LabelC.grid(sticky="w",padx=40,pady=5)
		Caja6=Entry(raiz7,validate="key",validatecommand=(validatecommand2E,"%S"), width=15)
		Caja6.grid(sticky="w",padx=75,pady=5)
		BotPed=Button(raiz7,text="Pedir",command=lambda:Pedir(Cre,Sal,Passw,raiz2))
		BotPed.place(x=100,y=60)
		def Pedir(Cre,Sal,Passw,raiz2):
			ObC= int(Caja6.get())
			if ObC<=Cre:
				ResC=Cre-ObC
				NewSal=Sal+ObC
				miCursor2.execute("UPDATE Clientes SET Saldo = ?, Credito = ? WHERE Password = ?",(NewSal,ResC,Passw))
				miConexion2.commit()
				messagebox.showinfo("Correcto","Credito Aprovado")
				messagebox.showinfo("Gracias","Si desea hacer mas transacciones ingrese de nuevo")
				raiz7.destroy()
				raiz2.destroy()
			else:
				messagebox.showerror("Error","Credito Insuficiente")
				raiz7.destroy()
				raiz2.destroy()
	def Crear():
		raiz5=Tk()
		raiz5.title("Crear Usuario")
		raiz5.iconbitmap("Bancolombia.ico")
		raiz5.geometry("230x280")
		def is_valid_char(char):
    			return char in "ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz."
		validatecommandE = raiz5.register(is_valid_char)
		def is_valid_int(int):
				return int in "012345678910."
		validatecommand2E= raiz5.register(is_valid_int)
		MiLabel4=Label(raiz5,text="Usuario")
		MiLabel4.grid(sticky="w",padx=10,pady=10)
		MiLabel5=Label(raiz5,text="Contraseña")
		MiLabel5.grid(sticky="w",padx=10,pady=10)
		MiLabel6=Label(raiz5,text="Credito")
		MiLabel6.grid(sticky="w",padx=10,pady=10)
		MiLabel7=Label(raiz5,text="Saldo")
		MiLabel7.grid(sticky="w",padx=10,pady=10)
		MiLabel8=Label(raiz5,text="Nombre Usuario")
		MiLabel8.grid(sticky="w",padx=10,pady=10)
		MiLabel9=Label(raiz5,text="Apellido Usuario")
		MiLabel9.grid(sticky="w",padx=10,pady=10)
		BotIngre=Button(raiz5,text="Ingresar",command=lambda:Ingre())
		BotIngre.place(x=80,y=250)
		UsEnt=Entry(raiz5,validate="key",validatecommand=(validatecommandE,"%S"), width=10)
		UsEnt.grid(sticky="w",row=0,column=2)
		CoEnt=Entry(raiz5,validate="key",validatecommand=(validatecommand2E,"%S"), width=4)
		CoEnt.grid(sticky="w",row=1,column=2)
		CreEnt=Entry(raiz5,validate="key",validatecommand=(validatecommand2E,"%S"), width=10)
		CreEnt.grid(sticky="w",row=2,column=2)
		SalEnt=Entry(raiz5,validate="key",validatecommand=(validatecommand2E,"%S"), width=10)
		SalEnt.grid(sticky="w",row=3,column=2)
		NombEnt=Entry(raiz5,validate="key",validatecommand=(validatecommandE,"%S"), width=10)
		NombEnt.grid(sticky="w",row=4,column=2)
		ApeEnt=Entry(raiz5,validate="key",validatecommand=(validatecommandE,"%S"), width=10)
		ApeEnt.grid(sticky="w",row=5,column=2)
		def Ingre():
			ApeEnt.grid(sticky="w",row=5,column=2)
			AuxUs=UsEnt.get()
			AuxNom=NombEnt.get()
			AuxApe=ApeEnt.get()
			if AuxNom=="" or CoEnt.get()==0 or CreEnt.get()==0 or SalEnt.get()==0 or AuxNom=="" or AuxApe=="":
				messagebox.showerror("Error","No puede dejar campos en blanco")
				raiz5.destroy()
			else:
				Aux = Cuenta (Usuario=AuxUs,Password=CoEnt.get(),Credito=CreEnt.get(),Saldo=SalEnt.get(),NombreU=AuxNom,ApellidoU=AuxApe)
				Cuenta.objects.insert(Aux)
				messagebox.showinfo("Proceso Completado","La creacion de la cuenta fue un exito")
				raiz5.destroy()
	def InfoAd():
		messagebox.showwarning("Usuario no encontrado", "Los datos que usted ha ingresado no estan en el sistema")
	def ConsulSal(ob,raiz2):
		messagebox.showinfo("Saldo","El saldo de la cuenta es: "+str(ob))
		raiz2.destroy()
	def SacPlat(ob,passw,raiz2):
		raiz3=Tk()
		raiz3.title("Sacar Plata")
		raiz3.iconbitmap("Bancolombia.ico")
		raiz3.geometry("220x200")
		MiFrame2=Frame()
		MiFrame2.pack(fill="both",expand="True")
		MiLabel3=Label(raiz3,text="¿Cuanto desea retirar?")
		MiLabel3.place(x=50,y=10)
		Bot20=Button(raiz3,text="20.000",command=lambda:Operaciones.Opera20(ob,passw,raiz2,raiz3))
		Bot20.place(x=10,y=40)
		Bot50=Button(raiz3,text="50.000",command=lambda:Operaciones.Opera50(ob,passw,raiz2,raiz3))
		Bot50.place(x=160,y=40)
		Bot100=Button(raiz3,text="100.000",command=lambda:Operaciones.Opera100(ob,passw,raiz2,raiz3))
		Bot100.place(x=10,y=80)
		Bot150=Button(raiz3,text="150.000",command=lambda:Operaciones.Opera150(ob,passw,raiz2,raiz3))
		Bot150.place(x=160,y=80)
		Bot200=Button(raiz3,text="200.000",command=lambda:Operaciones.Opera200(ob,passw,raiz2,raiz3))
		Bot200.place(x=10,y=120)
		Bot300=Button(raiz3,text="300.000",command=lambda:Operaciones.Opera300(ob,passw,raiz2,raiz3))
		Bot300.place(x=160,y=120)
		BotOtro=Button(raiz3,text="Otro Valor",command=lambda:Operaciones.OperaValor(ob,passw,raiz2,raiz3))
		BotOtro.place(x=10,y=160)
		BotVolver=Button(raiz3,text="Volver",command=lambda:raiz3.destroy())
		BotVolver.place(x=160,y=160)
class Operaciones():
	def Opera20(ob,passw,raiz2,raiz3):
		res2=20000
		Res20=ob-res2
		if res2<=ob:
			miCursor2.execute("UPDATE Clientes SET Saldo = ? WHERE Password = ?",(Res20,passw))
			miConexion2.commit()
			messagebox.showinfo("Saldo nuevo","Su nuevo saldo es de: "+str(Res20))
			messagebox.showinfo("Gracias","Si desea hacer mas transacciones ingrese de nuevo")
			raiz3.destroy()
			raiz2.destroy()
		else:
			messagebox.showerror("Error","Fondos Insuficientes")
			raiz3.destroy()
			raiz2.destroy()
	def Opera50(ob,passw,raiz2,raiz3):
		res5=50000
		Res50=ob-res5
		if res5<=ob:
			miCursor2.execute("UPDATE Clientes SET Saldo = ? WHERE Password = ?",(Res50,passw))
			miConexion2.commit()
			messagebox.showinfo("Saldo nuevo","Su nuevo saldo es de: "+str(Res50))
			messagebox.showinfo("Gracias","Si desea hacer mas transacciones ingrese de nuevo")
			raiz3.destroy()
			raiz2.destroy()
		else:
			messagebox.showerror("Error","Fondos Insuficientes")
			raiz3.destroy()
			raiz2.destroy()
	def Opera100(ob,passw,raiz2,raiz3):
		res10=100000
		Res100=ob-res10
		if res10<=ob:
			miCursor2.execute("UPDATE Clientes SET Saldo = ? WHERE Password = ?",(Res100,passw))
			miConexion2.commit()
			messagebox.showinfo("Saldo nuevo","Su nuevo saldo es de: "+str(Res100))
			messagebox.showinfo("Gracias","Si desea hacer mas transacciones ingrese de nuevo")
			raiz3.destroy()
			raiz2.destroy()
		else:
			messagebox.showerror("Error","Fondos Insuficientes")
			raiz3.destroy()
			raiz2.destroy()
	def Opera150(ob,passw,raiz2,raiz3):
		res15=ob-150000
		Res150=ob-res15
		if res15<=ob:
			miCursor2.execute("UPDATE Clientes SET Saldo = ? WHERE Password = ?",(Res150,passw))
			miConexion2.commit()
			messagebox.showinfo("Saldo nuevo","Su nuevo saldo es de: "+str(Res150))
			messagebox.showinfo("Gracias","Si desea hacer mas transacciones ingrese de nuevo")
			raiz3.destroy()
			raiz2.destroy()
		else:
			messagebox.showerror("Error","Fondos Insuficientes")
			raiz3.destroy()
			raiz2.destroy()
	def Opera200(ob,passw,raiz2,raiz3):
		res20=200000
		Res200=ob-res20
		if res20<=ob:
			miCursor2.execute("UPDATE Clientes SET Saldo = ? WHERE Password = ?",(Res200,passw))
			miConexion2.commit()
			messagebox.showinfo("Saldo nuevo","Su nuevo saldo es de: "+str(Res200))
			messagebox.showinfo("Gracias","Si desea hacer mas transacciones ingrese de nuevo")
			raiz3.destroy()
			raiz2.destroy()
		else:
			messagebox.showerror("Error","Fondos Insuficientes")
			raiz3.destroy()
			raiz2.destroy()
	def Opera300(ob,passw,raiz2,raiz3):
		res30=300000
		if res30<=ob:
			Res300=ob-res30
			miCursor2.execute("UPDATE Clientes SET Saldo = ? WHERE Password = ?",(Res300,passw))
			miConexion2.commit()
			messagebox.showinfo("Saldo nuevo","Su nuevo saldo es de: "+str(Res300))
			messagebox.showinfo("Gracias","Si desea hacer mas transacciones ingrese de nuevo")
			raiz3.destroy()
			raiz2.destroy()
		else:
			messagebox.showerror("Error","Fondos Insuficientes")
			raiz3.destroy()
			raiz2.destroy()
	def OperaValor(ob,passw,raiz2,raiz3):
		raiz4=Tk()
		raiz4.title("Sacar Plata")
		raiz4.iconbitmap("Bancolombia.ico")
		raiz4.geometry("180x100")
		def is_valid_int2(int):
			return int in "012345678910."
		validatecommand3= raiz4.register(is_valid_int2)
		Label4=Label(raiz4,text="¿Cuanto dinero desea retirar?")
		Label4.grid(sticky="w",padx=10,pady=10)
		Caja3=Entry(raiz4,validate="key",validatecommand=(validatecommand3,"%S"))
		Caja3.grid(sticky="w",padx=30,pady=10)
		BotE=Button(raiz4,text="Enviar",command=lambda:Valor())
		BotE.place(x=70,y=70)
		def Valor():
			resv=int(Caja3.get())
			ResVa=ob-resv
			if resv<ob:
				miCursor2.execute("UPDATE Clientes SET Saldo = ? WHERE Password = ?",(ResVa,passw))
				miConexion2.commit()
				messagebox.showinfo("Saldo nuevo","Su nuevo saldo es de: "+str(ResVa))
				messagebox.showinfo("Gracias","Si desea hacer mas transacciones ingrese de nuevo")
				raiz4.destroy()
				raiz3.destroy()
				raiz2.destroy()
			else:
				messagebox.showerror("Error","Fondos Insuficientes")
				raiz4.destroy()
				raiz3.destroy()
				raiz2.destroy()
#--------------Interfaz-------------------------------------------------
raiz=Tk()
raiz.title("Cajero Bancolombia")
raiz.iconbitmap("Bancolombia.ico")
raiz.geometry("230x150")
MiFrame=Frame()
MiFrame.pack(fill="both", expand= "False")
#-------------------------------Validaciones----------------------------
def is_valid_char(char):
    return char in "ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz."
validatecommand = raiz.register(is_valid_char)
def is_valid_int(int):
	return int in "012345678910."
validatecommand2= raiz.register(is_valid_int)
#-------------Labels,Entrys,Buttons-------------------------------------
MiLabe=Label(MiFrame,text="Cajero Automatico Bancolombia")
MiLabe.grid(sticky="w",padx=28,pady=10)
MiLabe2=Label(MiFrame,text="Ingrese su contraseña porfavor")
MiLabe2.grid(sticky="w",padx=30,pady=5)
Caja2=Entry(MiFrame,show="*",validate="key",validatecommand=(validatecommand2,"%S"), width=4)
Caja2.grid(sticky="w",padx=100,pady=10)
BotCre=Button(raiz,text="Crear",command=lambda:Metodos.Crear())
BotCre.place(x=10,y=115)
BotSalir=Button(raiz,text="Salir",command=lambda:raiz.destroy())
BotSalir.place(x=180,y=115)
BotonVal=Button(raiz, text="Validar", command= lambda:Metodos.ValCod())
BotonVal.place(x=90,y=115)
#-------------Main------------------------------------------------------
raiz.mainloop()
miConexion2.close()