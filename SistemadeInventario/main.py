from clases import clasesinventario
from funciones import funcionesinventario
from datetime import datetime






def main():

    #diccionario dodne se guardara el inventario de hoy
    productosdisponible = {}

    print("Bienvenido a su inventario diario, donde puede crear un inventario cada dia, detallando el producto,su id y su precio!")
    print()
    print("a continuacion elija una opcion para comenzar la administracion de su inventario")
    print()
    while True:
        print("1.agregar un producto para el inventario")
        print("2.Consultar Inventario de los productos")
        print("3.agregar unidades para un producto")
        print("4.quitar unidades d un producto")
        print("5.ver unidades de un producto")
        print("6.exportar inventario de hoy a excel")
        print("7.Salir del inventario")
        print()
        opcion = input('escriba la opcion elegir: ')
        print()

        if opcion == '1':
        
          verificarexistencia = 'existe'

          contador = 0

          while verificarexistencia == 'existe':

            contador += 1

            if contador >= 2:
                    print('el producto existe ya, porfavor coloque uno nuevo o verifique si ya tiene lo que quiere en su inventario')
                    print()

            print('a continuacion facilite los datos necesarios para crear el producto, los cuales seran nombre , idproducto Y precio')
            print()
            nombre = input('nombre de su producto:')
            numero = input('numero de su producto o id:')
            precio = input('precio que tendra este:')

            nombre = clasesinventario.producto(int(numero),nombre,precio)

            verificarexistencia = funcionesinventario.Listarproducto(nombre,productosdisponible)

          print('producto agregado existosamente !! , recuerde que luego puede agregar la cantidad de unidades que quiere y recomendablemente tenga , tambien puede consultarlas o quitarlas en las opciones relacionadas con unidades en el menu')
          print()
                
        
        elif opcion == '2':
        
            if not productosdisponible:
                print('aun no tiene productos en el inventario, porfavor crear un producto!')
                print()
            else:
                print('aqui estaria su inventario:')
                print()
                for producto in productosdisponible.values():
                    print(producto)
                    print()
                
            

        elif opcion == '3':
        
            print('Bienvenido a la adicion de unidades de un producto. aqui podra agregar la cantidad de unidades que pose de los productos de su inventario')
            print()

            producto = funcionesinventario.agregarUnidadesDeProducto('nombre del producto al la cual quiere agregar unidades:',productosdisponible)

            if producto[0] == 'valido':
                print(f'unidades agregadas a su producto {producto[1].nameproducto}. puede revisar su inventario acontinuacion')
                print()
                
            else:
                print('el producto nombrado no exite en el inventario, debe crearlo primero para poder agregar la cantidad de unidades que tiene o tendra')
                print()
            

        elif opcion == '4':
        
            print('Bienvenido a la resta de unidades de un producto. aqui podra restar la cantidad de unidades que pose de los productos de su inventario')
            print()

            producto = funcionesinventario.restarUnidadesDeProducto('nombre del producto al la cual quiere restar unidades:',productosdisponible)

            if producto[0] == 'valido':
                print(f'unidades restadas a su producto {producto[1].nameproducto}. puede revisar su inventario acontinuacion')
                print()
                
            else:
                print('el producto nombrado no exite en el inventario, debe crearlo primero para poder restar la cantidad de unidades que quiere')
                print()
        

        elif opcion == '5':
        
            print('a continuacion le mostraremos las unidades disponible que pose su producto seleccioando:')
            print()

            producto = funcionesinventario.mostrarUnidadesDeProducto('nombre del producto a la cual quiere consultar sus unidades:',productosdisponible)

            if producto == 'invalido':
                print('producto invalido o inexistente porfavor verifique su inventario')
                print()

            else:
                print(f'tiene {producto[1].unidades} unidades de {producto[1].nameproducto}')
                print()
                print('recuerde que puede ver cada unidades disponible de sus productos aqui individualmente o consultar el inventario para ver todo en general eligiendo opcion 2')
                print()
            
        elif opcion == '6':
        
            print('bienvenido a su exportador, inventario de hoy a excel, esto es para cuando ya tenga todo listo organizado y definido, tanto productos como unidades de cada producto')
            print()
            print('a continuacion se le creara el excel con el inventario de hoy. si le falto algo debera vovler a crear todo y setearlo y luego marcar esta opcion nuevamente')
            print()

            titulo = 'Inventario de Hoy → '
            fechadehoy = datetime.now().strftime("%d-%m-%Y")
            funcionesinventario.crearExcel(titulo,fechadehoy,productosdisponible)
        

        elif opcion == '7':
            print('hasta luego! gracias por usar el creador de inventarios diario')
            print()
            print('esperamos que haya sido util esta herramienta y que haya creado su inventario de hoy correctamente !!')
            print()
            exit();
        
        else:
            print('opcion invalida o inexsistente !')
            print()
            continue


        
        



    
if __name__ == "__main__":
     main()

