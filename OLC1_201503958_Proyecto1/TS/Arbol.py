from TS.Tipo import OperadorAritmetico


class Arbol:
    def __init__(self, instrucciones ):
        self.instrucciones = instrucciones
        self.excepciones = []
        self.consola = ""
        self.TSglobal = None
        self.funciones = []
        self.cons = None
        self.dot = ""
        self.contador = 0


    def getInstrucciones(self):
        return self.instrucciones

    def setInstrucciones(self, instrucciones):
        self.instrucciones = instrucciones

    def getExcepciones(self):
        return self.excepciones

    def setExcepciones(self, excepciones):
        self.excepciones = excepciones

    def getConsola(self):
        return self.consola
    
    def setConsola(self, consola):
        self.consola = consola

    def updateConsola(self,cadena):
        self.consola += str(cadena) + '\n'

    def getTSGlobal(self):
        return self.TSglobal
    
    def setTSglobal(self, TSglobal):
        self.TSglobal = TSglobal
        
    def getFunciones(self):
        return self.funciones

    def getFuncion(self, nombre):
        for funcion in self.funciones:
            if funcion.nombre == nombre:
                return funcion
        return None
    
    def addFuncion(self, funcion):
        self.funciones.append(funcion)
    
    def setCons(self,consola):
        self.cons = consola

    def getCons(self):
        return self.cons
    
    def getDot(self, raiz): 
        self.dot = ""
        self.dot += "digraph {\n"
        self.dot += "n0[label=\"" + raiz.getValor().replace("\"", "\\\"") + "\"];\n"
        self.contador = 1
        self.recorrerAST("n0", raiz)
        self.dot += "}"
        return self.dot

    def recorrerAST(self, idPadre, nodoPadre):
        for hijo in nodoPadre.getHijos():
            nombreHijo = "n" + str(self.contador)
            self.dot += nombreHijo + "[label=\"" + str(self.getOperador(hijo.getValor().replace("\"", "\\\""))) + "\"];\n"
            self.dot += idPadre + "->" + nombreHijo + ";\n"
            self.contador += 1
            self.recorrerAST(nombreHijo, hijo)

    def getOperador(self,operador):
        if operador == 'OperadorAritmetico.MAS':
            return '+'
        elif operador == 'OperadorAritmetico.MENOS':
            return "-"
        elif operador == 'OperadorAritmetico.UMENOS':
            return "-"
        elif operador == 'OperadorAritmetico.POR':
            return "*"
        elif operador == 'OperadorAritmetico.DIV':
            return "/"
        elif operador == 'OperadorAritmetico.POT':
            return "**"
        elif operador == 'OperadorAritmetico.MOD':
            return "%"
        elif operador == 'OperadorAritmetico.INCREMENTO':
            return "++"
        elif operador == 'OperadorAritmetico.Decremento':
            return "--"
        elif operador == 'TIPO.ARREGLO':
            return "ARREGLO"
        elif operador == 'TIPO.BOOLEANO':
            return "BOOLEANO"
        elif operador == 'TIPO.CADENA':
            return "CADENA"
        elif operador == 'TIPO.CHARACTER':
            return "CHARACTER"
        elif operador == 'TIPO.DECIMAL':
            return "DECIMAL"
        elif operador == 'TIPO.ENTERO':
            return "ENTERO"
        elif operador == 'OperadorLogico.AND':
            return "&&"
        elif operador =='OperadorLogico.OR':
            return "||"
        elif operador == 'OperadorLogico.NOT':
            return "!"
        elif operador == 'OperadorRelacional.DIFERENTE':
            return "=!"
        elif operador == 'OperadorRelacional.IGUALIGUAL':
            return "=="
        elif operador == 'OperadorRelacional.MAYORIGUAL':
            return ">="
        elif operador =='OperadorRelacional.MAYORQUE':
            return ">"
        elif operador == 'OperadorRelacional.MENORIGUAL':
            return "<="
        elif operador == 'OperadorRelacional.MENORQUE':
            return "<" 
        else:
            return operador