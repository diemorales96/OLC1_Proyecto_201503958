from Abstract.NodoAST import NodoAST
from Abstract.Instruccion import Instruccion
from TS.Excepcion import Excepcion
from TS.Tipo import TIPO, OperadorRelacional

class Relacional(Instruccion):
    def __init__(self, operador, OperacionIzq, OperacionDer, fila, columna):
        self.operador = operador
        self.OperacionIzq = OperacionIzq
        self.OperacionDer = OperacionDer
        self.fila = fila
        self.columna = columna
        self.tipo = TIPO.BOOLEANO

    
    def interpretar(self, tree, table):
        izq = self.OperacionIzq.interpretar(tree, table)
        if isinstance(izq, Excepcion): return izq
        der = self.OperacionDer.interpretar(tree, table)
        if isinstance(der, Excepcion): return der
        
 #---------------------------------------------------------MENORQUE--------------------------------------------
        if self.operador == OperadorRelacional.MENORQUE:
            if self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.ENTERO:
                return self.obtenerVal(self.OperacionIzq.tipo, izq) < self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.DECIMAL:
                return self.obtenerVal(self.OperacionIzq.tipo, izq) < self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.ENTERO:
                return self.obtenerVal(self.OperacionIzq.tipo, izq) < self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.DECIMAL:
                return self.obtenerVal(self.OperacionIzq.tipo, izq) < self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.BOOLEANO and self.OperacionDer.tipo == TIPO.BOOLEANO:
                return self.obtenerVal(self.OperacionIzq.tipo, izq) < self.obtenerVal(self.OperacionDer.tipo, der)
            elif (self.OperacionIzq.tipo == TIPO.NULO and self.OperacionDer.tipo != TIPO.NULO)or(self.OperacionIzq.tipo != TIPO.NULO and self.OperacionDer.tipo == TIPO.NULO)or(self.OperacionIzq.tipo == TIPO.NULO and self.OperacionDer.tipo == TIPO.NULO):
                return Excepcion("Semantico", "Null pointer para expresion <.", self.fila, self.columna)
            return Excepcion("Semantico", "Tipo Erroneo de operacion para <.", self.fila, self.columna)
 #---------------------------------------------------------MAYORQUE--------------------------------------------
        elif self.operador == OperadorRelacional.MAYORQUE:
            if self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.ENTERO:
                return self.obtenerVal(self.OperacionIzq.tipo, izq) > self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.DECIMAL:
                return self.obtenerVal(self.OperacionIzq.tipo, izq) > self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.ENTERO:
                return self.obtenerVal(self.OperacionIzq.tipo, izq) > self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.DECIMAL:
                return self.obtenerVal(self.OperacionIzq.tipo, izq) > self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.BOOLEANO and self.OperacionDer.tipo == TIPO.BOOLEANO:
                return self.obtenerVal(self.OperacionIzq.tipo, izq) > self.obtenerVal(self.OperacionDer.tipo, der)
            elif (self.OperacionIzq.tipo == TIPO.NULO and self.OperacionDer.tipo != TIPO.NULO)or(self.OperacionIzq.tipo != TIPO.NULO and self.OperacionDer.tipo == TIPO.NULO)or(self.OperacionIzq.tipo == TIPO.NULO and self.OperacionDer.tipo == TIPO.NULO):
                return Excepcion("Semantico", "Null pointer para expresion >.", self.fila, self.columna)
            return Excepcion("Semantico", "Tipo Erroneo de operacion para >.", self.fila, self.columna)
 #---------------------------------------------------------IGUAL IGUAL--------------------------------------------
        elif self.operador == OperadorRelacional.IGUALIGUAL:
            if self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.ENTERO:
                return self.obtenerVal(self.OperacionIzq.tipo, izq) == self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.DECIMAL:
                return self.obtenerVal(self.OperacionIzq.tipo, izq) == self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.ENTERO:
                return self.obtenerVal(self.OperacionIzq.tipo, izq) == self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.DECIMAL:
                return self.obtenerVal(self.OperacionIzq.tipo, izq) == self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.BOOLEANO and self.OperacionDer.tipo == TIPO.BOOLEANO:
                return self.obtenerVal(self.OperacionIzq.tipo, izq) == self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.CHARACTER and self.OperacionDer.tipo == TIPO.CHARACTER:
                return self.obtenerVal(self.OperacionIzq.tipo, izq) == self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.CADENA and self.OperacionDer.tipo == TIPO.ENTERO:
                return self.obtenerVal(self.OperacionIzq.tipo, izq) == str(self.obtenerVal(self.OperacionDer.tipo, der))
            elif self.OperacionIzq.tipo == TIPO.CADENA and self.OperacionDer.tipo == TIPO.DECIMAL:
                return self.obtenerVal(self.OperacionIzq.tipo, izq) == self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.CADENA and self.OperacionDer.tipo == TIPO.BOOLEANO:
                return self.obtenerVal(self.OperacionIzq.tipo, izq) == str(self.obtenerVal(self.OperacionDer.tipo, der)).lower()
            elif self.OperacionIzq.tipo == TIPO.CADENA and self.OperacionDer.tipo == TIPO.CADENA:
                return self.obtenerVal(self.OperacionIzq.tipo, izq) == self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.CADENA:
                return self.obtenerVal(self.OperacionIzq.tipo, izq) == self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.CADENA:
                return self.obtenerVal(self.OperacionIzq.tipo, izq) == self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.BOOLEANO and self.OperacionDer.tipo == TIPO.CADENA:
                return str(self.obtenerVal(self.OperacionIzq.tipo, izq)).lower() == self.obtenerVal(self.OperacionDer.tipo, der)
            elif (self.OperacionIzq.tipo == TIPO.NULO and self.OperacionDer.tipo != TIPO.NULO)or(self.OperacionIzq.tipo != TIPO.NULO and self.OperacionDer.tipo == TIPO.NULO)or(self.OperacionIzq.tipo == TIPO.NULO and self.OperacionDer.tipo == TIPO.NULO):
                return Excepcion("Semantico", "Null pointer para expresion ==.", self.fila, self.columna)
            return Excepcion("Semantico", "Tipo Erroneo de operacion para ==.", self.fila, self.columna)
 #---------------------------------------------------------DIFERENTE--------------------------------------------
        elif self.operador == OperadorRelacional.DIFERENTE:
            if self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.ENTERO:
                return self.obtenerVal(self.OperacionIzq.tipo, izq) != self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.DECIMAL:
                return self.obtenerVal(self.OperacionIzq.tipo, izq) != self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.ENTERO:
                return self.obtenerVal(self.OperacionIzq.tipo, izq) != self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.DECIMAL:
                return self.obtenerVal(self.OperacionIzq.tipo, izq) != self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.BOOLEANO and self.OperacionDer.tipo == TIPO.BOOLEANO:
                return self.obtenerVal(self.OperacionIzq.tipo, izq) != self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.CHARACTER and self.OperacionDer.tipo == TIPO.CHARACTER:
                return self.obtenerVal(self.OperacionIzq.tipo, izq) != self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.CADENA and self.OperacionDer.tipo == TIPO.ENTERO:
                return self.obtenerVal(self.OperacionIzq.tipo, izq) != str(self.obtenerVal(self.OperacionDer.tipo, der))
            elif self.OperacionIzq.tipo == TIPO.CADENA and self.OperacionDer.tipo == TIPO.DECIMAL:
                return self.obtenerVal(self.OperacionIzq.tipo, izq) != self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.CADENA and self.OperacionDer.tipo == TIPO.BOOLEANO:
                return self.obtenerVal(self.OperacionIzq.tipo, izq) != str(self.obtenerVal(self.OperacionDer.tipo, der)).lower()
            elif self.OperacionIzq.tipo == TIPO.CADENA and self.OperacionDer.tipo == TIPO.CADENA:
                return self.obtenerVal(self.OperacionIzq.tipo, izq) != self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.CADENA:
                return self.obtenerVal(self.OperacionIzq.tipo, izq) != self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.CADENA:
                return self.obtenerVal(self.OperacionIzq.tipo, izq) != self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.BOOLEANO and self.OperacionDer.tipo == TIPO.CADENA:
                return str(self.obtenerVal(self.OperacionIzq.tipo, izq)).lower() != self.obtenerVal(self.OperacionDer.tipo, der)
            elif (self.OperacionIzq.tipo == TIPO.NULO and self.OperacionDer.tipo != TIPO.NULO)or(self.OperacionIzq.tipo != TIPO.NULO and self.OperacionDer.tipo == TIPO.NULO)or(self.OperacionIzq.tipo == TIPO.NULO and self.OperacionDer.tipo == TIPO.NULO):
                return Excepcion("Semantico", "Null pointer para expresion =!.", self.fila, self.columna)
            return Excepcion("Semantico", "Tipo Erroneo de operacion para =!.", self.fila, self.columna)
#---------------------------------------------------------MAYORIGUAL--------------------------------------------
        elif self.operador == OperadorRelacional.MAYORIGUAL:
            if self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.ENTERO:
                return self.obtenerVal(self.OperacionIzq.tipo, izq) >= self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.DECIMAL:
                return self.obtenerVal(self.OperacionIzq.tipo, izq) >= self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.ENTERO:
                return self.obtenerVal(self.OperacionIzq.tipo, izq) >= self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.DECIMAL:
                return self.obtenerVal(self.OperacionIzq.tipo, izq) >= self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.BOOLEANO and self.OperacionDer.tipo == TIPO.BOOLEANO:
                return self.obtenerVal(self.OperacionIzq.tipo, izq) >= self.obtenerVal(self.OperacionDer.tipo, der)
            elif (self.OperacionIzq.tipo == TIPO.NULO and self.OperacionDer.tipo != TIPO.NULO)or(self.OperacionIzq.tipo != TIPO.NULO and self.OperacionDer.tipo == TIPO.NULO)or(self.OperacionIzq.tipo == TIPO.NULO and self.OperacionDer.tipo == TIPO.NULO):
                return Excepcion("Semantico", "Null pointer para expresion >=.", self.fila, self.columna)
            return Excepcion("Semantico", "Tipo Erroneo de operacion para >=.", self.fila, self.columna)
 #---------------------------------------------------------MENORIGUAL--------------------------------------------
        elif self.operador == OperadorRelacional.MENORIGUAL:
            if self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.ENTERO:
                return self.obtenerVal(self.OperacionIzq.tipo, izq) <= self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.DECIMAL:
                return self.obtenerVal(self.OperacionIzq.tipo, izq) <= self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.ENTERO:
                return self.obtenerVal(self.OperacionIzq.tipo, izq) <= self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.DECIMAL:
                return self.obtenerVal(self.OperacionIzq.tipo, izq) <= self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.BOOLEANO and self.OperacionDer.tipo == TIPO.BOOLEANO:
                return self.obtenerVal(self.OperacionIzq.tipo, izq) <= self.obtenerVal(self.OperacionDer.tipo, der)
            elif (self.OperacionIzq.tipo == TIPO.NULO and self.OperacionDer.tipo != TIPO.NULO)or(self.OperacionIzq.tipo != TIPO.NULO and self.OperacionDer.tipo == TIPO.NULO)or(self.OperacionIzq.tipo == TIPO.NULO and self.OperacionDer.tipo == TIPO.NULO):
                return Excepcion("Semantico", "Null pointer para expresion <=.", self.fila, self.columna)
            return Excepcion("Semantico", "Tipo Erroneo de operacion para <=.", self.fila, self.columna)
        return Excepcion("Semantico", "Tipo de Operacion Relacional no Especificado.", self.fila, self.columna) 

    def getNodo(self):
        nodo = NodoAST("RELACIONAL")
        nodo.agregarHijoNodo(self.OperacionIzq.getNodo())
        nodo.agregarHijoNodo(self.getOperador(self.operador.getNodo()))
        nodo.agregarHijoNodo(self.OperacionDer.getNodo())
        

    def getOperador(self,operador):
        if operador == OperadorRelacional.DIFERENTE:
            return "=!"
        elif operador == OperadorRelacional.IGUALIGUAL:
            return "=="
        elif operador == OperadorRelacional.MAYORIGUAL:
            return ">="
        elif operador == OperadorRelacional.MAYORQUE:
            return ">"
        elif operador == OperadorRelacional.MENORIGUAL:
            return "<="
        elif operador == OperadorRelacional.MENORQUE:
            return "<"
        else:
            return None

    def obtenerVal(self, tipo, val):
        if tipo == TIPO.ENTERO:
            return int(val)
        elif tipo == TIPO.DECIMAL:
            return float(val)
        elif tipo == TIPO.BOOLEANO:
            return bool(val)
        return str(val)
        