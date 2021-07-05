from TS.Excepcion import Excepcion
from TS.Tipo import TIPO
from Instrucciones.Funcion import Funcion


class Length(Funcion):
    def __init__(self, nombre, parametros, instrucciones, fila, columna):
        self.nombre = nombre.lower()
        self.parametros = parametros
        self.instrucciones = instrucciones
        self.fila = fila
        self.columna = columna
        self.tipo = TIPO.NULO
    
    def interpretar(self, tree, table):
        simbolo = table.getTabla("length##param1")
        if simbolo == None : return Excepcion("Semantico", "No se encontró el parámetro de Length", self.fila, self.columna)

        if simbolo.getTipo() == TIPO.CADENA :
            return len(simbolo.getValor())
        elif simbolo.arreglo == False or simbolo.getTipo()==TIPO.CADENA:
            self.tipo=TIPO.ENTERO
            return len(simbolo.getValor())
        return Excepcion("Semantico", "Tipo de parametro de Length No coincide.", self.fila, self.columna)