Tarea #1 de lenguajes formales
Estudiantes: Diego Alejandro Angarita Arboleda, Yan Frank Ríos López
Sistema operativo: windows 11
lenguaje de programacion: python
Numero de clase: C2566-SI2002-5730

Intrucciones:
Con el finde de brindar una mayor comodidad para correr el programa se recomienda descargar PycHarm (https://www.jetbrains.com/es-es/pycharm/download/?section=windows) o usar herramientas online como replit (https://replit.com/)

# 📘 Tarea 1 – Minimización de DFA

**Curso:** ST0270 – Lenguajes Formales y Compiladores  
**Tarea:** #1  
**Estudiantes:**  
- Diego Alejandro Angarita Arboleda  
- Yan Frank Ríos López  
**Número de clase:** C2566-SI2002-5730  
**Sistema operativo:** Windows 11  
**Lenguaje de programación:** Python 3  

---

## 📌 Descripción
Este proyecto implementa el **algoritmo de minimización de autómatas finitos deterministas (DFA)** presentado en *Kozen (1997), Lecture 14*.  
El programa recibe como entrada la definición de un DFA (sin estados inaccesibles) y determina los **estados equivalentes** que pueden ser colapsados.  
Finalmente, imprime los pares de estados equivalentes en orden lexicográfico.  

---

## 📥 Formato de Entrada
1. Una línea con un número `c > 0` indicando la cantidad de casos de prueba.  
2. Para cada caso:
   - Una línea con `n > 0`, el número de estados del DFA.  
   - Una línea con los símbolos del alfabeto separados por espacios.  
   - Una línea con los estados finales separados por espacios.  
   - `n` líneas, cada una describiendo una fila de la tabla de transiciones para un estado.  
     Los símbolos aparecen en el mismo orden que se listaron en la línea del alfabeto.  

---

## 📤 Formato de Salida
Para cada caso, el programa imprime los **pares de estados equivalentes** en orden lexicográfico.  
- Los pares se imprimen como `(p,q)` separados por espacios.  
- Si no hay pares equivalentes, se imprime una línea vacía.  

---

## ▶️ Instrucciones de Ejecución

### 1. Clonar el repositorio
```bash
git clone <tu-url-del-repo>
cd <carpeta-del-repo>
