import pytest
from src.main import TodoApp
import tkinter as tk

@pytest.fixture
def app():
    root = tk.Tk()
    app = TodoApp(root)
    yield app
    root.destroy()

def test_agregar_tarea(app):
    """Prueba para agregar una tarea válida."""
    app.entry_tarea.insert(0, "Comprar leche")
    app.agregar_tarea()
    assert "Comprar leche" in app.tareas, "La tarea debería estar en la lista de tareas."
    assert app.lista_tareas.size() == 1, "Debería haber una tarea en la lista visual."

def test_agregar_tarea_vacia(app):
    """Prueba para evitar agregar una tarea vacía."""
    app.entry_tarea.delete(0, tk.END)
    app.agregar_tarea()
    assert len(app.tareas) == 0, "No se debería agregar una tarea vacía."

def test_eliminar_tarea(app):
    """Prueba para eliminar una tarea existente."""
    app.tareas = ["Comprar leche"]
    app.lista_tareas.insert(tk.END, "Comprar leche")
    app.lista_tareas.select_set(0)  # Seleccionar la primera tarea
    app.eliminar_tarea()
    assert "Comprar leche" not in app.tareas, "La tarea debería haber sido eliminada."
    assert app.lista_tareas.size() == 0, "No debería quedar ninguna tarea en la lista."

def test_eliminar_tarea_sin_seleccion(app):
    """Prueba para evitar eliminar una tarea si no hay selección."""
    app.tareas = ["Comprar leche"]
    app.lista_tareas.insert(tk.END, "Comprar leche")
    app.eliminar_tarea()
    assert "Comprar leche" in app.tareas, "La tarea no debería eliminarse si no se selecciona."

def test_eliminar_tarea_lista_vacia(app):
    """Prueba para manejar la eliminación cuando no hay tareas."""
    app.eliminar_tarea()
    assert len(app.tareas) == 0, "No debería fallar al intentar eliminar en una lista vacía."

def test_marcar_completa(app):
    """Prueba para marcar una tarea como completada."""
    app.tareas = ["Comprar leche"]
    app.lista_tareas.insert(tk.END, "Comprar leche")
    app.lista_tareas.select_set(0)
    app.marcar_completa()
    assert "Comprar leche - COMPLETADA" in app.tareas, "La tarea debería marcarse como completada."
    assert app.lista_tareas.get(0) == "Comprar leche - COMPLETADA", "La tarea visual debería mostrar que está completada."

def test_marcar_completa_sin_seleccion(app):
    """Prueba para evitar marcar una tarea como completada sin selección."""
    app.tareas = ["Comprar leche"]
    app.lista_tareas.insert(tk.END, "Comprar leche")
    app.marcar_completa()  # No seleccionamos ninguna tarea
    assert "Comprar leche - COMPLETADA" not in app.tareas, "No se debería marcar nada si no se selecciona una tarea."

def test_marcar_completa_lista_vacia(app):
    """Prueba para evitar marcar tareas en una lista vacía."""
    app.marcar_completa()
    assert len(app.tareas) == 0, "No debería fallar al intentar marcar como completado en una lista vacía."

def test_listar_tareas(app):
    """Prueba para verificar la consistencia en la cantidad de tareas."""
    app.agregar_tarea()
    assert app.lista_tareas.size() == len(app.tareas), "La cantidad de tareas visuales y en la lista interna debería coincidir."
