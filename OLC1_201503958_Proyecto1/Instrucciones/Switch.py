from Abstract.Instruccion import Instruccion
from TS.Excepcion import Excepcion
from TS.Tipo import TIPO
from TS.TablaSimbolos import TablaSimbolos
from Instrucciones.Break import Break


class Switch(Instruccion):
    def __init__(self, expresion, case_list,def_instrucciones,fila,columna):
        self.expresion = expresion
        self.case_list = case_list
        self.def_instrucciones = def_instrucciones
        self.fila = fila
        self.columna = columna
    
    def interpretar(self, tree, table):
        val_expresion = self.expresion.interpretar(tree,table)
        if isinstance(val_expresion,Excepcion): return None