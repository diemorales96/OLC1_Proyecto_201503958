

from TS.Excepcion import Excepcion
from TS.Tipo import TIPO

class TablaSimbolos:
    def __init__(self, anterior = None,entorno = None,tipo_dec = None):
        self.tabla = {} 
        self.anterior = anterior
        self.entorno = entorno
        self.tipo_dec = tipo_dec
        
    TSIMB = []
    def setTabla(self, simbolo): 
        if simbolo.id.lower() in self.tabla :
            return Excepcion("Semantico", "Variable " + simbolo.id + " ya existe", simbolo.fila, simbolo.columna)
        else:
            self.tabla[simbolo.id.lower()] = simbolo
            if simbolo.arreglo == False:
                self.tipo_dec = "VARIABLE"
            else:
                self.tipo_dec = "ARREGLO"
            self.TSIMB.append([self.entorno,self.tipo_dec,simbolo.id.lower()])
            return None

    def getTabla(self, id):        
        tablaActual = self
        while tablaActual != None:
            if id.lower() in tablaActual.tabla :
                return tablaActual.tabla[id.lower()]   
            else:
                tablaActual = tablaActual.anterior
        return None

    def actualizarTabla(self, simbolo):
        tablaActual = self
        while tablaActual != None:
            if simbolo.id.lower() in tablaActual.tabla :
                if tablaActual.tabla[simbolo.id.lower()].getTipo() == simbolo.getTipo():
                    tablaActual.tabla[simbolo.id.lower()].setValor(simbolo.getValor())
                    tablaActual.tabla[simbolo.id.lower()].setTipo(simbolo.getTipo())
                    return None
                elif tablaActual.tabla[simbolo.id.lower()].getTipo() == TIPO.NULO:
                    tablaActual.tabla[simbolo.id.lower()].setValor(simbolo.getValor())
                    tablaActual.tabla[simbolo.id.lower()].setTipo(simbolo.getTipo())
                    return None
                elif simbolo.getValor() == None:
                    tablaActual.tabla[simbolo.id.lower()].setValor(simbolo.getValor())
                    tablaActual.tabla[simbolo.id.lower()].setTipo(simbolo.getTipo())
                    return None
                return Excepcion("Semantico", "Tipo de dato Diferente en Asignacion", simbolo.getFila(), simbolo.getColumna())

            else:
                tablaActual = tablaActual.anterior
            
        return Excepcion("Semantico", "Variable No encontrada en Asignacion", simbolo.getFila(), simbolo.getColumna())
        
    def obtenerTSimbolos(self):
        print(self.TSIMB)
