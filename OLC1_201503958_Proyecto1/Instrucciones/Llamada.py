from TS.Simbolo import Simbolo
from Instrucciones.Funcion import Funcion
from Abstract.Instruccion import Instruccion
from TS.Excepcion import Excepcion
from TS.TablaSimbolos import TablaSimbolos
from Instrucciones.Break import Break


class Llamada(Instruccion):
    def __init__(self, nombre, parametros, fila, columna):
        self.nombre = nombre
        self.parametros = parametros
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        result = tree.getFuncion(self.nombre.lower()) 
        if result == None: 
            return Excepcion("Semantico", "NO SE ENCONTRO LA FUNCION: " + self.nombre, self.fila, self.columna)
        
        nuevaTabla = TablaSimbolos(tree.getTSGlobal())
        if len(result.parametros) == len(self.parametros): 
           contador=0
           for expresion in self.parametros: 
                resultExpresion = expresion.interpretar(tree, table)
                if isinstance(resultExpresion, Excepcion): return resultExpresion
                if result.parametros[contador]["identificador"].lower() == "Length##Param1":
                    result.parametros[contador]["tipo"] = expresion.tipo
                if result.parametros[contador]["tipo"] == expresion.tipo: 
                    
                    simbolo = Simbolo(str(result.parametros[contador]['identificador']).lower(), result.parametros[contador]['tipo'], self.fila, self.columna, resultExpresion)
                    resultTabla = nuevaTabla.setTabla(simbolo)
                    if isinstance(resultTabla, Excepcion): return resultTabla
                else:
                    return Excepcion("Semantico", "Tipo de dato diferente en Parametros de la llamada.", self.fila, self.columna)
                contador += 1 
        else: 
            return Excepcion("Semantico", "Cantidad de Parametros incorrecta.", self.fila, self.columna)
        value = result.interpretar(tree, nuevaTabla)   
        if isinstance(value, Excepcion): return value
        self.tipo = result.tipo
        return value