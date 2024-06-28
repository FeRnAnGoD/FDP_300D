import csv, os, time

def lista_productos(n):
    for i in productos:
            n += 1
            print({n},i,'al precio de',productos[i],'pesos')

def recibo(n):
    d = 0
    print('-------------------------------------------------')
    print('-----T I E N D A---G R E E N--- G A R D E N -----')
    print('-------------------------------------------------')
    print('--Número boleta: ',numero_boleta)
    print('--Nombre: ',boleta['nombre'][c])
    print('--Dirección: ',boleta['direccion'][c])
    print('--Teléfono: ',boleta['telefono'][c])
    print('--Producto/s:')
    for i in boleta.get('producto')[c]:
        print('--',boleta['cantidad'][c][d],'unidades de',boleta['producto'][c][d],'a un valor de $',boleta['total'][c][d])
        d += 1
    d = 0
    print('--Total a pagar: ',pago)
    print('-------------------------------------------------')

productos = {
    'abono':1200,
    'tierra':1000,
    'lirio':1100,
    'rosas_rojas':1700,
    'margaritas':1100
}
boleta = {
    'nombre':[],
    'direccion':[],
    'telefono':[],
    'producto':[],
    'cantidad':[],
    'total':[],
    'pago_total':[],
    'id_boleta':[]
}
a = 0
b = 0
c = 0
d = 0
n = 0
pago = 0
numero_boleta = 1
print('¡¡ Bienvenido al sistema de ventas de JAL TEC. !!')
while a == 0:
    nom = input('Ingrese su nombre (si es una empresa escriba el nombre de la misma): ')
    boleta['nombre'].append(nom)
    while nom == '':
        boleta['nombre'].remove('')
        nom = input('Ingrese un nombre válido porfavor: ')
        boleta['nombre'].append(nom)
    vivienda = input('Ingrese su dirección: ')
    boleta['direccion'].append(vivienda)
    while vivienda == '':
        boleta['direccion'].remove('')
        vivienda = input('Ingrese un nombre válido porfavor: ')
        boleta['direccion'].append(vivienda)
    celular = input('Ingrese su número de teléfono: ')
    boleta['telefono'].append(celular)
    while celular == '':
        boleta['telefono'].remove('')
        celular = input('Ingrese un nombre válido porfavor: ')
        boleta['telefono'].append(celular)
    time.sleep(2)
    os.system('cls')
    print('La lista de productos es la siguiente:')
    boleta['producto'].append([])
    boleta['total'].append([])
    boleta['cantidad'].append([])
    boleta['pago_total'].append([])
    boleta['id_boleta'].append(numero_boleta)
    while b == 0:
        lista_productos(n)
        n = 0  
        op = int(input('Elija un producto (ingrese el número del producto): '))
        if op == 1:
            boleta['producto'][c].append('abono')
            seleccion = 'abono'
        elif op == 2:
            boleta['producto'][c].append('tierra')
            seleccion = 'tierra'
        elif op == 3:
            boleta['producto'][c].append('lirio') 
            seleccion = 'lirio' 
        elif op == 4:
            boleta['producto'][c].append('rosas_rojas')    
            seleccion = 'rosas_rojas'
        elif op == 5:
            boleta['producto'][c].append('margaritas')
            seleccion = 'margaritas'
        cant = int(input('Ingrese la cantidad del producto deseada: '))
        boleta['cantidad'][c].append(cant)
        total_cant = cant*productos[seleccion]
        boleta['total'][c].append(total_cant)
        pago = pago + total_cant
        boleta['pago_total'][c].append(pago)
        time.sleep(2)
        os.system('cls')
        dc = input('¿Desea comprar más productos? (Si/No): ')  
        if dc == 'No' or dc == 'NO' or dc == 'nO' or dc == 'no':
            print('Finalizando compra...')
            break
        else:
            print('Redireccionando a la lista de productos...')
    recibo(n)
    c += 1
    numero_boleta += 1
    pago = 0
    
    salir = str(input('¿Desea seguir comprando? (Como otro cliente) (Si/No): '))
    if salir == 'No' or salir == 'NO' or salir == 'nO' or salir == 'no':
        print('Saliendo del programa...')
        break
    
with open('Reporte_GreenGarden.csv', mode = 'w') as miCsv:
    escribirCsv = csv.writer(miCsv)
    for i in boleta:
        escribirCsv.writerows([[i+':']]), escribirCsv.writerows([boleta[i]])