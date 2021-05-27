frutas = {"Plátano":1.35, "Manzana":0.80, "Pera":0.85, "Naranja":0.70}

print("¿Qué fruta desea comprar?")
fruta = input()

if fruta in frutas: 
    print("¿Cuántos kilos desea comprar?")
    kilos = float(input())
    precio = frutas[fruta]*kilos
    print(f"Producto: {fruta} \nKilos: {kilos} \nPrecio total: {precio}")
else: 
    print(f"La fruta: {fruta} no está disponible")
