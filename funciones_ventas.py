#funciones

ventas=[]

def registrar_nueva_venta():
    nombre_producto=input("ingrese nombre del producto:")
    cantidad= int(input("ingrese cantidad del producto: "))
    valor_unitario=int (input("ingrese el valor del producto: "))
    forma_pago=input("ingrese una forma de pago: ")
    
    datos_ventas=[nombre_producto, cantidad, valor_unitario, forma_pago]
    ventas.append(datos_ventas)
    precio_total=cantidad*valor_unitario
    
    print("Su total es:",precio_total)
    
    
    
def Reporte_de_ventas():
    if len(ventas) == 0:
        print("no se añadió ninguna venta")
    else:
        print("ventas agregadas ")
        for lulo in ventas:
            print(f"NOMBRE: {lulo[0]}\nCANTIDAD: {lulo[1]}\nVALOR: {lulo[2]}\nFORMA DE PAGO: {lulo[3]} ")
       
        



def Reporte_de_ventas_p():
    if len(ventas) == 0:
        print("no se añadió ninguna venta")
    else:
        print("ventas agregadas ")
        for lulo in ventas:
            print(f"NOMBRE: \n{lulo[0]} CANTIDAD:\n {lulo[1]} VALOR: \n{lulo[2]} ")
       
   

def reporte_formas_pago():
    pass

def salir():
    pass