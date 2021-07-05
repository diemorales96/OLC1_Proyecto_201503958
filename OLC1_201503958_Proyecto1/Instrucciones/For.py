from Abstract.NodoAST import NodoAST
from Instrucciones.Return import Return
from Instrucciones.Asignacion import Asignacion
from Instrucciones.Declaracion import Declaracion
from Abstract.Instruccion import Instruccion
from TS.Excepcion import Excepcion
from TS.Tipo import TIPO
from TS.TablaSimbolos import TablaSimbolos
from Instrucciones.Break import Break

class For(Instruccion):
    def __init__(self, declaraciones, condicion, incremento, instrucciones, fila, columna):
        self.declaraciones = declaraciones
        self.condicion = condicion
        self.incremento = incremento
        self.instrucciones = instrucciones
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        nTabla = TablaSimbolos(table,"FOR["+str(self.fila)+","+str(self.columna)+"]") 
        declaracion = self.declaraciones.interpretar(tree,nTabla)
        if isinstance(declaracion,Declaracion): return None
        if isinstance(declaracion,Asignacion): return None

        while True:
            condicion = self.condicion.interpretar(tree, nTabla)
            if isinstance(condicion, Excepcion): return condicion

            if self.condicion.tipo == TIPO.BOOLEANO:
                if bool(condicion) == True:   
                    nuevaTabla = TablaSimbolos(nTabla,"FOR["+str(self.fila)+","+str(self.columna)+"]")      
                    for instruccion in self.instrucciones:
                        result = instruccion.interpretar(tree, nuevaTabla)
                        if isinstance(result, Excepcion) :
                            tree.getExcepciones().append(result)
                            tree.updateConsola(result.toString())
                        if isinstance(result, Break): return None
                        if isinstance(result, Return): return result
                    self.incremento.interpretar(tree,nTabla)
                else:
                    break
            else:
                return Excepcion("Semantico", "Tipo de dato no booleano en IF.", self.fila, self.columna)

    def getNodo(self):
        nodo = NodoAST("FOR")
        
        instrucciones = NodoAST("INSTRUCCIONES")
        for instr in self.instrucciones:
            instrucciones.agregarHijoNodo(instr.getNodo())
        nodo.agregarHijoNodo(instrucciones)
        return nodo

        
             