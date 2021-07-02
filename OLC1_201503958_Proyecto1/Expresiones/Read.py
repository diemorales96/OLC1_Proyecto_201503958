from Abstract.NodoAST import NodoAST
from Abstract.Instruccion import Instruccion
from TS.Tipo import TIPO
from tkinter import *
import sys

class Read(Instruccion):
    def __init__(self, fila, columna):
        self.fila = fila
        self.columna = columna
        self.tipo = TIPO.CADENA

    def interpretar(self, tree, table):
        consola = tree.getCons()
        consola.delete('1.0',END)
        consola.insert(INSERT,str(tree.getConsola()))
        raiz = Tk()
        window = mainWindow(raiz)
        raiz.mainloop()
        lectura = window.entryValue()
        return lectura

    def getNodo(self):
        nodo = NodoAST("READ")
        return nodo

class popupWindow(object):
    def __init__(self,master):
        top=self.top=Toplevel(master)
        self.l=Label(top,text="Ingrese un valor:")
        self.l.pack()
        self.e=Entry(top)
        self.e.pack()
        self.b=Button(top,text='Ingresar',command=self.getValueRead)
        self.b.pack()
    
    def cleanup(self):
        self.top.destroy()

    def getValueRead(self):
        self.value = self.e.get()
        self.top.destroy()
        return self.value


class mainWindow(object):
    def __init__(self,master):
        self.master=master
        self.b=Button(master,text="Colocar Nuevo Valor",command=self.popup)
        self.b.pack()
        self.b2=Button(master,text="Ingresar Nuevo Valor",command=lambda :self.destruir())
        self.b2.pack()
    def destruir(self):
        self.master.after(1000, lambda: self.master.quit())
        self.master.after(1000, lambda: self.master.destroy())

    def popup(self):
        self.w=popupWindow(self.master)
        self.b["state"] = "disabled"
        self.master.wait_window(self.w.top)
        self.b["state"] = "normal"

    def entryValue(self):
        return self.w.value