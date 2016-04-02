import tkFileDialog
from procesos_lista import Procesos
per=[]
sn=""
op=0
proc=Procesos("",0,"")
print(proc)
while 1:
    proc.imprimir(per)
    proc.menu()
    op=input("Opcion: ")
    if op==1:
        while (sn!="n"):
            print ("\nIngresa los datos para  crear   una nueva persona:\n") 
            nom=raw_input("Nombre: " )
            ed=input("Edad: ")
            ciu=raw_input("Ciudad: ")
            pers=Procesos(nom,ed,ciu)
            per.append(pers)
            sn=raw_input("deseas agregar otra persona? s/n :")
        sn=""
    elif op==2:
        per=proc.borrarelemento(per)
    elif op==3:
        per=proc.orden_nombre(per)
    elif op==4:
        per=proc.orden_edad(per)
    elif op==5:
        per=proc.orden_ciudad(per)
    elif op==6:
        proc.imprimir(per)
        per=proc.modificar(per)
    elif op==7:
        proc.buscar(per)
    elif op==8:
        proc.guardar(per)
    elif op==9:
        per=proc.importar(per)
    else:
        print("opcion invalida")
        
    


 
