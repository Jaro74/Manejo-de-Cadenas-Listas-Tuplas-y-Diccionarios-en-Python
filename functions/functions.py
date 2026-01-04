from utility.utility import *
"""Se utiliza el módulo typing para indicar explícitamente los tipos de datos esperados, 
mejorando la legibilidad del código, facilitando su mantenimiento
y reduciendo posibles errores durante el desarrollo."""
from typing import Dict, List, Tuple

# -------------------------------
# 1) CADENAS
# -------------------------------

def bloque_cadenas() -> None:
    """
    - Permite 2 modos:
      1) Introducir nombre completo (separación automática por convención)
      2) Introducir nombre y apellidos por separado (más fiable)
    - Formato título
    - Contar vocales
    - Invertir el orden de las palabras
    - Mostrar 'Apellidos, Nombre'
    """
    print("\n==============================")
    print("1) CADENAS DE CARACTERES")
    print("==============================")
    print("¿Cómo quieres introducir los datos?")
    print("1. Nombre completo (separación automática de apellidos)")
    print("2. Nombre y apellidos por separado (recomendado)")

    opcion = input("Elige 1 o 2: ").strip()

    # Variables que siempre vamos a rellenar
    nombre_completo = ""
    nombre_apellidos = ""

    if opcion == "2":
        # ✅ Modo fiable: el usuario separa nombre y apellidos
        nombre = pedir_nombre_valido("Introduce tu nombre: ")
        apellidos = pedir_nombre_valido("Introduce tus apellidos: ")

        nombre_completo = f"{nombre} {apellidos}".strip()
        # Formato seguro: Apellidos, Nombre
        nombre_apellidos = f"{apellidos.title()}, {nombre.title()}"

    else:
        # ✅ Modo rápido: nombre completo + separación por convención
        # (si mete 1 palabra, no se puede separar apellidos)
        nombre_completo = pedir_nombre_valido("Introduce tu nombre completo: ")
        nombre_completo = " ".join(nombre_completo.split())  # limpia espacios dobles

        if len(nombre_completo.split()) < 2:
            # No se puede construir "Apellidos, Nombre" con 1 palabra
            nombre_apellidos = "No se puede determinar (faltan apellidos)."
        else:
            # Para hacerlo más claro, preguntamos si tiene 1 o 2 apellidos
            tiene_dos = input("¿Tienes dos apellidos? (s/n): ").strip().lower()
            num_apellidos = 2 if tiene_dos in ("s", "si", "sí") else 1

            nombre_apellidos = formatear_apellidos_nombre(nombre_completo, num_apellidos)

    # Operaciones comunes (se aplican siempre al nombre completo)
    nombre_titulo = nombre_completo.title()
    numero_vocales = contar_vocales(nombre_completo)

    palabras = nombre_completo.split()
    nombre_invertido = " ".join(reversed(palabras))

    print("\n--- RESULTADOS ---")
    print(f"Nombre en formato título: {nombre_titulo}")
    print(f"Número de vocales: {numero_vocales}")
    print(f"Nombre invertido (por palabras): {nombre_invertido}")
    print(f"Formato Apellidos, Nombre: {nombre_apellidos}")


# -------------------------------
# 2) LISTAS
# -------------------------------

def bloque_listas() -> List[str]:
    """
    - Crear lista de 5 productos
    - Mostrar ordenada
    - Añadir producto (sin duplicados)
    - Eliminar el tercero
    - Mostrar los que empiezan por 'A'
    """
    print("\n==============================")
    print("2) LISTAS")
    print("==============================")

    productos: List[str] = ["Ordenador", "Montaje", "Auriculares", "Monitor", "Teclado"]

    print("\nLista original:")
    print(productos)

    print("\nLista ordenada alfabéticamente (sin modificar la original):")
    print(sorted(productos))

    # Mejora: limpiar y formatear el nuevo producto + evitar duplicados
    nuevo_producto = pedir_texto_no_vacio("\nIntroduce un producto nuevo para añadir: ").strip().title()

    if nuevo_producto in productos:
        print("⚠️ Ese producto ya existe. No se añadirá duplicado.")
    else:
        productos.append(nuevo_producto)

    # Eliminar el 3º elemento (índice 2) si existe
    if len(productos) >= 3:
        eliminado = productos.pop(2)
        print(f"\n✅ Eliminado el 3er producto (índice 2): {eliminado}")

    print("\nLista final tras cambios:")
    print(productos)

    """
    Se comprueba si la lista resultante está vacía para mostrar un mensaje informativo al usuario 
    en lugar de una lista vacía, mejorando la experiencia de uso
    Se encapsula la lógica de filtrado en una función reutilizable que devuelve 
    tanto los elementos encontrados como su número total, mejorando la modularidad y el mantenimiento del código.
    """
    # --- FILTRO FIJO: productos que comienzan por 'A' ---
    productos_con_a, total_con_a = filtrar_productos_por_letra(productos, "a")

    print("\nProductos que comienzan por 'A':")

    if productos_con_a:
        print(productos_con_a)
        print(f"Total de productos que comienzan por 'A': {total_con_a}")
    else:
        print("No hay productos que comiencen por la letra 'A'.")
        print("Total de productos que comienzan por 'A': 0")

    # --- FILTRO DINÁMICO: letra introducida por el usuario ---
    letra = pedir_letra_valida("\nIntroduce una letra para filtrar productos: ")

    productos_filtrados, total = filtrar_productos_por_letra(productos, letra)

    print(f"\nProductos que comienzan por '{letra.upper()}':")

    if productos_filtrados:
        print(productos_filtrados)
        print(f"Total de productos que comienzan por '{letra.upper()}': {total}")
    else:
        print(f"No hay productos que comiencen por la letra '{letra.upper()}'.")
        print(f"Total de productos que comienzan por '{letra.upper()}': 0")

    return productos


# -------------------------------
# 3) TUPLAS
# -------------------------------

def bloque_tuplas() -> None:
    """
    - Definir tupla de códigos
    - Verificar si código existe
    - Mostrar del 2º al 4º
    """
    print("\n==============================")
    print("3) TUPLAS")
    print("==============================")

    codigos: Tuple[str, ...] = ("P001", "P002", "P003", "P004", "P005")
    print(f"\nCódigos disponibles: {codigos}")

    codigo_usuario = pedir_texto_no_vacio("Introduce un código (ej. P003): ").upper()
    existe = codigo_usuario in codigos

    print(f"\n¿Existe {codigo_usuario}? -> {existe}")

    # Del segundo al cuarto (índices 1..3)
    print(f"Códigos del 2º al 4º: {codigos[1:4]}")


# -------------------------------
# 4) DICCIONARIOS
# -------------------------------

def crear_diccionario_precios(productos: List[str]) -> Dict[str, Dict[str, float]]:
    """
    Crea un diccionario con clave normalizada (case-insensitive) y guarda:
    - nombre_original (para mostrar bonito)
    - precio
    """
    precios_base = [899.00, 59.90, 29.99, 179.95, 24.50, 12.00, 75.00]
    precios: Dict[str, Dict[str, float]] = {}

    for i, producto in enumerate(productos):
        clave = normalizar_clave(producto)
        precio = precios_base[i] if i < len(precios_base) else 10.0

        precios[clave] = {
            "nombre_original": producto.strip(),
            "precio": precio
        }

    return precios


def bloque_diccionarios(productos: List[str]) -> None:
    """
    - Crear diccionario producto->precio (case-insensitive)
    - Consultar precio por nombre
    - Añadir producto con precio
    - Eliminar otro producto
    """
    print("\n==============================")
    print("4) DICCIONARIOS")
    print("==============================")

    precios_productos = crear_diccionario_precios(productos)

    print("\nDiccionario inicial (producto -> precio):")
    for info in precios_productos.values():
        print(f" - {info['nombre_original']}: {info['precio']:.2f} €")

    # Consulta (da igual mayúsculas/minúsculas)
    producto_consulta = pedir_texto_no_vacio("\n¿De qué producto quieres ver el precio?: ")
    clave_consulta = normalizar_clave(producto_consulta)

    info = precios_productos.get(clave_consulta)
    if info is None:
        print("❌ Ese producto no está registrado.")
    else:
        print(f"✅ Precio de '{info['nombre_original']}': {info['precio']:.2f} €")

    # Añadir nuevo producto (guardando clave normalizada)
    nuevo_nombre = pedir_texto_no_vacio("\nNombre del nuevo producto a añadir: ").strip().title()
    nuevo_precio = pedir_float_positivo(f"Precio de '{nuevo_nombre}': ")
    clave_nueva = normalizar_clave(nuevo_nombre)

    precios_productos[clave_nueva] = {
        "nombre_original": nuevo_nombre,
        "precio": nuevo_precio
    }
    print("✅ Producto añadido correctamente.")

    # Eliminar producto (da igual mayúsculas/minúsculas)
    producto_eliminar = pedir_texto_no_vacio("Nombre de un producto a eliminar: ")
    clave_eliminar = normalizar_clave(producto_eliminar)

    if clave_eliminar in precios_productos:
        eliminado = precios_productos[clave_eliminar]["nombre_original"]
        del precios_productos[clave_eliminar]
        print(f"✅ Producto eliminado: {eliminado}")
    else:
        print("❌ No existe ese producto, no se eliminó nada.")

    print("\nDiccionario final (producto -> precio):")
    for info in precios_productos.values():
        print(f" - {info['nombre_original']}: {info['precio']:.2f} €")
