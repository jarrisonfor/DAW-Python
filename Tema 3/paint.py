"""
UT4-AEA2 Paint - Canvas
Implementar nuevas funcionalidades para la herramienta de dibujo

"""
from tkinter import Tk, Button, Scale, Canvas, RAISED, SUNKEN, ROUND, TRUE, HORIZONTAL, PhotoImage
from tkinter.colorchooser import askcolor


class Paint(object):

    DEFAULT_PEN_SIZE = 5.0
    DEFAULT_COLOR = 'black'

    def __init__(self):
        self.root = Tk()

        self.pen_button = Button(self.root, text='Lápiz', command=self.use_pen)
        self.pen_button.grid(row=1, column=0, padx=5, pady=5)

        self.brush_button = Button(
            self.root, text='Pincel', command=self.use_brush)
        self.brush_button.grid(row=1, column=1, padx=5, pady=5)

        self.color_button = Button(
            self.root, text='Color', command=self.choose_color)
        self.color_button.grid(row=1, column=2, padx=5, pady=5)

        self.eraser_button = Button(
            self.root, text='Goma', command=self.use_eraser)
        self.eraser_button.grid(row=1, column=3, padx=5, pady=5)

        self.limpiar_button = Button(
            self.root, text='Limpiar', command=self.usar_borrar_todo)
        self.limpiar_button.grid(row=1, column=4, padx=5, pady=5)

        self.choose_size_button = Scale(
            self.root, from_=1, to=15, orient=HORIZONTAL)
        self.choose_size_button.grid(row=1, column=5, padx=5, pady=5)

        self.c = Canvas(self.root, bg='white', width=600, height=600)
        self.c.grid(column=0, row=0, columnspan=6, padx=2, pady=2)
        self.c.config(cursor="tcross")

        self.setup()
        self.root.mainloop()

    def setup(self):
        self.old_x = None
        self.old_y = None
        self.line_width = self.choose_size_button.get()
        self.color = self.DEFAULT_COLOR
        self.eraser_on = False
        self.active_button = self.pen_button
        self.c.bind('<B1-Motion>', self.paint)  # Pintar en el lienzo
        self.c.bind('<ButtonRelease-1>', self.reset)

    def use_pen(self):
        self.activate_button(self.pen_button)

    def use_brush(self):
        self.activate_button(self.brush_button)

    def usar_borrar_todo(self):
        self.c.delete("all")

    def choose_color(self):
        self.eraser_on = False
        color = askcolor(color=self.color)[1]
        if color != None:
            self.color = color
        else:
            return None

    def use_eraser(self):
        self.activate_button(self.eraser_button, eraser_mode=True)

    def activate_button(self, some_button, eraser_mode=False):
        self.active_button.config(relief=RAISED)
        some_button.config(relief=SUNKEN)
        self.active_button = some_button
        self.eraser_on = eraser_mode

    def paint(self, event):
        self.line_width = self.choose_size_button.get()
        paint_color = 'white' if self.eraser_on else self.color
        if self.old_x and self.old_y:
            self.c.create_line(self.old_x, self.old_y, event.x, event.y,
                               width=self.line_width, fill=paint_color,
                               capstyle=ROUND, smooth=TRUE, splinesteps=36)
        self.old_x = event.x
        self.old_y = event.y

    def reset(self, event):
        self.old_x, self.old_y = None, None


Paint()
