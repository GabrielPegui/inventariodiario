class producto:
    def __init__(self,iddeproducto,nameproducto,precio):
        self.iddeproducto = iddeproducto
        self.nameproducto = nameproducto
        self.unidades = 0
        self.precio = precio

    def __str__(self):
        return f'producto {self.nameproducto} con el numero de id: {self.iddeproducto}, tiene un precio de : {self.precio}.  Cuenta con {self.unidades} unidades de este producto para venta o utilidad'



    def agregarunidades(self,cantidaddeunidades):
        nuevaCunidades = self.unidades + cantidaddeunidades
        self.unidades = nuevaCunidades

    def restarunidades(self,cantidaddeunidades):
        nuevaCunidades = self.unidades - cantidaddeunidades
        if nuevaCunidades <= 0:
            self.unidades = 0
        else:
         self.unidades = nuevaCunidades