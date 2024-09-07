class Impresora:
    def __init__(self, estado, marca, modelo, tipo, conectividad, nivel_tinta, paginas_impresas, papel_tipo):
        self.__estado = estado
        self.__marca = marca
        self.__modelo = modelo
        self.__tipo = tipo
        self.__conectividad = conectividad
        self.__nivel_tinta = nivel_tinta
        self.__paginas_impresas = paginas_impresas
        self.__papel_tipo = papel_tipo

    def get_estado(self):
        return self.__estado

    def set_estado(self, estado):
        self.__estado = estado

    def get_paginas_impresas(self):
        return self.__paginas_impresas

    def set_paginas_impresas(self, paginas_impresas):
        self.__paginas_impresas = paginas_impresas

    def get_nivel_tinta(self):
        return self.__nivel_tinta

    def set_nivel_tinta(self, nivel_tinta):
        self.__nivel_tinta = nivel_tinta

    def estado_de_funcionamiento(self):
        if self.__estado == 1:
            return "Encendido"
        elif self.__estado == 0:
            return "Apagado"
        else:
            raise ValueError("Seleccione Uno o Cero")

    def __str__(self):
        return f"Estado: {self.__estado} Marca: {self.__marca} Modelo: {self.__modelo}"

    def imprimir_hojas(self):
        if self.__paginas_impresas <= 100:
            return "Imprimiendo"
        else:
            return "Cargar tinta"

    def nivel_de_tinta(self):
        if self.__nivel_tinta == 0:
            return "Vacio"
        if self.__nivel_tinta == 1:
            return "Bajo"
        if self.__nivel_tinta == 2:
            return "Medio"
        else:
            return "Completo"




if __name__ == "__main__":
    mi_impresora = Impresora(estado=0, marca="Epson", modelo="Server", tipo="A", conectividad="wifi",
                             nivel_tinta="medio", paginas_impresas=100, papel_tipo="A4")

    mi_impresora.set_estado(int(input("ingresa una valor: ")))

    print(f"Estado de la impresora: {mi_impresora.estado_de_funcionamiento()}")


    mi_impresora.get_estado()
    mi_impresora.set_estado(100)
