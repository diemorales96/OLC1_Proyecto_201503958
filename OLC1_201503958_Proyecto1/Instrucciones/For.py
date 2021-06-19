from Instrucciones.Asignacion import Asignacion
from Instrucciones.Declaracion import Declaracion
from Abstract.Instruccion import Instruccion
from TS.Excepcion import Excepcion
from TS.Tipo import TIPO
from TS.TablaSimbolos import TablaSimbolos
from Instrucciones.Break import Break
from TS.Simbolo import Simbolo
from Instrucciones.Incremento import Incremento

class For(Instruccion):
    def __init__(self, declaraciones, condicion, incremento, instrucciones, fila, columna):
        self.declaraciones = declaraciones
        self.condicion = condicion
        self.incremento = incremento
        self.instrucciones = instrucciones
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        
        declaracion = self.declaraciones.interpretar(tree,table)
        if isinstance(declaracion,Declaracion): return None
        if isinstance(declaracion,Asignacion): return None

        while True:
            condicion = self.condicion.interpretar(tree, table)
            if isinstance(condicion, Excepcion): return condicion

            if self.condicion.tipo == TIPO.BOOLEANO:
                if bool(condicion) == True:   # VERIFICA SI ES VERDADERA LA CONDICION
                    nuevaTabla = TablaSimbolos(table)       #NUEVO ENTORNO
                    for instruccion in self.instrucciones:
                        result = instruccion.interpretar(tree, nuevaTabla) #EJECUTA INSTRUCCION ADENTRO DEL IF
                        if isinstance(result, Excepcion) :
                            tree.getExcepciones().append(result)
                            tree.updateConsola(result.toString())
                        if isinstance(result, Break): return None
                    self.incremento.interpretar(tree,table)
                else:
                    break
            else:
                return Excepcion("Semantico", "Tipo de dato no booleano en IF.", self.fila, self.columna)
        
             