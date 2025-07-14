
productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
             '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
             'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
             'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
             'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
             '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
             '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
             'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']}

stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
        'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
        'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0]}


# una tienda online llamada pybook se ha especializado en la venta de notebooks . la informacion de cada modelo de notebook esta registrada en un diccionario llamado "productos" donde las llaves son los modelos
#y los valores asiociados a las llaves son listas que contiene informacion asociada a cada modelo , los putnos suspensivos indican que pueden existir muchos mas datos
 # pybooks le solicita las siguientes opciones:
# 1- stock marca
# 2- busqueda por precio 
# 3- actualizar precio
# 4- salir 

#la opcion 1 de stock marca debe entregar el stock de una marca particular ingresada por teclado , la marca ingresada puede estar escrita en mayuscula o en minuscula y debe funcionar de igual manera . debe estar implementada en una funcion llamada stock_marca(marca) que recibe como parametro la marca y no debe retornar nada 

# la opcion 2 (busqueda por precio) debe entregar una lista de strings de todos los modelos que estan dentro de un rango de precios ingresados por teclado y que tengan stock distinto (stock distinto de cero) la lista debe tener el nombre de la marca junto al modelo con el formato "marca-- modelo". estos nombres deben estar ordenados alfabeticamente.
# al momento de ingresar el rango de precios deben ser valores enteros si no se cumple , el programa debe mostrar el mensaje "debe ingresar valores enteros!! y volver a preguntar por el rango de valores , en esta situacion el usuario debe poder ingresar cualquier tipo de dato. por ultimo si no se encuentra ningun notebook dentro del rango de precios 
# el programa debe mostrar el mensaje " no hay notebooks en ese rango de precios "  debe estar implementada mediante la funcion llamada busqueda_precio (p_min , p_max ) que reciba el precio minimo y el precio maximo como parametro y no debe retornar nada

# la opcion 3 ( actualizar precio) debe actualizar el precio de un modelo en particular en el diccionario stock , debe estar implementado mediante una funcion llamada actualizar_precio(modelo ,p) que reciba como parametro un modelo y el precio nuevo, si el modelo ingresado no existe la funcion debe retornar "False" y si el modelo existe entonces la funcion debe retornar "True". 
#el codigo principal main debe recibir el valor de retorno y mostrar los mensajes "precio actualizado!!" si se puedo realizar la actualizacion y el modelo no existe
#si no se pudo. finalmente el programa debe preguntar si desea actualizar otro precio de notebook si la respuesta es "si" , el proceso comienza nuevamente , si la respuesta es "no" entonces el prgrama vuelve al menu principal

# la opcion 4(salir) , debe terminar el programa mostrando por pantalla el mensaje: " programa finalizado "

#estando en el menu principal , si se ingresa cualquier otro valor como opcion , entonces el programa debe mostrar el mensaje : "debe seleccionar una opcion valida!!" y volver a preguntar.



def stock_marca(marca):
    marca = marca.lower()
    encontrados = False
    for modelo, datos in productos.items():
        if datos[0].lower() == marca:
            encontrados = True
            if modelo in stock:
                print(f"Modelo: {modelo} - Stock: {stock[modelo][1]}")
            else:
                print(f"Modelo: {modelo} - Stock: No disponible")
    if not encontrados:
        print("No hay productos de esa marca.")

def busqueda_precio(p_min, p_max):
    resultados = []
    for modelo, info in stock.items():
        precio, cantidad = info
        if p_min <= precio <= p_max and cantidad > 0:
            if modelo in productos:
                marca = productos[modelo][0]
                resultados.append(f"{marca}--{modelo}")
    if resultados:
        resultados.sort()
        for item in resultados:
            print(item)
    else:
        print("no hay notebooks en ese rango de precios")

def actualizar_precio(modelo, p):
    if modelo in stock:
        stock[modelo][0] = p
        return True
    return False

def main():
    while True:
        print("\n--- PyBook: Tienda Online de Notebooks ---")
        print("1 - Stock por marca")
        print("2 - Búsqueda por precio")
        print("3 - Actualizar precio")
        print("4 - Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            marca = input("Ingrese la marca: ")
            stock_marca(marca)

        elif opcion == '2':
            while True:
                try:
                    p_min = int(input("Ingrese precio mínimo: "))
                    p_max = int(input("Ingrese precio máximo: "))
                    break
                except ValueError:
                    print("debe ingresar valores enteros!!")
            busqueda_precio(p_min, p_max)

        elif opcion == '3':
            while True:
                modelo = input("Ingrese modelo a actualizar: ")
                try:
                    nuevo_precio = int(input("Ingrese nuevo precio: "))
                except ValueError:
                    print("debe ingresar un precio válido!!")
                    continue

                resultado = actualizar_precio(modelo, nuevo_precio)
                if resultado:
                    print("precio actualizado!!")
                else:
                    print("modelo no existe")

                seguir = input("¿Desea actualizar otro precio de notebook? (si/no): ").strip().lower()
                if seguir != "si":
                    break

        elif opcion == '4':
            print("programa finalizado")
            break

        else:
            print("debe seleccionar una opcion valida!!")

if __name__ == "__main__":
    main()




  
      
