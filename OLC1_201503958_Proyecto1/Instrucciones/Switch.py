from Abstract.NodoAST import NodoAST
from Abstract.Instruccion import Instruccion
from TS.Excepcion import Excepcion
from TS.TablaSimbolos import TablaSimbolos
from Instrucciones.Break import Break
from Instrucciones.Return import Return


class Switch(Instruccion):
    def __init__(self, condicionSwitch, bloqueCases,default,fila,columna):
        self.condicionSwitch=condicionSwitch
        self.bloqueCases=bloqueCases
        self.default=default
        self.fila=fila
        self.columna=columna

    def interpretar(self, tree, table):
        condicionSwitch = self.condicionSwitch.interpretar(tree, table)
        if isinstance(condicionSwitch, Excepcion): return condicionSwitch


        if self.bloqueCases!=None:
            for instruccion in self.bloqueCases:
                condicionCase = instruccion.condicion.interpretar(tree, table)
                if condicionCase == condicionSwitch:
                    for instrucase in instruccion.instrucciones:
                        result = instrucase.interpretar(tree, table)
                        if isinstance(result, Excepcion):
                            tree.getExcepciones().append(result)
                            tree.updateConsola(result.toString())
                        if isinstance(result, Break): return None
                        if isinstance(result, Return): return result
        if self.default!=None:
            for instrudefault in self.default:
                result = instrudefault.interpretar(tree, table)
                if isinstance(result, Excepcion):
                    tree.getExcepciones().append(result)
                    tree.updateConsola(result.toString())
                    return None

    def getNodo(self):
        nodo = NodoAST("SWITCH")
        instruccionesSwitch = NodoAST("INSTRUCCIONES SWITCH")
        for instr in self.bloqueCases:
            for inst2 in instr.instrucciones:
                instruccionesSwitch.agregarHijoNodo(inst2.getNodo())
                nodo.agregarHijoNodo(instruccionesSwitch)
        return nodo

    def verificarBool(self,valor):
        if valor=='true':
            return True
        elif valor=='false':
            return False
        else:
            return bool(valor)