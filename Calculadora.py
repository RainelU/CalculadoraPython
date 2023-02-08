import tkinter as tk
from tkinter import ttk, messagebox

class Calculadora(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('400x450')
        self.title('Calculadora')
        self.resizable(0,0)
        self.iconbitmap('assets/calculadora.ico')
        # Atributos de clase
        self.expresion = ''
        #Caja de texto
        self.entrada = None
        # StringVar utilizar para obtener el valor del input
        self.entrada_texto = tk.StringVar()

        # Creamos los componentes encapsulado
        self._crearComponentes()
        self.mainloop()

    def _eventoLimpiar(self):
        self.expresion = ''
        self.entrada_texto.set(self.expresion)

    def _eventoClic(self, elemento):
        # Concatenamos el elemento a la expresion existente
        self.expresion = f'{self.expresion}{elemento}'

        if elemento == '+' or elemento == '-' or elemento == '/' or elemento == '*':
            self.entrada_texto.set('')
        else:
            self.entrada_texto.set(self.expresion)

    def _eventoEvaluar(self):
        # Concatenamos el elemento a la expresion existente
        try:
            resultado = str(eval(self.expresion))
            self.entrada_texto.set(resultado)
            self.expresion = resultado
        except Exception as e:
            self.entrada_texto.set('ERROR VALORES')

    def _eventoBorrar(self):
        texto = ""
        if len(self.expresion) > 0:
            texto = self.expresion[:-1]

        self.expresion = texto
        self.entrada_texto.set(self.expresion)

    def _crearComponentes(self):
        caja_resultados = tk.Frame(self, width=400, height=50, bg='grey')
        caja_resultados.pack(side=tk.TOP)

        # Cajas de Texto
        caja_texto= tk.Entry(caja_resultados,
                                 fg='black',
                                 font=('Arial', 30, 'bold'),
                                 textvariable=self.entrada_texto,
                                 width=18,
                                 justify=tk.RIGHT,
                                 state=tk.DISABLED,
                                 cursor='x_cursor'
                             )

        caja_texto.grid(row=0, column=0, ipady=16, sticky="NSWE")

        botones_frame = tk.Frame(self, width=400, height=450, bg='grey')
        botones_frame.pack()

        # First Row
        tk.Button(botones_frame,
                  text="C", width=28, height=4, bd=0, bg='#eee', cursor='hand2', command=self._eventoLimpiar
                  ).grid(row=0, column=0, columnspan=2, padx=1, pady=1)
        tk.Button(botones_frame,
                  text='⌫',width=13,height=4, bd=0,bg='#eee',cursor='hand2',command=self._eventoBorrar
                  ).grid(row=0, column=2, padx=1, pady=1)
        tk.Button(botones_frame,
                  text='/',width=13,height=4, bd=0,bg='#eee',cursor='hand2',command=lambda: self._eventoClic('/')
                  ).grid(row=0, column=3, padx=1, pady=1)

        # Second Row
        tk.Button(botones_frame,
                  text='7', width=10, height=3, bd=0, bg='#fff', cursor='hand2', command=lambda: self._eventoClic(7), font=('Arial', 13)
                  ).grid(row=1, column=0, padx=1, pady=1)
        tk.Button(botones_frame,
                  text='8', width=11, height=3, bd=0, bg='#fff', cursor='hand2', command=lambda: self._eventoClic(8), font=('Arial', 13)
                  ).grid(row=1, column=1, pady=1)
        tk.Button(botones_frame,
                  text='9', width=10, height=3, bd=0, bg='#fff', cursor='hand2', command=lambda: self._eventoClic(9), font=('Arial', 13)
                  ).grid(row=1, column=2, padx=1, pady=1)
        tk.Button(botones_frame,
                  text='*', width=10, height=3, bd=0, bg='#eee', cursor='hand2', command=lambda: self._eventoClic('*'), font=('Arial', 13)
                  ).grid(row=1, column=3)

        # Third Row
        tk.Button(botones_frame,
                  text='4', width=10, height=3, bd=0, bg='#fff', cursor='hand2', command=lambda: self._eventoClic(4), font=('Arial', 13)
                  ).grid(row=2, column=0, padx=1, pady=1)
        tk.Button(botones_frame,
                  text='5', width=11, height=3, bd=0, bg='#fff', cursor='hand2', command=lambda: self._eventoClic(5), font=('Arial', 13)
                  ).grid(row=2, column=1, pady=1)
        tk.Button(botones_frame,
                  text='6', width=10, height=3, bd=0, bg='#fff', cursor='hand2', command=lambda: self._eventoClic(6), font=('Arial', 13)
                  ).grid(row=2, column=2, padx=1, pady=1)
        tk.Button(botones_frame,
                  text='-', width=10, height=3, bd=0, bg='#eee', cursor='hand2', command=lambda: self._eventoClic('-'), font=('Arial', 13)
                  ).grid(row=2, column=3)

        # Fourth Row
        tk.Button(botones_frame,
                  text='1', width=10, height=3, bd=0, bg='#fff', cursor='hand2', command=lambda: self._eventoClic(1),
                  font=('Arial', 13)
                  ).grid(row=3, column=0, padx=1, pady=1)
        tk.Button(botones_frame,
                  text='2', width=11, height=3, bd=0, bg='#fff', cursor='hand2', command=lambda: self._eventoClic(2),
                  font=('Arial', 13)
                  ).grid(row=3, column=1, pady=1)
        tk.Button(botones_frame,
                  text='3', width=10, height=3, bd=0, bg='#fff', cursor='hand2', command=lambda: self._eventoClic(3),
                  font=('Arial', 13)
                  ).grid(row=3, column=2, padx=1, pady=1)
        tk.Button(botones_frame,
                  text='+', width=10, height=3, bd=0, bg='#eee', cursor='hand2', command=lambda: self._eventoClic('+'),
                  font=('Arial', 13)
                  ).grid(row=3, column=3)

        # fifth Row
        tk.Button(botones_frame,
                  text='0', width=22, height=3, bd=0, bg='#fff', cursor='hand2', command=lambda: self._eventoClic(0),
                  font=('Arial', 13)
                  ).grid(row=4, column=0, columnspan=2, padx=1, pady=1)
        tk.Button(botones_frame,
                  text='.', width=10, height=3, bd=0, bg='#eee', cursor='hand2', command=lambda: self._eventoClic('.'),
                  font=('Arial', 13)
                  ).grid(row=4, column=2, padx=1, pady=1)
        tk.Button(botones_frame,
                  text='=', width=10, height=3, bd=0, bg='#eee', cursor='hand2', command=self._eventoEvaluar,
                  font=('Arial', 13)
                  ).grid(row=4, column=3, padx=1, pady=1)


if __name__ == '__main__':
    calculadora = Calculadora()