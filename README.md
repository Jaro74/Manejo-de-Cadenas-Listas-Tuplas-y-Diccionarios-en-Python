# 📦 Actividad Unidad 4 – Estructuras de Datos en Python

## 📖 Descripción
Este proyecto corresponde a la **Actividad de la Unidad 4** de la asignatura de **Programación** del ciclo **FP DAM**.  
El objetivo es desarrollar un programa en Python que procese datos de clientes y productos utilizando las principales **estructuras de datos** del lenguaje, aplicando buenas prácticas de programación y validación de datos.

El programa simula un **entorno real de empresa a nivel junior**, incorporando modularidad, reutilización de funciones y control de errores.

---

## 🎯 Objetivos
- Utilizar correctamente:
  - Cadenas de caracteres
  - Listas
  - Tuplas
  - Diccionarios
- Validar la entrada de datos del usuario
- Aplicar programación modular
- Mejorar la claridad, robustez y mantenibilidad del código

---

## 🗂️ Estructura del proyecto

```text
ActivityUnit4/
│
├── main.py # Punto de entrada del programa
│
├── functions/
│ ├── init.py
│ ├── functions.py/
│ │ ├── cadenas # Operaciones con cadenas
│ │ ├── listas # Gestión de listas de productos
│ │ ├── tuplas # Operaciones con tuplas
│ │ └── diccionarios # Gestión de productos y precios
│ │
├── utility/
│ ├── init.py
│ └── utility.py # Funciones de validación reutilizables
│
└── .venv/ # Entorno virtual

```

---

## 🧩 Funcionalidades principales

### 🔤 Cadenas de caracteres
- Introducción del nombre de dos formas:
  - Nombre completo
  - Nombre y apellidos por separado (más fiable)
- Formateo del nombre:
  - Formato título
  - Orden invertido
  - Formato **Apellidos, Nombre**
- Conteo de vocales
- Validación de caracteres permitidos

---

### 📋 Listas
- Creación de una lista de productos
- Ordenación alfabética
- Inserción y eliminación de elementos
- Filtros de productos:
  - Filtro fijo por la letra **A**
  - Filtro dinámico por letra introducida por el usuario
- Conteo de coincidencias

---

### 🔐 Tuplas
- Definición de códigos de productos
- Comprobación de existencia de un código
- Uso de *slicing* para mostrar rangos

---

### 🗃️ Diccionarios
- Gestión de productos y precios
- Consulta de precios por nombre
- Alta y baja de productos
- Mejora aplicada:
  - Búsqueda **independiente de mayúsculas/minúsculas**

---

## 🛡️ Validaciones y buenas prácticas
- Validación de:
  - Nombres y apellidos
  - Letras individuales
  - Precios numéricos
- Uso de funciones reutilizables
- Anotaciones de tipo con `typing`
- Código comentado y modular
- Control de errores comunes

---

## ▶️ Ejecución del programa

1. Abrir el proyecto en PyCharm (o editor compatible)
2. Ejecutar el archivo:```bash
python main.py ```

3. Navegar por el menú interactivo para probar las distintas funcionalidades.



---

## 🧠 Mejoras implementadas
Entrada flexible del nombre para evitar errores con apellidos simples o compuestos

Normalización de datos para búsquedas más robustas

Separación del código en módulos

Mayor claridad y experiencia de usuario

---
## ✅ Conclusión
Este proyecto cumple los objetivos de la unidad, aplicando correctamente las estructuras de datos en Python y simulando un entorno real de desarrollo.
Las mejoras añadidas aumentan la fiabilidad, claridad y calidad del programa, siguiendo buenas prácticas de programación.

### 👨‍🎓 Autor
Alumno: Emilio Javier Iniesta Laliga

Curso: FP DAM

Asignatura: Programación Python

