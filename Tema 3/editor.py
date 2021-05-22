"""

UT4-AEA3 Editor de Texto - Manejo de ficheros
Implementar nuevas funcionalidades para el editor de texto

"""

from tkinter.filedialog import askopenfilename, asksaveasfilename
import tkinter as tk
from tkinter import filedialog as FileDialog, Tk, Menu, Text, StringVar, Label, Frame
from io import open

ruta = ""  # La utilizaremos para almacenar la ruta del fichero


class TextLineNumbers(tk.Canvas):
    def __init__(self, *args, **kwargs):
        tk.Canvas.__init__(self, *args, **kwargs)
        self.textwidget = None

    def attach(self, text_widget):
        self.textwidget = text_widget

    def redraw(self, *args):
        '''redraw line numbers'''
        self.delete("all")

        i = self.textwidget.index("@0,0")
        while True:
            dline = self.textwidget.dlineinfo(i)
            if dline is None:
                break
            y = dline[1]
            linenum = str(i).split(".")[0]
            self.create_text(2, y, anchor="nw", text=linenum)
            i = self.textwidget.index("%s+1line" % i)


class CustomText(tk.Text):
    def __init__(self, *args, **kwargs):
        tk.Text.__init__(self, *args, **kwargs)

        # create a proxy for the underlying widget
        self._orig = self._w + "_orig"
        self.tk.call("rename", self._w, self._orig)
        self.tk.createcommand(self._w, self._proxy)

    def _proxy(self, *args):
        # let the actual widget perform the requested action
        cmd = (self._orig,) + args
        result = self.tk.call(cmd)

        # generate an event if something was added or deleted,
        # or the cursor position changed
        if (args[0] in ("insert", "replace", "delete") or
            args[0:3] == ("mark", "set", "insert") or
            args[0:2] == ("xview", "moveto") or
            args[0:2] == ("xview", "scroll") or
            args[0:2] == ("yview", "moveto") or
            args[0:2] == ("yview", "scroll")
            ):
            self.event_generate("<<Change>>", when="tail")

        # return what the actual widget returned
        return result


class Editor(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.text = CustomText(self)
        self.vsb = tk.Scrollbar(
            self,
            orient="vertical",
            command=self.text.yview
        )
        self.text.configure(yscrollcommand=self.vsb.set)
        self.text.tag_configure("bigfont", font=("Helvetica", "24", "bold"))
        self.linenumbers = TextLineNumbers(self, width=50)
        self.linenumbers.attach(self.text)

        self.vsb.pack(side="right", fill="y")
        self.linenumbers.pack(side="left", fill="y")
        self.text.pack(side="right", fill="both", expand=True)

        self.text.bind("<<Change>>", self._on_change)
        self.text.bind("<Configure>", self._on_change)

    def nuevo(self):
        global ruta
        mensaje.set("Nuevo fichero")
        ruta = ""
        self.text.delete(1.0, "end")
        root.title("Mi editor")

    def abrir(self):
        global ruta
        mensaje.set("Abrir fichero")
        ruta = FileDialog.askopenfilename(
            initialdir='.',
            filetypes=(("Ficheros de texto", "*.txt"),),
            title="Abrir un fichero de texto")

        if ruta != "":
            fichero = open(ruta, 'r')
            contenido = fichero.read()
            self.text.delete(1.0, 'end')
            self.text.insert('insert', contenido)
            fichero.close()
            root.title(ruta + " - Mi editor")

    def guardar(self):
        mensaje.set("Guardar fichero")
        if ruta != "":
            contenido = self.text.get(1.0, 'end-1c')
            fichero = open(ruta, 'w+')
            fichero.write(contenido)
            fichero.close()
            mensaje.set("Fichero guardado correctamente")
        else:
            self.guardar_como()

    def guardar_como(self):
        global ruta
        mensaje.set("Guardar fichero como")

        fichero = FileDialog.asksaveasfile(title="Guardar fichero",
                                           mode="w", defaultextension=".txt")

        if fichero is not None:
            ruta = fichero.name
            contenido = self.text.get(1.0, 'end-1c')
            fichero = open(ruta, 'w+')
            fichero.write(contenido)
            fichero.close()
            mensaje.set("Fichero guardado correctamente")
        else:
            mensaje.set("Guardado cancelado")
            ruta = ""

    def _on_change(self, event):
        self.linenumbers.redraw()


root = tk.Tk()
root.title("Mi editor")
editor = Editor(root)
editor.pack(side="top", fill="both", expand=True)
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Nuevo", command=editor.nuevo)
filemenu.add_command(label="Abrir", command=editor.abrir)
filemenu.add_command(label="Guardar", command=editor.guardar)
filemenu.add_command(label="Guardar como", command=editor.guardar_como)
filemenu.add_separator()
filemenu.add_command(label="Salir", command=root.quit)
menubar.add_cascade(menu=filemenu, label="Archivo")
root.config(menu=menubar)

mensaje = StringVar()
mensaje.set("Bienvenido a tu Editor")
monitor = Label(root, textvar=mensaje, justify='left')
monitor.pack(side="left")

root.mainloop()
