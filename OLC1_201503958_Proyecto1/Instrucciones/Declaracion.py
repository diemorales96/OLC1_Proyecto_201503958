from Abstract.NodoAST import NodoAST
from TS.Excepcion import Excepcion
from Abstract.Instruccion import Instruccion
from TS.Simbolo import Simbolo


class Declaracion(Instruccion):
    def __init__(self, identificador, fila, columna, expresion=None):
        self.identificador = identificador
        self.expresion = expresion
        self.fila = fila
        self.columna = columna
        self.arreglo = False

    def interpretar(self, tree, table):
        value = self.expresion.interpretar(tree, table) 
        if isinstance(value, Excepcion): return value

        simbolo = Simbolo(str(self.identificador), self.expresion.tipo,self.arreglo, self.fila, self.columna, value)

        result = table.setTabla(simbolo)

        if isinstance(result, Excepcion): return result
        return None

    def getNodo(self):
        nodo = NodoAST("DECLARACION")
        nodo.agregarHijo(str(self.identificador))
        nodo.agregarHijoNodo(self.expresion.getNodo())
        return nodo