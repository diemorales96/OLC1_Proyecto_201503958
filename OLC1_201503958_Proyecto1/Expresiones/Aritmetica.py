from Abstract.Instruccion import Instruccion
from TS.Excepcion import Excepcion
from TS.Tipo import TIPO, OperadorAritmetico
from TS.Simbolo import Simbolo

class Aritmetica(Instruccion):
    def __init__(self, operador, OperacionIzq, OperacionDer, fila, columna):
        self.operador = operador
        self.OperacionIzq = OperacionIzq
        self.OperacionDer = OperacionDer
        self.fila = fila
        self.columna = columna
        self.tipo = None

    
    def interpretar(self, tree, table):
        izq = self.OperacionIzq.interpretar(tree, table)
        if isinstance(izq, Excepcion): return izq
        if self.OperacionDer != None:
            der = self.OperacionDer.interpretar(tree, table)
            if isinstance(der, Excepcion): return der

 #-----------------------------------------------SUMA-----------------------------------------------------------
        if self.operador == OperadorAritmetico.MAS: 
            if self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.ENTERO:
                self.tipo = TIPO.ENTERO
                return self.obtenerVal(self.OperacionIzq.tipo, izq) + self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.DECIMAL:
                self.tipo = TIPO.DECIMAL
                return self.obtenerVal(self.OperacionIzq.tipo, izq) + self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.BOOLEANO:
                self.tipo = TIPO.ENTERO
                return self.obtenerVal(self.OperacionIzq.tipo, izq) + int(self.obtenerVal(self.OperacionDer.tipo, der))
            elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.ENTERO:
                self.tipo = TIPO.DECIMAL
                return self.obtenerVal(self.OperacionIzq.tipo, izq) + self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.DECIMAL:
                self.tipo = TIPO.DECIMAL
                return self.obtenerVal(self.OperacionIzq.tipo, izq) + self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.BOOLEANO:
                self.tipo = TIPO.DECIMAL
                return self.obtenerVal(self.OperacionIzq.tipo, izq) + int(self.obtenerVal(self.OperacionDer.tipo, der))
            elif self.OperacionIzq.tipo == TIPO.BOOLEANO and self.OperacionDer.tipo == TIPO.ENTERO:
                self.tipo = TIPO.ENTERO
                return   int(self.obtenerVal(self.OperacionIzq.tipo, der)) + self.obtenerVal(self.OperacionDer.tipo, izq)
            elif self.OperacionIzq.tipo == TIPO.BOOLEANO and self.OperacionDer.tipo == TIPO.DECIMAL:
                self.tipo = TIPO.DECIMAL
                return   int(self.obtenerVal(self.OperacionIzq.tipo, izq)) + self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.CADENA:
                self.tipo = TIPO.CADENA
                return   str(self.obtenerVal(self.OperacionIzq.tipo, izq)) + self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.CADENA and self.OperacionDer.tipo == TIPO.ENTERO:
                self.tipo = TIPO.CADENA
                return   self.obtenerVal(self.OperacionIzq.tipo, izq) + str(self.obtenerVal(self.OperacionDer.tipo, der))
            elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.CADENA:
                self.tipo = TIPO.CADENA
                return   str(self.obtenerVal(self.OperacionIzq.tipo, izq)) + self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.CADENA and self.OperacionDer.tipo == TIPO.DECIMAL:
                self.tipo = TIPO.CADENA
                return   self.obtenerVal(self.OperacionIzq.tipo, izq) + str(self.obtenerVal(self.OperacionDer.tipo, der))
            elif self.OperacionIzq.tipo == TIPO.CADENA and self.OperacionDer.tipo == TIPO.DECIMAL:
                self.tipo = TIPO.CADENA
                return   self.obtenerVal(self.OperacionIzq.tipo, izq) + str(self.obtenerVal(self.OperacionDer.tipo, der))
            elif self.OperacionIzq.tipo == TIPO.BOOLEANO and self.OperacionDer.tipo == TIPO.CADENA:
                self.tipo = TIPO.CADENA
                return   str(self.obtenerVal(self.OperacionIzq.tipo, izq)) + self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.CADENA and self.OperacionDer.tipo == TIPO.BOOLEANO:
                self.tipo = TIPO.CADENA
                return   self.obtenerVal(self.OperacionIzq.tipo, izq) + str(self.obtenerVal(self.OperacionDer.tipo, der))
            elif self.OperacionIzq.tipo == TIPO.CHARACTER and self.OperacionDer.tipo == TIPO.CADENA:
                self.tipo = TIPO.CADENA
                return   self.obtenerVal(self.OperacionIzq.tipo, izq) + self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.CADENA and self.OperacionDer.tipo == TIPO.CHARACTER:
                self.tipo = TIPO.CADENA
                return   self.obtenerVal(self.OperacionIzq.tipo, izq) + self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.CADENA and self.OperacionDer.tipo == TIPO.CADENA:
                self.tipo = TIPO.CADENA
                return   self.obtenerVal(self.OperacionIzq.tipo, izq) + self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.CHARACTER and self.OperacionDer.tipo == TIPO.CHARACTER:
                self.tipo = TIPO.CADENA
                return   self.obtenerVal(self.OperacionIzq.tipo, izq) + self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.BOOLEANO and self.OperacionDer.tipo == TIPO.BOOLEANO:
                self.tipo = TIPO.ENTERO
                return   int(self.obtenerVal(self.OperacionIzq.tipo, izq)) + int(self.obtenerVal(self.OperacionDer.tipo, der))                             
            elif (self.OperacionIzq.tipo == TIPO.NULO and self.OperacionDer.tipo != TIPO.NULO)or(self.OperacionIzq.tipo != TIPO.NULO and self.OperacionDer.tipo == TIPO.NULO)or(self.OperacionIzq.tipo == TIPO.NULO and self.OperacionDer.tipo == TIPO.NULO):
                return Excepcion("Semantico", "Null pointer para expresion +.", self.fila, self.columna)
            return Excepcion("Semantico", "Tipo Erroneo de operacion para +.", self.fila, self.columna)
    #-----------------------------------------------RESTA-----------------------------------------------------------
        elif self.operador == OperadorAritmetico.MENOS: 
            if self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.ENTERO:
                self.tipo = TIPO.ENTERO
                return self.obtenerVal(self.OperacionIzq.tipo, izq) - self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.DECIMAL:
                self.tipo = TIPO.DECIMAL
                return self.obtenerVal(self.OperacionIzq.tipo, izq) - self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.BOOLEANO:
                self.tipo = TIPO.ENTERO
                return self.obtenerVal(self.OperacionIzq.tipo, izq) - int(self.obtenerVal(self.OperacionDer.tipo, der))
            elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.ENTERO:
                self.tipo = TIPO.DECIMAL
                return self.obtenerVal(self.OperacionIzq.tipo, izq) - self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.DECIMAL:
                self.tipo = TIPO.DECIMAL
                return self.obtenerVal(self.OperacionIzq.tipo, izq) - self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.BOOLEANO:
                self.tipo = TIPO.DECIMAL
                return self.obtenerVal(self.OperacionIzq.tipo, izq) - int(self.obtenerVal(self.OperacionDer.tipo, der))
            elif self.OperacionIzq.tipo == TIPO.BOOLEANO and self.OperacionDer.tipo == TIPO.ENTERO:
                self.tipo = TIPO.ENTERO
                return int(self.obtenerVal(self.OperacionIzq.tipo, izq)) - self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.BOOLEANO and self.OperacionDer.tipo == TIPO.DECIMAL:
                self.tipo = TIPO.DECIMAL
                return int(self.obtenerVal(self.OperacionIzq.tipo, izq)) - self.obtenerVal(self.OperacionDer.tipo, der)
            elif (self.OperacionIzq.tipo == TIPO.NULO and self.OperacionDer.tipo != TIPO.NULO)or(self.OperacionIzq.tipo != TIPO.NULO and self.OperacionDer.tipo == TIPO.NULO)or(self.OperacionIzq.tipo == TIPO.NULO and self.OperacionDer.tipo == TIPO.NULO):
                return Excepcion("Semantico", "Null pointer para expresion -.", self.fila, self.columna)
            return Excepcion("Semantico", "Tipo Erroneo de operacion para -.", self.fila, self.columna)
 #-----------------------------------------------MULTIPLICACION-----------------------------------------------------------
        elif self.operador == OperadorAritmetico.POR:
            if self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.ENTERO:
                self.tipo = TIPO.ENTERO
                return self.obtenerVal(self.OperacionIzq.tipo, izq) * self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.DECIMAL:
                self.tipo = TIPO.DECIMAL
                return self.obtenerVal(self.OperacionIzq.tipo, izq) * self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.ENTERO:
                self.tipo = TIPO.DECIMAL
                return self.obtenerVal(self.OperacionIzq.tipo, izq) * self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.DECIMAL:
                self.tipo = TIPO.DECIMAL
                return self.obtenerVal(self.OperacionIzq.tipo, izq) * self.obtenerVal(self.OperacionDer.tipo, der)
            elif (self.OperacionIzq.tipo == TIPO.NULO and self.OperacionDer.tipo != TIPO.NULO)or(self.OperacionIzq.tipo != TIPO.NULO and self.OperacionDer.tipo == TIPO.NULO)or(self.OperacionIzq.tipo == TIPO.NULO and self.OperacionDer.tipo == TIPO.NULO):
                return Excepcion("Semantico", "Null pointer para expresion *.", self.fila, self.columna)
            return Excepcion("Semantico", "Tipo Erroneo de operacion para *.", self.fila, self.columna)
 #-----------------------------------------------DIVISION-----------------------------------------------------------------
        elif self.operador == OperadorAritmetico.DIV:
            if self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.ENTERO:
                self.tipo = TIPO.ENTERO
                if self.obtenerVal(self.OperacionDer.tipo, der) != 0:
                    return self.obtenerVal(self.OperacionIzq.tipo, izq) / self.obtenerVal(self.OperacionDer.tipo, der)
                else:
                    return Excepcion("Semantico", "No se puede dividir un nuemero entre 0.", self.fila, self.columna)
            elif self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.DECIMAL:
                self.tipo = TIPO.DECIMAL
                if self.obtenerVal(self.OperacionDer.tipo, der) != 0:
                    return self.obtenerVal(self.OperacionIzq.tipo, izq) / self.obtenerVal(self.OperacionDer.tipo, der)
                else:
                    return Excepcion("Semantico", "No se puede dividir un nuemero entre 0.", self.fila, self.columna)
            elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.ENTERO:
                self.tipo = TIPO.DECIMAL
                if self.obtenerVal(self.OperacionDer.tipo, der) != 0:
                    return self.obtenerVal(self.OperacionIzq.tipo, izq) / self.obtenerVal(self.OperacionDer.tipo, der)
                else:
                    return Excepcion("Semantico", "No se puede dividir un nuemero entre 0.", self.fila, self.columna)
            elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.DECIMAL:
                self.tipo = TIPO.DECIMAL
                if self.obtenerVal(self.OperacionDer.tipo, der) != 0:
                    return self.obtenerVal(self.OperacionIzq.tipo, izq) / self.obtenerVal(self.OperacionDer.tipo, der)
                else:
                    return Excepcion("Semantico", "No se puede dividir un nuemero entre 0.", self.fila, self.columna)
            elif (self.OperacionIzq.tipo == TIPO.NULO and self.OperacionDer.tipo != TIPO.NULO)or(self.OperacionIzq.tipo != TIPO.NULO and self.OperacionDer.tipo == TIPO.NULO)or(self.OperacionIzq.tipo == TIPO.NULO and self.OperacionDer.tipo == TIPO.NULO):
                return Excepcion("Semantico", "Null pointer para expresion /.", self.fila, self.columna)
            return Excepcion("Semantico", "Tipo Erroneo de operacion para /.", self.fila, self.columna)
 #-----------------------------------------------POTENCIA-----------------------------------------------------------
        elif self.operador == OperadorAritmetico.POT:
            if self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.ENTERO:
                self.tipo = TIPO.ENTERO
                return self.obtenerVal(self.OperacionIzq.tipo, izq) ** self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.DECIMAL:
                self.tipo = TIPO.DECIMAL
                return self.obtenerVal(self.OperacionIzq.tipo, izq) ** self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.ENTERO:
                self.tipo = TIPO.DECIMAL
                return self.obtenerVal(self.OperacionIzq.tipo, izq) ** self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.DECIMAL:
                self.tipo = TIPO.DECIMAL
                return self.obtenerVal(self.OperacionIzq.tipo, izq) ** self.obtenerVal(self.OperacionDer.tipo, der)
            elif (self.OperacionIzq.tipo == TIPO.NULO and self.OperacionDer.tipo != TIPO.NULO)or(self.OperacionIzq.tipo != TIPO.NULO and self.OperacionDer.tipo == TIPO.NULO)or(self.OperacionIzq.tipo == TIPO.NULO and self.OperacionDer.tipo == TIPO.NULO):
                return Excepcion("Semantico", "Null pointer para expresion **.", self.fila, self.columna)
            return Excepcion("Semantico", "Tipo Erroneo de operacion para **.", self.fila, self.columna) 
 #-----------------------------------------------MODULO-----------------------------------------------------------
        elif self.operador == OperadorAritmetico.MOD:
            if self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.ENTERO:
                self.tipo = TIPO.DECIMAL
                if self.obtenerVal(self.OperacionDer.tipo, der) != 0:
                    return self.obtenerVal(self.OperacionIzq.tipo, izq) % self.obtenerVal(self.OperacionDer.tipo, der)
                else:
                    return Excepcion("Semantico", "No se puede dividir un nuemero entre 0.", self.fila, self.columna)
            elif self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.DECIMAL:
                self.tipo = TIPO.DECIMAL
                if self.obtenerVal(self.OperacionDer.tipo, der) != 0:
                    return self.obtenerVal(self.OperacionIzq.tipo, izq) % self.obtenerVal(self.OperacionDer.tipo, der)
                else:
                    return Excepcion("Semantico", "No se puede dividir un nuemero entre 0.", self.fila, self.columna)
            elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.ENTERO:
                self.tipo = TIPO.DECIMAL
                if self.obtenerVal(self.OperacionDer.tipo, der) != 0:
                    return self.obtenerVal(self.OperacionIzq.tipo, izq) % self.obtenerVal(self.OperacionDer.tipo, der)
                else:
                    return Excepcion("Semantico", "No se puede dividir un nuemero entre 0.", self.fila, self.columna)
            elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.DECIMAL:
                self.tipo = TIPO.DECIMAL
                if self.obtenerVal(self.OperacionDer.tipo, der) != 0:
                    return self.obtenerVal(self.OperacionIzq.tipo, izq) % self.obtenerVal(self.OperacionDer.tipo, der)
                else:
                    return Excepcion("Semantico", "No se puede dividir un nuemero entre 0.", self.fila, self.columna)
            elif (self.OperacionIzq.tipo == TIPO.NULO and self.OperacionDer.tipo != TIPO.NULO)or(self.OperacionIzq.tipo != TIPO.NULO and self.OperacionDer.tipo == TIPO.NULO)or(self.OperacionIzq.tipo == TIPO.NULO and self.OperacionDer.tipo == TIPO.NULO):
                return Excepcion("Semantico", "Null pointer para expresion %.", self.fila, self.columna)
            return Excepcion("Semantico", "Tipo Erroneo de operacion para %.", self.fila, self.columna)            
 #-----------------------------------------------NEGACION UNARIA-----------------------------------------------------------
        elif self.operador == OperadorAritmetico.UMENOS: 
            if self.OperacionIzq.tipo == TIPO.ENTERO:
                self.tipo = TIPO.ENTERO
                return - self.obtenerVal(self.OperacionIzq.tipo, izq)
            elif self.OperacionIzq.tipo == TIPO.DECIMAL:
                self.tipo = TIPO.DECIMAL
                return - self.obtenerVal(self.OperacionIzq.tipo, izq)
            elif self.OperacionIzq.tipo == TIPO.NULO:
                return Excepcion("Semantico", "Null pointer para expresion - unario.", self.fila, self.columna)
            return Excepcion("Semantico", "Tipo Erroneo de operacion para - unario.", self.fila, self.columna)
 #---------------------------------------------Incremento--------------------------------------------------------------------
        elif self.operador == OperadorAritmetico.INCREMENTO:    
            if self.OperacionIzq.tipo == TIPO.ENTERO:
                self.tipo = TIPO.ENTERO
                simbolo = Simbolo(self.OperacionIzq.identificador, self.OperacionIzq.tipo, self.fila, self.columna, izq +1)
                table.actualizarTabla(simbolo)
                return  self.obtenerVal(self.OperacionIzq.tipo, izq)+1
            elif self.OperacionIzq.tipo == TIPO.DECIMAL:
                self.tipo = TIPO.DECIMAL
                simbolo = Simbolo(self.OperacionIzq.identificador, self.OperacionIzq.tipo, self.fila, self.columna, izq +1)
                table.actualizarTabla(simbolo)
                return  self.obtenerVal(self.OperacionIzq.tipo, izq)+1
            elif self.OperacionIzq.tipo == TIPO.NULO:
                return Excepcion("Semantico", "Null pointer para expresion Incremento.", self.fila, self.columna)
            return Excepcion("Semantico", "Tipo Erroneo de operacion para Incremento.", self.fila, self.columna)    
 #---------------------------------------------DECREMENTO--------------------------------------------------------------------
        elif self.operador == OperadorAritmetico.Decremento:    
            if self.OperacionIzq.tipo == TIPO.ENTERO:
                self.tipo = TIPO.ENTERO
                simbolo = Simbolo(self.OperacionIzq.identificador, self.OperacionIzq.tipo, self.fila, self.columna, izq -1)
                table.actualizarTabla(simbolo)
                return  self.obtenerVal(self.OperacionIzq.tipo, izq)-1
            elif self.OperacionIzq.tipo == TIPO.DECIMAL:
                self.tipo = TIPO.DECIMAL
                simbolo = Simbolo(self.OperacionIzq.identificador, self.OperacionIzq.tipo, self.fila, self.columna, izq -1)
                table.actualizarTabla(simbolo)
                return  self.obtenerVal(self.OperacionIzq.tipo, izq)-1
            elif self.OperacionIzq.tipo == TIPO.NULO:
                return Excepcion("Semantico", "Null pointer para expresion Decremento.", self.fila, self.columna)
            return Excepcion("Semantico", "Tipo Erroneo de operacion para Decremento.", self.fila, self.columna)    
        return Excepcion("Semantico", "Tipo de Operacion Aritmetica no Especificado.", self.fila, self.columna)



        
    def obtenerVal(self, tipo, val):
        if tipo == TIPO.ENTERO:
            return int(val)
        elif tipo == TIPO.DECIMAL:
            return float(val)
        elif tipo == TIPO.BOOLEANO:
            return bool(val)
        return str(val)
        