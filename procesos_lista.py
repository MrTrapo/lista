import tkFileDialog
from objetos_personas import Persona
class Procesos(Persona):
    def __init__(self,nom,ed,ciu):
        Persona.__init__(self,nom,ed,ciu)
        
    def orden_nombre(self,cadena):
            for i in range (len(cadena)):       
                for j in range (0,len(cadena)):                                  
                    if cadena[i].nombre.lower()<=cadena[j].nombre.lower():
                        aux=cadena[j]
                        cadena[j]=cadena[i]
                        cadena[i]=aux
            return cadena
        
    def orden_edad(self,cadena):
            for i in range (len(cadena)):       
                for j in range (0,len(cadena)):                                  
                    if cadena[i].edad<=cadena[j].edad:
                        aux=cadena[j]
                        cadena[j]=cadena[i]
                        cadena[i]=aux
            return cadena 

    def orden_ciudad(self,cadena):
            for i in range (len(cadena)):       
                for j in range (0,len(cadena)):                                  
                    if cadena[i].ciudad.lower()<=cadena[j].ciudad.lower():
                        aux=cadena[j]
                        cadena[j]=cadena[i]
                        cadena[i]=aux
            return cadena 

    def menu(self):
        print('''\n\tMenu:
        1.agrgar persona
        2.borrar persona
        3.ordenar por nombre
        4.ordenar por edad
        5.ordenar por ciudad
        6.modificar datos
        7.buscar persona
        8.guardar
        9.importar lista desde  archivo''')

    def borrarelemento(self,cadena):
            numero=input("ingresa el numero (comenzando de 1) del elemento que deseas borrar: ")
            if numero<1 or numero>len(cadena):
                print("\n\tno existe ese elemento en el arreglo\n")
            else:
                cadena.pop(numero-1)
            return cadena
        
    def imprimir(self,per):
        if len(per)==0:
            print("\nlista vacia")
        else:
            print("\nlos elementos  en la  lista  son:")
            for i in range(len(per)):
                print("{}. {} - {} - {}".format((i+1),per[i].nombre,per[i].edad,per[i].ciudad))
            print("\n")

    def modificar(self,per):
            numero=input("\nIngresa el numero (comenzando de 1) del elemento que deseas modificar: ")
            if numero<1 or numero>len(per):
                print("\n\tno existe ese elemento en el arreglo\n")
            else:
                op=input("\nDesea modificar a {}\n1.Nobre\t2.Edad\t3.Ciudad ?\ningrese el numero de la opcion:".format(per[numero-1].nombre))
            if op<1 and op>3:
                print("\n\tno existe esa opcion\n")
            else:
                print ("\nIngresa los datos para  modificar a {}:\n".format(per[numero-1].nombre))
                if op==1:
                    per[numero-1].nombre=raw_input("Nombre: " )
                if op==2:
                    per[numero-1].edad=input("Edad: ")
                if op==3:
                    per[numero-1].ciudad=raw_input("Ciudad: ")
            return per

    def buscar(self,per):
        listab=[]
        palabra=raw_input("\nPersona que se desea buscar: ")
        for i in range(len(per)):
            if palabra.lower() in per[i].nombre.lower():
                listab.append(per[i])
        print("\nlos elementos  encontrados  son:")
        for i in range(len(listab)):
            print("{} - {} - {}".format(listab[i].nombre,listab[i].edad,listab[i].ciudad))
        print("\n")
        
    def guardar(self,per):
        nuevo=tkFileDialog.asksaveasfilename()
        f=open(nuevo,"w")
        for i in range(len(per)):
            f.write("{},{},{}\n".format(per[i].nombre,per[i].edad,per[i].ciudad))
        f.close()
        
    def importar(self,per):
        cadena=[]
        datos=tkFileDialog.askopenfilename()
        f=open(datos,'r')
        f.readline()
        for i in f.readlines():
                cadena=i[:-1].split(",")
                pers=Procesos(cadena[0],cadena[1],cadena[2])
                per.append(pers)
        f.close()
        return per
        
        
