from Abstract.NodoAST import NodoAST
from Abstract.Instruccion import Instruccion
from TS.Excepcion import Excepcion
from TS.TablaSimbolos import TablaSimbolos


class Case(Instruccion):
    def __init__(self,condicion, instrucciones, fila, columna):
        self.condicion=condicion
        self.instrucciones=instrucciones
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        condicion=self.condicion.interpretar(tree,table)
        if isinstance(condicion,Excepcion): return condicion

    def getInstruccione(self):
        return self.instrucciones

    def getNodo(self):
        nodo = NodoAST("CASE")
        nodo.agregarHijo(str(self.condicion))
        return nodo
