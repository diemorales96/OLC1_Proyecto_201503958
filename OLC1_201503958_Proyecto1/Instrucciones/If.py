from Abstract.NodoAST import NodoAST
from Instrucciones.Return import Return
from Abstract.Instruccion import Instruccion
from TS.Excepcion import Excepcion
from TS.Tipo import TIPO
from TS.TablaSimbolos import TablaSimbolos
from Instrucciones.Break import Break


class If(Instruccion):
    def __init__(self, condicion, instruccionesIf, instruccionesElse, ElseIf, fila, columna):
        self.condicion = condicion
        self.instruccionesIf = instruccionesIf
        self.instruccionesElse = instruccionesElse
        self.elseIf = ElseIf
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        condicion = self.condicion.interpretar(tree, table)
        if isinstance(condicion, Excepcion): return condicion

        if self.condicion.tipo == TIPO.BOOLEANO:
            if bool(condicion) == True:  
                nuevaTabla = TablaSimbolos(table,"IF["+str(self.fila)+","+str(self.columna)+"]")    
                for instruccion in self.instruccionesIf:
                    result = instruccion.interpretar(tree, nuevaTabla) 
                    if isinstance(result, Excepcion) :
                        tree.getExcepciones().append(result)
                        tree.updateConsola(result.toString())
                    if isinstance(result, Break): return result
                    if isinstance(result, Return): return result
            else:               
                if self.instruccionesElse != None:
                    nuevaTabla = TablaSimbolos(table,"ELSE["+str(self.fila)+","+str(self.columna)+"]")   
                    for instruccion in self.instruccionesElse:
                        result = instruccion.interpretar(tree, nuevaTabla) 
                        if isinstance(result, Excepcion) :
                            tree.getExcepciones().append(result)
                            tree.updateConsola(result.toString()) 
                        if isinstance(result, Break): return result
                        if isinstance(result, Return): return result
                elif self.elseIf != None:
                    result = self.elseIf.interpretar(tree, table)
                    if isinstance(result, Excepcion): return result
                    if isinstance(result, Break): return result
                    if isinstance(result, Return): return result

        else:
            return Excepcion("Semantico", "Tipo de dato no booleano en IF.", self.fila, self.columna)
    
    def getNodo(self):
        nodo = NodoAST("IF")

        instruccionesIf = NodoAST("INSTRUCCIONES IF")
        for instr in self.instruccionesIf:
            instruccionesIf.agregarHijoNodo(instr.getNodo())
        nodo.agregarHijoNodo(instruccionesIf)

        if self.instruccionesElse != None:
            instruccionesElse = NodoAST("INSTRUCCIONES ELSE")
            for instr in self.instruccionesElse:
                instruccionesElse.agregarHijoNodo(instr.getNodo())
            nodo.agregarHijoNodo(instruccionesElse) 
        elif self.elseIf != None:
            nodo.agregarHijoNodo(self.elseIf.getNodo())

        return nodo    