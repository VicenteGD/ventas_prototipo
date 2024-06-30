#ejercicio ventas
import os, csv, time
from funciones_ventas import*
os.system("cls")

while True:
    os.system("cls")
    
    print("""\tMENÚ DE VENTAS
        1). Registrar nueva venta
        2). Reporte de ventas hostórico
        3). Reporte de ventas por producto
        4). Reporte de formas de pago
        5). salir""")

    opc = int(input("ingresa una opción (1,2,3,4): "))
    os.system("cls")
    
    if opc==1:
        registrar_nueva_venta()
    elif opc==2:
        Reporte_de_ventas()
    elif opc==3:
        Reporte_de_ventas_p()
    elif opc==4:
        reporte_formas_pago()
    else: 
        salir()
        
    time.sleep(3)
    
         
        
