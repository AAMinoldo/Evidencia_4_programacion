import pytest
from impresora import Impresora


@pytest.mark.parametrize("valor, resultado", [
    (0, "Apagado"),
    (1, "Encendido")
   ])
def test_impresora_encendido_apagado(valor, resultado):
    my_impresora = Impresora(valor, "Epson", "Server", "A", "wifi",
                             "medio", 100, "A4")
    assert my_impresora.estado_de_funcionamiento() == resultado


@pytest.mark.parametrize("valor", [2,3,4,5])
def test_excepcion_encendido_apagado(valor):
    with pytest.raises(ValueError, match="Seleccione Uno o Cero"):
        Impresora(valor, "Epson", "Server", tipo="A", conectividad="wifi",
                  nivel_tinta="medio", paginas_impresas=100, papel_tipo="A4").estado_de_funcionamiento()


'''en este caso puntual se parametrizan todos lo atributos, para resaltar una de las distintas formas'''
@pytest.mark.parametrize("estado, marca, modelo,"
                         " tipo, conectividad,"
                         " nivel_tinta, paginas_impresas,"
                         " papel_tipo, resultado_esperado",
                         [
                             (1, "Epson", "Server", "A", "wifi", "Medio", 50, "A4",
                              "Estado: 1 Marca: Epson Modelo: Server"),
                             (2, "HP", "LaserJet", "B", "usb", "Alto", 150, "A4",
                              "Estado: 2 Marca: HP Modelo: LaserJet"),
                             (3, "Canon", "Pixma", "C", "bluetooth", "Vacio", 75, "A5",
                              "Estado: 3 Marca: Canon Modelo: Pixma"),
                             (4, "Canon", "Pixma", "C", "bluetooth", "Vacio", 75, "A5",
                              "Estado: 4 Marca: Canon Modelo: Pixma"),
                         ])
def test_str_metodo(estado, marca, modelo, tipo, conectividad, nivel_tinta, paginas_impresas, papel_tipo,
                    resultado_esperado):
    my_impresora = Impresora(estado, marca, modelo, tipo, conectividad,
                             nivel_tinta, paginas_impresas, papel_tipo)
    resultado = str(my_impresora)
    assert resultado == resultado_esperado


@pytest.mark.parametrize("valor, resultado", [
    (1, "Imprimiendo"),
    (100, "Imprimiendo"),
    (101, "Cargar tinta")
])
def test_imprimir_hojas(valor, resultado):
    my_impresora = Impresora(1, "Epson", "Server", "A", "wifi",
                             "medio", valor, "A4")
    assert my_impresora.imprimir_hojas() == resultado


@pytest.mark.parametrize("valor, resultado", [
    (4, "Completo"),
    (3, "Completo"),
    (2, "Medio"),
    (1, "Bajo"),
    (0, "Vacio")
])
def test_nivel_tinta(valor, resultado):
    my_impresora = Impresora(estado=1, marca="Epson", modelo="Server", tipo="A", conectividad="wifi",
                             nivel_tinta=valor, paginas_impresas=100, papel_tipo="A4")
    assert my_impresora.nivel_de_tinta() == resultado



