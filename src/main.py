import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Tareas")
        self.root.geometry("400x400")
        
        self.tareas = []

        # Label
        self.label = tk.Label(root, text="Lista de Tareas", font=("Arial", 14))
        self.label.pack(pady=10)

        # Cuadro de texto para ingresar tareas
        self.entry_tarea = tk.Entry(root, width=40)
        self.entry_tarea.pack(pady=10)

        # Botón para agregar tarea
        self.boton_agregar = tk.Button(root, text="Agregar Tarea", command=self.agregar_tarea)
        self.boton_agregar.pack(pady=10)

        # Lista de tareas (Listbox)
        self.lista_tareas = tk.Listbox(root, width=50, height=10)
        self.lista_tareas.pack(pady=10)

        # Botones para eliminar y completar tareas
        self.boton_eliminar = tk.Button(root, text="Eliminar Tarea", command=self.eliminar_tarea)
        self.boton_eliminar.pack(pady=10)

        self.boton_completar = tk.Button(root, text="Marcar Como Completa", command=self.marcar_completa)
        self.boton_completar.pack(pady=10)

    def agregar_tarea(self):
        tarea = self.entry_tarea.get()
        if tarea:
            self.tareas.append(tarea)
            self.lista_tareas.insert(tk.END, tarea)
            self.entry_tarea.delete(0, tk.END)
        else:
            messagebox.showwarning("Entrada vacía", "Debes escribir una tarea para agregar.")

    def eliminar_tarea(self):
        try:
            tarea_index = self.lista_tareas.curselection()[0]
            tarea = self.lista_tareas.get(tarea_index)
            self.lista_tareas.delete(tarea_index)
            self.tareas.remove(tarea)
        except IndexError:
            messagebox.showwarning("Sin selección", "Debes seleccionar una tarea para eliminar.")

    def marcar_completa(self):
        try:
            tarea_index = self.lista_tareas.curselection()[0]
            tarea = self.lista_tareas.get(tarea_index)
            tarea_completa = f"{tarea} - COMPLETADA"
            self.lista_tareas.delete(tarea_index)
            self.lista_tareas.insert(tarea_index, tarea_completa)
            self.tareas[tarea_index] = tarea_completa
        except IndexError:
            messagebox.showwarning("Sin selección", "Debes seleccionar una tarea para marcar como completa.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()