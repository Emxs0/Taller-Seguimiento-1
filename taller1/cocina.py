import tkinter as tk
from tkinter import messagebox, ttk

Ruta_del_logo = "letmecook.ico"

# --- Clases de Modelo de Datos ---
# Clase Receta para almacenar nombre y lista de ingredientes
class Receta:
    def __init__(self, nombre, ingredientes):
        self.nombre = nombre
        self.ingredientes = ingredientes

# Clase GestorRecetas para gestionar las recetas
class GestorRecetas:
    def __init__(self):
        self.recetas = []

    def agregar_receta(self, nombre, ingredientes):
        receta = Receta(nombre, ingredientes)
        self.recetas.append(receta)

    def eliminar_receta(self, indice):
        try:
            receta_eliminada = self.recetas.pop(indice)
            return receta_eliminada.nombre
        except IndexError:
            return None

# --- Clase Principal de la Aplicación ---
class RecetasApp:
    def __init__(self, master):
        self.master = master
        master.title("Gestor de Recetas")
        master.geometry("350x400")

        # Configuracion del icono
        try:
            master.iconbitmap(Ruta_del_logo)
        except tk.TclError:
            print(f"Advertencia: No se pudo cargar el icono desde la ruta: {Ruta_del_logo}")

        # Instancia del gestor de recetas
        self.gestor = GestorRecetas()

        # --- Creación del Menú ---
        barra_menu = tk.Menu(master)
        master.config(menu=barra_menu)

        # Menú de Ayuda
        menu_ayuda = tk.Menu(barra_menu, tearoff=0)
        barra_menu.add_cascade(label="Ayuda", menu=menu_ayuda)
        menu_ayuda.add_command(label="Cómo usar...", command=self.mostrar_ayuda)

        # --- Creación de Widgets ---
        # Frame principal para organizar los widgets
        main_frame = ttk.Frame(master, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Etiquetas y entradas para el nombre y los ingredientes
        ttk.Label(main_frame, text="Nombre de la receta:").pack(fill=tk.X, pady=(0, 2))
        self.entry_nombre = ttk.Entry(main_frame)
        self.entry_nombre.pack(fill=tk.X, pady=(0, 10))

        ttk.Label(main_frame, text="Ingredientes (separados por coma):").pack(fill=tk.X, pady=(0, 2))
        self.entry_ingredientes = ttk.Entry(main_frame)
        self.entry_ingredientes.pack(fill=tk.X, pady=(0, 10))

        # Botón para agregar receta
        self.btn_agregar = ttk.Button(main_frame, text="Agregar receta", command=self.agregar_receta)
        self.btn_agregar.pack(fill=tk.X, pady=5)

        # Listbox para mostrar las recetas guardadas
        self.listbox_recetas = tk.Listbox(main_frame, height=6)
        self.listbox_recetas.pack(fill=tk.BOTH, expand=True, pady=5)

        # Botones para ver y eliminar recetas
        self.btn_ver = ttk.Button(main_frame, text="Ver ingredientes", command=self.ver_ingredientes)
        self.btn_ver.pack(fill=tk.X, pady=(5, 2))

        self.btn_eliminar = ttk.Button(main_frame, text="Eliminar receta", command=self.eliminar_receta)
        self.btn_eliminar.pack(fill=tk.X, pady=(2, 5))

    # Función para agregar una nueva receta
    def agregar_receta(self):
        nombre = self.entry_nombre.get().strip()
        # Limpia los ingredientes de espacios en blanco y filtra los vacíos
        ingredientes = [ing.strip() for ing in self.entry_ingredientes.get().split(",") if ing.strip()]
        
        if nombre and ingredientes:
            self.gestor.agregar_receta(nombre, ingredientes)
            self.listbox_recetas.insert(tk.END, nombre)
            self.entry_nombre.delete(0, tk.END)
            self.entry_ingredientes.delete(0, tk.END)
            messagebox.showinfo("Receta agregada", f"La receta '{nombre}' ha sido agregada.")
        else:
            messagebox.showwarning("Error", "Por favor, ingrese un nombre y al menos un ingrediente.")

    # Función para mostrar los ingredientes de una receta seleccionada
    def ver_ingredientes(self):
        seleccion = self.listbox_recetas.curselection()
        if seleccion:
            indice = seleccion[0]
            receta = self.gestor.recetas[indice]
            ingredientes = ", ".join(receta.ingredientes)
            messagebox.showinfo(f"Ingredientes de {receta.nombre}", f"{ingredientes}")
        else:
            messagebox.showwarning("Error", "Seleccione una receta para ver sus ingredientes.")

    # Función para eliminar una receta seleccionada
    def eliminar_receta(self):
        seleccion = self.listbox_recetas.curselection()
        if seleccion:
            indice = seleccion[0]
            nombre = self.gestor.eliminar_receta(indice)
            if nombre:
                self.listbox_recetas.delete(indice)
                messagebox.showinfo("Receta eliminada", f"La receta '{nombre}' ha sido eliminada.")
            else:
                messagebox.showerror("Error", "No se pudo eliminar la receta.")
        else:
            messagebox.showwarning("Error", "Seleccione una receta para eliminar.")

    # Función para mostrar la ayuda
    def mostrar_ayuda(self):
        ayuda_texto = """
Cómo usar el Gestor de Recetas:

1.  **Agregar una receta:**
    -   Escribe el nombre de la receta en el primer campo.
    -   Escribe los ingredientes en el segundo campo, separados por comas (ej: tomate, cebolla, ajo).
    -   Haz clic en "Agregar receta".

2.  **Ver ingredientes:** Selecciona una receta de la lista y haz clic en "Ver ingredientes".

3.  **Eliminar una receta:** Selecciona una receta de la lista y haz clic en "Eliminar receta".
"""
        messagebox.showinfo("Ayuda - Gestor de Recetas", ayuda_texto)
if __name__ == "__main__":
    # Crear la ventana principal y la aplicación
    root = tk.Tk()
    app = RecetasApp(root)
    # Iniciar el bucle principal de la ventana
    root.mainloop()
