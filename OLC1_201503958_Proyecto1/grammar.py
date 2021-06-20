
from Instrucciones.Main import Main
import re
import os
from TS.Excepcion import Excepcion
import webbrowser
from tkinter import messagebox
from tkinter.messagebox import showerror
from tkinter import Tk, Menu, messagebox, filedialog, ttk, Label, scrolledtext, INSERT, END, Button, Scrollbar, RIGHT, Y, Frame, Canvas, HORIZONTAL, VERTICAL, simpledialog, Text
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import tkinter as tk
import tkinter.font as tkFont

#///////////////////////////////////////ANALISIS LEXICO//////////////////////////////////////////
errores = []
reservadas = {
    'print'     : 'RPRINT',
    'if'        : 'RIF',
    'case'      : 'RCASE',
    'for'       : 'RFOR',
    'else'      : 'RELSE',
    'while'     : 'RWHILE',
    'true'      : 'RTRUE',
    'false'     : 'RFALSE',
    'break'     : 'RBREAK',
    'var'       : 'RVAR',
    'null'      : 'RNULL',
    'main'      : 'RMAIN'
}

tokens  = [
    'PUNTOCOMA',
    'PARA',
    'PARC',
    'LLAVEA',
    'LLAVEC',
    'MAS',
    'MASMAS',
    'MENOS',
    'MENOSMENOS',
    'POR',
    'DIV',
    'MOD',
    'POT',
    'MENORQUE',
    'MAYORQUE',
    'MENORIGUAL',
    'MAYORIGUAL',
    'IGUALIGUAL',
    'DIFERENTE',
    'IGUAL',
    'AND',
    'OR',
    'NOT',
    'DECIMAL',
    'ENTERO',
    'CADENA',
    'CARACTER',
    'ID',
    'DOSPUNTOS'
] + list(reservadas.values())

# Tokens
t_PUNTOCOMA     = r';'
t_PARA          = r'\('
t_PARC          = r'\)'
t_LLAVEA        = r'{'
t_LLAVEC        = r'}'
t_MAS           = r'\+'
t_MASMAS        = r'\+\+'
t_MENOS         = r'-'
t_MENOSMENOS    = r'--'
t_POR           = r'\*'
t_DIV           = r'/'
t_MOD           = r'%'
t_POT           = r'\*\*'
t_MENORQUE      = r'<'
t_MAYORQUE      = r'>'
t_MENORIGUAL    = r'<='
t_MAYORIGUAL    = r'>='
t_DIFERENTE     = r'=!'
t_IGUALIGUAL    = r'=='
t_IGUAL         = r'='
t_AND           = r'&&'
t_OR            = r'\|\|'
t_NOT           = r'!'
t_DOSPUNTOS     = r':'

def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Float value too large %d", t.value)
        t.value = 0
    return t

def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

def t_COMENTARIO_MULT(t):
    r'\#\*(.|\n)*?\*\#'
    t.lexer.lineno += 1

def t_COMENTARIO_SIMPLE(t):
    r'\#.*\n'
    t.lexer.lineno += 1

def t_ID(t):
     r'[a-zA-Z][a-zA-Z_0-9]*'
     t.type = reservadas.get(t.value.lower(),'ID')
     return t

def t_CADENA(t):
    r'\"(\\"|.)*?\"'
    t.value = t.value[1:-1]
    t.value = t.value.replace('\\t', '\t')
    t.value = t.value.replace('\\n', '\n')
    t.value = t.value.replace("\\'", "\'")
    t.value = t.value.replace('\\"', '\"')
    t.value = t.value.replace('\\\\', '\\')
    return t

def t_CARACTER(t):
    r"""\'(\\'|\\\\|\\n|\\t|\\r|\\"|[^\\\'\"])?\'"""
    t.value = t.value[1:-1]
    t.value = t.value.replace('\\t', '\t')
    t.value = t.value.replace('\\n', '\n')
    t.value = t.value.replace("\\'", "\'")
    t.value = t.value.replace('\\"', '\"')
    t.value = t.value.replace('\\\\', '\\')
    return t

t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    errores.append(Excepcion("Lexico","Error léxico." + t.value[0] , t.lexer.lineno, find_column(input, t)))
    t.lexer.skip(1)

def find_column(inp, token):
    line_start = inp.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1

import ply.lex as lex
lexer = lex.lex(reflags= re.IGNORECASE)

#///////////////////////////////////////PRECEDENCIA/ANALISIS SINTACTICO//////////////////////////////////////////

precedence = (
    ('left','OR'),
    ('left','AND'),
    ('right','UNOT'),
    ('left','MENORQUE','MAYORQUE', 'IGUALIGUAL','DIFERENTE','MENORIGUAL','MAYORIGUAL'), 
    ('left','MAS','MENOS'),
    ('left','DIV','POR','MOD'),
    ('left','POT'),
    ('right','UMENOS','MASMAS','MENOSMENOS'),
    )


from Abstract.Instruccion import Instruccion
from Instrucciones.Imprimir import Imprimir
from Expresiones.Primitivos import Primitivos
from TS.Tipo import OperadorAritmetico, OperadorLogico, TIPO, OperadorRelacional
from Expresiones.Aritmetica import Aritmetica
from Expresiones.Relacional import Relacional
from Expresiones.Logica import Logica
from Instrucciones.Declaracion import Declaracion
from Expresiones.Identificador import Identificador
from Instrucciones.Asignacion import Asignacion
from Instrucciones.If import If
from Instrucciones.While import While
from Instrucciones.For import For
from Instrucciones.Break import Break
from Instrucciones.Incremento import Incremento

def p_init(t) :
    'init            : instrucciones'
    t[0] = t[1]

def p_instrucciones_instrucciones_instruccion(t) :
    'instrucciones    : instrucciones instruccion'
    if t[2] != "":
        t[1].append(t[2])
    t[0] = t[1]
    
#///////////////////////////////////////INSTRUCCIONES//////////////////////////////////////////////////

def p_instrucciones_instruccion(t) :
    'instrucciones    : instruccion'
    if t[1] == "":
        t[0] = []
    else:    
        t[0] = [t[1]]

#///////////////////////////////////////INSTRUCCION//////////////////////////////////////////////////

def p_instruccion(t) :
    '''instruccion      : imprimir_instr finins
                        | declaraciones finins
                        | if_instr
                        | while_instr
                        | break_instr finins
                        | incremento_decremento_instr finins
                        | for_instr
                        | main_instr'''
    t[0] = t[1]

def p_finins(t) :
    '''finins       : PUNTOCOMA
                    | '''
    t[0] = None
#///////////////////////////////////////RECUPERACION//////////////////////////////////////////
def p_instruccion_error(t):
    'instruccion        : error PUNTOCOMA'
    errores.append(Excepcion("Sintáctico","Error Sintáctico." + str(t[1].value) , t.lineno(1), find_column(input, t.slice[1])))
    t[0] = ""
#///////////////////////////////////////IMPRIMIR//////////////////////////////////////////////////

def p_imprimir(t) :
    'imprimir_instr     : RPRINT PARA expresion PARC'
    t[0] = Imprimir(t[3], t.lineno(1), find_column(input, t.slice[1]))
#///////////////////////////////////////DECLARACIONES/ASIGNACIONES//////////////////////////////////////////
def p_declaraciones(t):
    '''declaraciones    : declaracion_instr_simple 
                        | declaracion_instr_completa 
                        | asignacion_instr'''
    t[0] = t[1]

#///////////////////////////////////////DECLARACION COMPLETA//////////////////////////////////////////////////

def p_declaracion_completa(t) :
    'declaracion_instr_completa     : RVAR ID IGUAL expresion'
    
    t[0] = Declaracion(t[2], t.lineno(2), find_column(input, t.slice[2]), t[4])

#///////////////////////////////////////DECLARACION SIMPLE//////////////////////////////////////////////////

def p_declaracion_simple(t) :
    'declaracion_instr_simple     : RVAR ID'
    primitivo_nulo = Primitivos(TIPO.NULO, None, t.lineno(1), find_column(input, t.slice[1]))
    t[0] = Declaracion(t[2], t.lineno(2), find_column(input, t.slice[2]),primitivo_nulo)

#///////////////////////////////////////ASIGNACION//////////////////////////////////////////////////

def p_asignacion(t) :
    'asignacion_instr     : ID IGUAL expresion'
    t[0] = Asignacion(t[1], t[3], t.lineno(1), find_column(input, t.slice[1]))

#///////////////////////////////////////IF//////////////////////////////////////////////////

def p_if1(t) :
    'if_instr     : RIF PARA expresion PARC LLAVEA instrucciones LLAVEC'
    t[0] = If(t[3], t[6], None, None, t.lineno(1), find_column(input, t.slice[1]))

def p_if2(t) :
    'if_instr     : RIF PARA expresion PARC LLAVEA instrucciones LLAVEC RELSE LLAVEA instrucciones LLAVEC'
    t[0] = If(t[3], t[6], t[10], None, t.lineno(1), find_column(input, t.slice[1]))

def p_if3(t) :
    'if_instr     : RIF PARA expresion PARC LLAVEA instrucciones LLAVEC RELSE if_instr'
    t[0] = If(t[3], t[6], None, t[9], t.lineno(1), find_column(input, t.slice[1]))

#///////////////////////////////////////SWITCH//////////////////////////////////////////////////

#def p_switch(t):
#    'switch_instr   : RSWITCH PARA expresion PARC LLAVEA case_list LLAVEC'
#    t[0] = SWITCH(t[3],t[6],t.lineno(1),find_column(input,t.slice[1]))
#def p_case(t):
#    'case_list  : RCASE expresion DOSPUNTOS instrucciones'
#    t[0] = CASE(t[2],t[4], t.lineno(1),find_column(input,t.slice[1]))

#///////////////////////////////////////WHILE//////////////////////////////////////////////////

def p_while(t) :
    'while_instr     : RWHILE PARA expresion PARC LLAVEA instrucciones LLAVEC'
    t[0] = While(t[3], t[6], t.lineno(1), find_column(input, t.slice[1]))

#///////////////////////////////////////FOR//////////////////////////////////////////////////

def p_for(t) :
    'for_instr     : RFOR PARA declaraciones PUNTOCOMA expresion PUNTOCOMA incremento_decremento_instr PARC LLAVEA instrucciones LLAVEC'
    t[0] =  For(t[3], t[5],t[7],t[10], t.lineno(1), find_column(input, t.slice[1]))


#///////////////////////////////////////BREAK//////////////////////////////////////////////////

def p_break(t) :
    'break_instr     : RBREAK'
    t[0] = Break(t.lineno(1), find_column(input, t.slice[1]))

#///////////////////////////////////////MAIN//////////////////////////////////////////

def p_main(t):
    'main_instr     : RMAIN PARA PARC LLAVEA instrucciones LLAVEC'
    t[0] = Main(t[5],t.lineno(1),find_column(input,t.slice[1]))
 
#///////////////////////////////////////EXPRESION//////////////////////////////////////////////////

def p_expresion_binaria(t):
    '''
    expresion : expresion MASMAS
            | expresion MAS expresion
            | expresion MENOSMENOS
            | expresion MENOS expresion
            | expresion POR expresion
            | expresion DIV expresion
            | expresion POT expresion
            | expresion MOD expresion
            | expresion MENORQUE expresion
            | expresion MAYORQUE expresion
            | expresion MENORIGUAL expresion
            | expresion MAYORIGUAL expresion
            | expresion DIFERENTE expresion
            | expresion IGUALIGUAL expresion
            | expresion AND expresion
            | expresion OR expresion
    '''
    if t[2] == '++':
        t[0] = Aritmetica(OperadorAritmetico.INCREMENTO, t[1],None, t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '+':
        t[0] = Aritmetica(OperadorAritmetico.MAS, t[1],t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '--':
        t[0] = Aritmetica(OperadorAritmetico.Decremento, t[1],None, t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '-':
        t[0] = Aritmetica(OperadorAritmetico.MENOS, t[1],t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '*':
        t[0] = Aritmetica(OperadorAritmetico.POR, t[1],t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '/':
        t[0] = Aritmetica(OperadorAritmetico.DIV, t[1],t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '**':
        t[0] = Aritmetica(OperadorAritmetico.POT, t[1],t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '%':
        t[0] = Aritmetica(OperadorAritmetico.MOD, t[1],t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '<=':
        t[0] = Relacional(OperadorRelacional.MENORIGUAL, t[1],t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '>=':
        t[0] = Relacional(OperadorRelacional.MAYORIGUAL, t[1],t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '<':
        t[0] = Relacional(OperadorRelacional.MENORQUE, t[1],t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '>':
        t[0] = Relacional(OperadorRelacional.MAYORQUE, t[1],t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '==':
        t[0] = Relacional(OperadorRelacional.IGUALIGUAL, t[1],t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '=!':
        t[0] = Relacional(OperadorRelacional.DIFERENTE, t[1],t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '&&':
        t[0] = Logica(OperadorLogico.AND, t[1],t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '||':
        t[0] = Logica(OperadorLogico.OR, t[1],t[3], t.lineno(2), find_column(input, t.slice[2]))

#///////////////////////////////////////UNARIO//////////////////////////////////////////
def p_expresion_unaria(t):
    '''
    expresion : MENOS expresion %prec UMENOS 
            | NOT expresion %prec UNOT 
    '''
    if t[1] == '-':
        t[0] = Aritmetica(OperadorAritmetico.UMENOS, t[2],None, t.lineno(1), find_column(input, t.slice[1]))
    elif t[1] == '!':
        t[0] = Logica(OperadorLogico.NOT, t[2],None, t.lineno(1), find_column(input, t.slice[1]))
#///////////////////////////////////////INCREMENTO Y DECREMENTO//////////////////////////////////////////
def p_incremento(t):
    '''
    incremento_decremento_instr : expresion MASMAS 
                                | expresion MENOSMENOS
    '''
    if t[2] == '++':
        t[0] = Incremento(OperadorAritmetico.INCREMENTO, t[1],None, t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '--':
        t[0] = Incremento(OperadorAritmetico.Decremento, t[1],None, t.lineno(2), find_column(input, t.slice[2]))
#///////////////////////////////////////AGRUPACIONES//////////////////////////////////////////
def p_expresion_agrupacion(t):
    '''
    expresion :   PARA expresion PARC 
    '''
    t[0] = t[2]
#///////////////////////////////////////PRIMITIVOS//////////////////////////////////////////
def p_expresion_identificador(t):
    '''expresion : ID'''
    t[0] = Identificador(t[1], t.lineno(1), find_column(input, t.slice[1]))

def p_expresion_entero(t):
    '''expresion : ENTERO'''
    t[0] = Primitivos(TIPO.ENTERO,t[1], t.lineno(1), find_column(input, t.slice[1]))

def p_primitivo_decimal(t):
    '''expresion : DECIMAL'''
    t[0] = Primitivos(TIPO.DECIMAL, t[1], t.lineno(1), find_column(input, t.slice[1]))


def p_primitivo_cadena(t):
    '''expresion : CADENA'''
    t[0] = Primitivos(TIPO.CADENA,str(t[1]).replace('\\n', '\n'), t.lineno(1), find_column(input, t.slice[1]))

def p_primitivo_caracter(t):
    '''expresion : CARACTER'''
    t[0] = Primitivos(TIPO.CHARACTER,str(t[1]).replace('\\n', '\n'), t.lineno(1), find_column(input, t.slice[1]))

def p_primitivo_true(t):
    '''expresion : RTRUE'''
    t[0] = Primitivos(TIPO.BOOLEANO, True, t.lineno(1), find_column(input, t.slice[1]))

def p_primitivo_false(t):
    '''expresion : RFALSE'''
    t[0] = Primitivos(TIPO.BOOLEANO, False, t.lineno(1), find_column(input, t.slice[1]))

def p_primitivo_null(t):
    '''expresion : RNULL'''
    t[0] = Primitivos(TIPO.NULO, None, t.lineno(1), find_column(input, t.slice[1]))

import ply.yacc as yacc
parser = yacc.yacc()

input = ''

def getErrores():
    return errores

def parse(inp) :
    global errores
    global lexer
    global parser
    errores = []
    lexer = lex.lex(reflags= re.IGNORECASE)
    parser = yacc.yacc()
    global input
    input = inp
    return parser.parse(inp)

from TS.Arbol import Arbol
from TS.TablaSimbolos import TablaSimbolos
def analizar():
    entrada = Text1.get(1.0,END)

    instrucciones = parse(entrada) 
    ast = Arbol(instrucciones)
    TSGlobal = TablaSimbolos()
    ast.setTSglobal(TSGlobal)
    
    for error in errores:                  
        ast.getExcepciones().append(error)
        ast.updateConsola(error.toString())

    for instruccion in ast.getInstrucciones():     
        if isinstance(instruccion, Declaracion) or isinstance(instruccion, Asignacion):
            value = instruccion.interpretar(ast,TSGlobal)
            if isinstance(value, Excepcion) :
                ast.getExcepciones().append(value)
                ast.updateConsola(value.toString())
            if isinstance(value, Break): 
                err = Excepcion("Semantico", "Sentencia BREAK fuera de ciclo", instruccion.fila, instruccion.columna)
                ast.getExcepciones().append(err)
                ast.updateConsola(err.toString())
            
    for instruccion in ast.getInstrucciones():     
        contador = 0
        if isinstance(instruccion, Main):
            contador += 1
            if contador == 2: 
                err = Excepcion("Semantico", "Existen 2 funciones Main", instruccion.fila, instruccion.columna)
                ast.getExcepciones().append(err)
                ast.updateConsola(err.toString())
                break
            value = instruccion.interpretar(ast,TSGlobal)
            if isinstance(value, Excepcion) :
                ast.getExcepciones().append(value)
                ast.updateConsola(value.toString())
            if isinstance(value, Break): 
                err = Excepcion("Semantico", "Sentencia BREAK fuera de ciclo", instruccion.fila, instruccion.columna)
                ast.getExcepciones().append(err)
                ast.updateConsola(err.toString())

    for instruccion in ast.getInstrucciones():  
        if not (isinstance(instruccion, Main) or isinstance(instruccion, Declaracion) or isinstance(instruccion, Asignacion)):
            err = Excepcion("Semantico", "Sentencias fuera de Main", instruccion.fila, instruccion.columna)
            ast.getExcepciones().append(err)
            ast.updateConsola(err.toString())

    ReporteTabla(ast.getExcepciones())
    salida.delete(1.0,END)
    s = ast.getConsola()
    print(s)
    salida.insert(INSERT,s)
#END

def ReporteTabla(Errores):
    cadena = "<html>\n <head> <head>\n<body>\n<center>\n<table border=\"1\" class = \"egt\">\n\t"
    cadena = cadena + "\n\t\t<th>No.</th>\n\t\t<th>Fila</th>\n\t\t<th>Columna</th>\n\t\t<th>Descripcion</th>\n\t\t<th>Tipo de Error.</th>\n\t</tr>\n" 
    cont = 1
    for a in Errores:
        cadena = cadena + "<tr>\n\t\t<td>"+ str(cont) +"</td>\n"
        cadena = cadena + "\n\t\t<td>"+ str(a.fila) +"</td>\n"
        cadena = cadena + "\n\t\t<td>"+ str(a.columna) +"</td>\n"
        cadena = cadena + "\n\t\t<td>"+ a.descripcion +"</td>\n"
        cadena = cadena + "\n\t\t<td>"+ a.tipo +"</td>\n"
    cont += 1
    cadena = cadena +"</table>\n</body>\n</html>"
    crearArchivo(cadena,".")

def crearArchivo(cadena,path):
        try:
            os.stat(path.strip())
        except:
            os.makedirs(path.strip())
        with open(path+"Reporte Errores.html","w+") as file:
            file.seek(0,0)
            file.write(cadena)
            file.close()
        #END
    #END

def load_file():
    name = askopenfilename(initialdir="C:/Users/Batman/Documents/Programming/tkinter/",
                           filetypes =(("Text File", "*.jpr"),("All Files","*.*")),
                           title = "Choose a file."
                           )
    try:
        with open(name,'r',encoding="utf-8") as UseFile:
            Text1.delete(1.0,END)
            texto = UseFile.read()
            Text1.insert(INSERT,texto)
    except:
        print("No file exists")
#END

def mostrar_Reporte():
    webbrowser.open_new_tab('.Reporte Errores.html')


def close_window (): 
    app.destroy()
#END

app = Tk()
app.geometry("1350x500")
app.title("Proyecto")

Vp = Frame(app)
menubar = Menu(app)

Vp.grid(column = 0, row = 0,padx =(70,70), pady=(10,10))

filemenu = Menu(menubar)
filemenu = Menu(menubar)
filemenu.add_command(label="Nuevo")
filemenu.add_command(label="Abrir", command = load_file)
filemenu.add_command(label="Guardar")
filemenu.add_command(label="Guardar Como")
filemenu.add_command(label="Ejecutar Analizar", command = analizar)
filemenu.add_command(label = "Reporte de Errores", command = mostrar_Reporte)
filemenu.add_command(label="Salir",command = close_window)

menubar.add_cascade(label="File", menu=filemenu)

app.config(menu=menubar)

fontInput = tkFont.Font(family="Courier New", size=10, weight="bold")
fontOutput = tkFont.Font(family="Courier New", size=10)
Text1 = tkinter.Text()
Text1.configure(font=fontInput)
Text1.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)

scrollb = ttk.Scrollbar(command = Text1.yview)
scrollb.grid(row=0, column=1, sticky='nsew')
Text1['yscrollcommand'] = scrollb.set

salida = tkinter.Text()

salida.configure(font = fontOutput,background = '#0000D6',foreground = 'white')
salida.grid(row=0, column=2, sticky="nsew", padx=2, pady=2)

scrollb = ttk.Scrollbar(command = salida.yview)
scrollb.grid(row=0, column=3, sticky='nsew')
salida['yscrollcommand'] = scrollb.set

app.mainloop()