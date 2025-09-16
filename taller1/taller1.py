import tkinter as tk
from tkinter import ttk
import random


Ruta_del_logo = "carrito.ico"

class AdivinaNumeroApp:
    def __init__(self, master):
        self.master = master
        master.title("Adivina el Número")
        master.geometry("350x200")
        try:
            master.iconbitmap(Ruta_del_logo)
        except tk.TclError:
            print(f"No se pudo cargar el ícono desde: {Ruta_del_logo}")

        self.intentos = 0
        self.numero_secreto = 0

        # Estilo para los widgets
        self.style = ttk.Style()
        self.style.configure("TLabel", font=("Helvetica", 12))
        self.style.configure("TButton", font=("Helvetica", 10, "bold"))

        # --- Widgets ---
        self.label_instruccion = ttk.Label(master, text="Adivina un número entre 1 y 100")
        self.label_instruccion.pack(pady=10)

        self.entry_numero = ttk.Entry(master, font=("Helvetica", 12), justify=tk.CENTER)
        self.entry_numero.pack(pady=5)
        self.entry_numero.focus_set()

        self.boton_adivinar = ttk.Button(master, text="Adivinar", command=self.verificar_intento)
        self.boton_adivinar.pack(pady=5)

        self.label_resultado = ttk.Label(master, text="", style="TLabel")
        self.label_resultado.pack(pady=10)

        self.boton_reiniciar = ttk.Button(master, text="Reiniciar Juego", command=self.iniciar_juego)
        self.boton_reiniciar.pack(pady=5)

        # Iniciar el juego por primera vez
        self.iniciar_juego()

    def iniciar_juego(self):
        """Genera un nuevo número secreto y reinicia la interfaz."""
        self.numero_secreto = random.randint(1, 100)
        self.intentos = 0
        self.label_resultado.config(text="")
        self.entry_numero.delete(0, tk.END)
        self.boton_adivinar.config(state=tk.NORMAL)
        self.entry_numero.config(state=tk.NORMAL)

    def verificar_intento(self):
        """Verifica el número ingresado por el usuario."""
        try:
            intento_usuario = int(self.entry_numero.get())
            self.intentos += 1

            if intento_usuario < self.numero_secreto:
                self.label_resultado.config(text=f"¡Muy bajo! Intento #{self.intentos}")
            elif intento_usuario > self.numero_secreto:
                self.label_resultado.config(text=f"¡Muy alto! Intento #{self.intentos}")
            else:
                self.label_resultado.config(text=f"¡Correcto! Lo lograste en {self.intentos} intentos.")
                self.boton_adivinar.config(state=tk.DISABLED)
                self.entry_numero.config(state=tk.DISABLED)

        except ValueError:
            self.label_resultado.config(text="Por favor, ingresa un número válido.")
        finally:
            # Limpiar el campo de entrada después de cada intento
            self.entry_numero.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = AdivinaNumeroApp(root)
    root.mainloop()
