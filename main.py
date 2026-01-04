

"""
Versión :
- Menú interactivo
- Validaciones básicas
- Salida formateada
- Código modular (funciones)
- Comentarios claros y variables descriptivos

Mejoras aplicadas:
1) Diccionarios: búsqueda case-insensitive (normalización de claves)
2) Nombres: permitir guiones y apóstrofes (Pérez-García, O'Connor)
3) Listas: evitar duplicados + limpiar formato (title)
4) Menú: aceptar 'salir/exit/q' además de 0
5) Estilo: unificar docstring inicial (evitar strings sueltos)
6) Nombres: formato 'Apellidos, Nombre' con función dedicada
7) Se implementan dos filtros: uno fijo para la letra “A” y otro dinámico introducido por el usuario,
reutilizando la misma función de filtrado para evitar duplicación de código.
8) Modulo typing: se añaden anotaciones de tipo para mejorar la legibilidad y mantenimiento del código.
9) Se amplía la entrada de datos del nombre para mejorar la fiabilidad del tratamiento de apellidos,
permitiendo tanto una introducción automática como manual.
"""

"""Se utiliza el módulo typing para indicar explícitamente los tipos de datos esperados, 
mejorando la legibilidad del código, facilitando su mantenimiento
y reduciendo posibles errores durante el desarrollo."""

from typing import Dict, List, Tuple
from functions.functions import *
from utility.utility import *
# -------------------------------
# MENÚ PRINCIPAL
# -------------------------------

def mostrar_menu() -> None:
    print("\n====================================")
    print("   MENÚ - Procesamiento de datos")
    print("====================================")
    print("1. Cadenas de caracteres")
    print("2. Listas")
    print("3. Tuplas")
    print("4. Diccionarios")
    print("5. Ejecutar TODO")
    print("0. Salir (o escribe: salir / exit / q)")


def main() -> None:
    """
    Programa principal con menú.
    Reutilizamos la lista de productos para alimentar el diccionario.
    """
    productos_guardados: List[str] = ["Ordenador", "Montaje", "Auriculares", "Monitor", "Teclado"]

    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ").strip().lower()

        # Mejora: permitir comandos de salida
        if opcion in ("salir", "exit", "q"):
            opcion = "0"

        if opcion == "1":
            bloque_cadenas()

        elif opcion == "2":
            productos_guardados = bloque_listas()

        elif opcion == "3":
            bloque_tuplas()

        elif opcion == "4":
            bloque_diccionarios(productos_guardados)

        elif opcion == "5":
            bloque_cadenas()
            productos_guardados = bloque_listas()
            bloque_tuplas()
            bloque_diccionarios(productos_guardados)

        elif opcion == "0":
            print("Saliendo... 👋")
            break

        else:
            print("⚠️ Opción inválida. Elige un número del menú.")


if __name__ == "__main__":
    main()