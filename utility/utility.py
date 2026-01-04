"""Se utiliza el módulo typing para indicar explícitamente los tipos de datos esperados,
mejorando la legibilidad del código, facilitando su mantenimiento
y reduciendo posibles errores durante el desarrollo."""
from typing import Dict, List, Tuple
# -------------------------------
# UTILIDADES
# -------------------------------

def normalizar_clave(texto: str) -> str:
    """
    Normaliza texto para usarlo como clave:
    - minúsculas
    - sin espacios extra
    """
    return " ".join(texto.strip().lower().split())


def pedir_nombre_valido(mensaje: str) -> str:
    """
    Pide un nombre completo válido:
    - Solo letras y espacios
    - Permite guiones y apóstrofes: Pérez-García, O'Connor
    - No permite números ni símbolos raros
    """
    while True:
        nombre = input(mensaje).strip()

        if not nombre:
            print("⚠️ El nombre no puede estar vacío.")
            continue
        # Permitimos letras, espacios, guiones y apóstrofes
        if not all(c.isalpha() or c.isspace() or c in "-'" for c in nombre):
            print("⚠️ El nombre solo puede contener letras, espacios y - '")
            continue

        return nombre


def formatear_apellidos_nombre(nombre_completo: str, num_apellidos: int = 2) -> str:
    """
    Devuelve el nombre en formato: 'Apellidos, Nombre'.
    Soporta nombres y apellidos compuestos.

    num_apellidos:
        - 1 -> último apellido
        - 2 -> dos últimos apellidos (por defecto)
    """
    partes = nombre_completo.split()

    # Si no hay suficientes palabras, se devuelve tal cual
    if len(partes) <= num_apellidos:
        return nombre_completo

    nombre = " ".join(partes[:-num_apellidos]).capitalize()
    apellidos = " ".join(partes[-num_apellidos:]).capitalize()

    return f"{apellidos}, {nombre}"


def pedir_texto_no_vacio(mensaje: str) -> str:
    """
    Pide texto al usuario hasta que no esté vacío.
    """
    while True:
        texto = input(mensaje).strip()
        if texto:
            return texto
        print("⚠️ No puede estar vacío. Inténtalo de nuevo.")


def pedir_float_positivo(mensaje: str) -> float:
    """
    Pide un número float >= 0 validando entrada.
    Admite coma o punto.
    """
    while True:
        entrada = input(mensaje).strip().replace(",", ".")
        try:
            valor = float(entrada)
            if valor < 0:
                print("⚠️ El valor no puede ser negativo.")
                continue
            return valor
        except ValueError:
            print("⚠️ Número inválido. Ejemplo válido: 12.50")


def contar_vocales(texto: str) -> int:
    """
    Cuenta vocales (incluye tildes y ü).
    Se utiliza un conjunto (set) para almacenar las vocales
    y se recorre el texto contando aquellas que pertenecen a dicho conjunto,
    optimizando el rendimiento de la comprobación.
    """
    vocales = set("aeiouáéíóúüAEIOUÁÉÍÓÚÜ")
    return sum(1 for c in texto if c in vocales)

def pedir_letra_valida(mensaje: str) -> str:
    """
    Pide una sola letra válida:
    - No vacía
    - Solo una letra
    - No permite números ni símbolos
    """
    while True:
        entrada = input(mensaje).strip()

        if not entrada:
            print("⚠️ Debes introducir una letra.")
            continue

        if len(entrada) != 1:
            print("⚠️ Introduce solo una letra.")
            continue

        if not entrada.isalpha():
            print("⚠️ Solo se permiten letras.")
            continue

        return entrada.lower()



def filtrar_productos_por_letra(productos: List[str], letra: str) -> Tuple[List[str], int]:
    """
    Filtra los productos que comienzan por una letra dada.

    Devuelve:
    - Lista de productos que comienzan por esa letra
    - Número total de coincidencias
    """
    letra = letra.lower()

    productos_filtrados = [
        p for p in productos
        if p.strip().lower().startswith(letra)
    ]

    return productos_filtrados, len(productos_filtrados)
