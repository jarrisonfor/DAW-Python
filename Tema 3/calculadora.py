"""
UT4-AEA1 Calculadora simple - Operaciones aritméticas
Implementar nuevas funcionalidades para la calculadora incluyendo nuevos botones
"""

import re
from tkinter import Tk, Text, Button, END


class Interfaz(object):
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Calculadora")
        self.ventana.grid_columnconfigure(0, weight=1)
        self.ventana.geometry('330x230')
        self.ventana.resizable(0, 0)
        self.pantalla = Text(
            ventana,
            state="disabled",
            height=3,
            background="orchid",
            foreground="white",
            font=(
                "Helvetica",
                15
            )
        )
        self.pantalla.grid(
            row=0,
            column=0,
            columnspan=5,
            padx=5,
            pady=5,
            sticky="ew"
        )
        self.operacion = ""

        grid = [
            [u"\u00F7", u"\u00D7", '-', '+', u"\u232B"],
            ['7', '8', '9', '(', 'C', ],
            ['4', '5', '6', None, '='],
            ['1', '2', '3', ')', None],
            ['0', None, '.', None, None],
        ]

        for i, row in enumerate(grid):
            for j, button in enumerate(row):
                if button == '0':
                    self.crearBoton(button).grid(
                        row=i + 1,
                        column=j,
                        columnspan=2,
                        sticky="ew"
                    )
                elif button == '=':
                    self.crearBoton(button).grid(
                        row=i + 1,
                        column=j,
                        rowspan=3,
                        sticky="nsew"
                    )
                elif button == ')' or button == '(':
                    self.crearBoton(button).grid(
                        row=i + 1,
                        column=j,
                        rowspan=2,
                        sticky="nsew"
                    )
                elif button:
                    self.crearBoton(button).grid(
                        row=i + 1,
                        column=j,
                        sticky="ew"
                    )
        return

    def crearBoton(self, valor):
        return Button(
            text=valor,
            width=4,
            font=("Helvetica", 15),
            command=lambda: self.click(valor)
        )

    def click(self, texto):
        if texto == "=" and self.operacion != "":
            self.operacion = re.sub(u"\u00F7", "/", self.operacion)
            self.operacion = re.sub(u"\u00D7", "*", self.operacion)
            resultado = str(eval(self.operacion))
            self.operacion = resultado
            self.limpiarPantalla()
            self.mostrarEnPantalla(resultado)
        elif texto == u"\u232B":
            self.operacion = self.operacion[0:-1]
            self.limpiarPantalla()
            self.mostrarEnPantalla(self.operacion)
        elif texto == 'C':
            self.operacion = ''
            self.limpiarPantalla()
        else:
            self.operacion += str(texto)
            self.mostrarEnPantalla(texto)
        return

    def limpiarPantalla(self):
        self.pantalla.configure(state="normal")
        self.pantalla.delete("1.0", END)
        self.pantalla.configure(state="disabled")

    def mostrarEnPantalla(self, valor):
        self.pantalla.configure(state="normal")
        self.pantalla.insert(END, valor)
        self.pantalla.configure(state="disabled")


ventana_principal = Tk()
calculadora = Interfaz(ventana_principal)
ventana_principal.mainloop()
