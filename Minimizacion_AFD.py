def minimize_automaton(n_states, alphabet, final_states, transitions):
    # Paso 1: Crear tabla de pares (representada como diccionario)
    # marked[i][j] = True si los estados i,j están marcados como no equivalentes
    marked = {}
    for i in range(n_states):
        marked[i] = {}  
        for j in range(i + 1, n_states):
            marked[i][j] = False
    
    # Paso 2: Marcado inicial - marcar pares donde uno es final y otro no
    for i in range(n_states):
        for j in range(i + 1, n_states):
            if (i in final_states) != (j in final_states):
                marked[i][j] = True
    
    # Paso 3: Marcado iterativo
    changed = True
    while changed:
        changed = False
        
        # Revisar todos los pares no marcados
        for i in range(n_states):
            for j in range(i + 1, n_states):
                if not marked[i][j]:  # Si el par no está marcado
                    
                    # Revisar cada símbolo del alfabeto
                    for symbol_idx, symbol in enumerate(alphabet):
                        # Obtener estados destino
                        dest_i = transitions[i][symbol_idx]
                        dest_j = transitions[j][symbol_idx]
                        
                        # Si los destinos son diferentes, verificar si están marcados
                        if dest_i != dest_j:
                            # Ordenar para acceder correctamente a la tabla
                            min_dest = min(dest_i, dest_j)
                            max_dest = max(dest_i, dest_j)
                            
                            # Si el par destino está marcado, marcar el par actual
                            if min_dest in marked and max_dest in marked[min_dest]:
                                if marked[min_dest][max_dest]:
                                    marked[i][j] = True
                                    changed = True
                                    break
    
    # Paso 4: Recolectar pares equivalentes (no marcados)
    equivalent_pairs = []
    for i in range(n_states):
        for j in range(i + 1, n_states):
            if not marked[i][j]:
                equivalent_pairs.append((i, j))
    
    return equivalent_pairs


def main():
    """Función principal que maneja entrada y salida según las especificaciones"""
    
    print("=== ALGORITMO DE MINIMIZACIÓN DE AUTÓMATAS - KOZEN ===")
    print("Formato de entrada:")
    print("1. Número de casos de prueba")
    print("2. Para cada caso:")
    print("   - Número de estados")
    print("   - Alfabeto (símbolos separados por espacios)")
    print("   - Estados finales (números separados por espacios)")
    print("   - Tabla de transiciones (una fila por estado)")
    print("=" * 60)
    
    # Leer número de casos
    print("Ingrese el número de casos de prueba:")
    c = int(input().strip())
    
    for case_num in range(1, c + 1):
        print(f"\n--- CASO {case_num} ---")
        
        # Leer número de estados
        print("Ingrese el número de estados:")
        n = int(input().strip())
        print(f"Estados del autómata: 0, 1, 2, ..., {n-1}")
        
        # Leer alfabeto
        print("Ingrese el alfabeto (símbolos separados por espacios):")
        print("Ejemplo: a b")
        alphabet = input().strip().split()
        print(f"Alfabeto: {alphabet}")
        
        # Leer estados finales
        print("Ingrese los estados finales (números separados por espacios):")
        print("Si no hay estados finales, presione Enter")
        final_states_line = input().strip()
        if final_states_line:
            final_states = set(map(int, final_states_line.split()))
        else:
            final_states = set()
        print(f"Estados finales: {final_states if final_states else 'ninguno'}")
        
        # Leer tabla de transiciones
        print(f"\nIngrese la tabla de transiciones ({n} filas):")
        print(f"Cada fila debe tener {len(alphabet)} números (estados destino)")
        print("Orden de símbolos:", " ".join(alphabet))
        
        transitions = []
        for i in range(n):
            print(f"Estado {i} -> ", end="")
            row = list(map(int, input().strip().split()))
            
            # Validar que la fila tenga el número correcto de transiciones
            if len(row) != len(alphabet):
                print(f"ERROR: Se esperaban {len(alphabet)} transiciones, se recibieron {len(row)}")
                return
            
            transitions.append(row)
        
        print("\n--- PROCESANDO ---")
        
        # Aplicar algoritmo de minimización
        equivalent_pairs = minimize_automaton(n, alphabet, final_states, transitions)
        
        # Mostrar resultado
        print(f"\nResultado para el caso {case_num}:")
        if equivalent_pairs:
            output_pairs = []
            for pair in equivalent_pairs:
                output_pairs.append(f"({pair[0]}, {pair[1]})")
            result = " ".join(output_pairs)
            print(f"Estados equivalentes: {result}")
        else:
            print("No hay estados equivalentes")
            result = ""
        
        # Salida en formato requerido para la tarea
        print("\n--- SALIDA FORMATO TAREA ---")
        print(result if result else "")
    
    print("\n=== PROCESAMIENTO COMPLETO ===")


if __name__ == "__main__":
    main()