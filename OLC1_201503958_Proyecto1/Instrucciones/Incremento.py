from Abstract.NodoAST import NodoAST
from Abstract.Instruccion import Instruccion
from TS.Excepcion import Excepcion
from TS.Tipo import TIPO, OperadorAritmetico
from TS.Simbolo import Simbolo

class Incremento(Instruccion):
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
 #---------------------------------------------Incremento--------------------------------------------------------------------            
        if self.operador == OperadorAritmetico.INCREMENTO:    
            if self.OperacionIzq.tipo == TIPO.ENTERO:
                self.tipo = TIPO.ENTERO
                simbolo = Simbolo(self.OperacionIzq.identificador,self.OperacionIzq.tipo , self.fila, self.columna, self.obtenerVal(self.OperacionIzq.tipo , izq) + 1)
                res = table.actualizarTabla(simbolo)
                if isinstance(res, Excepcion): return res
                return None
            elif self.OperacionIzq.tipo == TIPO.DECIMAL:
                self.tipo = TIPO.DECIMAL
                simbolo = Simbolo(self.OperacionIzq.identificador,self.OperacionIzq.tipo , self.fila, self.columna, self.obtenerVal(self.OperacionIzq.tipo , izq) + 1)
                res = table.actualizarTabla(simbolo)
                if isinstance(res, Excepcion): return res
                return None
            return Excepcion("Semantico", "Tipo Erroneo de operacion para Incremento.", self.fila, self.columna)    
 #---------------------------------------------DECREMENTO--------------------------------------------------------------------
        elif self.operador == OperadorAritmetico.Decremento:    
            if self.OperacionIzq.tipo == TIPO.ENTERO:
                self.tipo = TIPO.ENTERO
                simbolo = Simbolo(self.OperacionIzq.identificador,self.OperacionIzq.tipo , self.fila, self.columna, self.obtenerVal(self.OperacionIzq.tipo , izq) - 1)
                res = table.actualizarTabla(simbolo)
                if isinstance(res, Excepcion): return res
                return None
            elif self.OperacionIzq.tipo == TIPO.DECIMAL:
                self.tipo = TIPO.DECIMAL
                simbolo = Simbolo(self.OperacionIzq.identificador,self.OperacionIzq.tipo , self.fila, self.columna, self.obtenerVal(self.OperacionIzq.tipo , izq) - 1)
                res = table.actualizarTabla(simbolo)
                if isinstance(res, Excepcion): return res
                return None
            return Excepcion("Semantico", "Tipo Erroneo de operacion para Incremento.", self.fila, self.columna)    
        return Excepcion("Semantico", "Tipo de Operacion no Especificado.", self.fila, self.columna)

    def getNodo(self):
        nodo = NodoAST("INCREMENTO")
        if self.OperacionDer != None:
            nodo.agregarHijoNodo(self.OperacionIzq.getNodo())
            nodo.agregarHijo(self.operador)
            nodo.agregarHijoNodo(self.OperacionDer.getNodo())
        else:
            nodo.agregarHijo(self.operador)
            nodo.agregarHijoNodo(self.OperacionIzq.getNodo())
        return nodo

    def obtenerVal(self, tipo, val):
        if tipo == TIPO.ENTERO:
            return int(val)
        elif tipo == TIPO.DECIMAL:
            return float(val)
        elif tipo == TIPO.BOOLEANO:
            return bool(val)
        return str(val)