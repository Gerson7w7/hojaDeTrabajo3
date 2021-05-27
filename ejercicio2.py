#La ruta es de mi escritorio, para que funcione tiene que tener la ruta su escritorio, gracias!

print("Tablas de multiplicar \n Introduzca un número entre 1 y 10: ")
n = int(input())

def archivo(n): 
    if n >= 1 & n <= 10:
        ruta = 'C:\\Users\\gerso\\Desktop\\Tabla-' + str(n) + '.txt'
        archivo = open(ruta, 'a')
        archivo.write(f"Tabla del número {n} \n")
        for i in range(10):
            archivo.write(f"{i+1}x{n} = {(i+1)*n} \n")    
        print("Archivo creado con éxito!")
        archivo.close()
    else: 
        print("Número fuera de rango.")

archivo(n)