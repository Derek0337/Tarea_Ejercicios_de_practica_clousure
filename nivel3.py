
#nombre: Baque Hernández Derek Damián

# ==========================================
# NIVEL 3: HOFs Complejas
# ==========================================
import time

print(" NIVEL 3 HOFs Complejas")

# Ejercicio 11: Pipeline de Mapeo y Filtrado Combinado
def procesar_coleccion(lista, fn_predicado, fn_transformacion):
    # Uso normal de filter y map
    filtrados = filter(fn_predicado, lista)
    return list(map(fn_transformacion, filtrados))

print("\nEjercicio 11:")
precios = [15.0, 25.0, 10.0, 50.0]
# Filtrar mayores a 20 y sumarles $5
resultado = procesar_coleccion(precios, lambda p: p > 20, lambda p: p + 5)
print("Lista procesada:", resultado)

# Ejercicio 12: Reductor / Agrupador Personalizado
def agrupar_por(lista_diccionarios, fn_clave):
    agrupado = {}
    for item in lista_diccionarios:
        clave = fn_clave(item)
        if clave not in agrupado:
            agrupado[clave] = []
        agrupado[clave].append(item["nombre"])
    return agrupado

print("\nEjercicio 12:")
usuarios = [
    {"nombre": "Paquito", "rol": "usuario"},
    {"nombre": "Admin12 ", "rol": "admin"},
    {"nombre": "Derke", "rol": "usuario"}
]
print("Agrupados:", agrupar_por(usuarios, lambda u: u.get("rol")))

# Ejercicio 13: Ejecutor Repetitivo con Estado Accesible
def ejecutar_y_rastrear(fn_tarea, n):
    def historial():
        lista = []
        for i in range(n):
            lista.append(fn_tarea(i))
        return lista
    return historial

print("\nEjercicio 13:")
generar_ips = ejecutar_y_rastrear(lambda i: f"192.168.1.{i+10}", 3)
print("Historial de IPs:", generar_ips())

# Ejercicio 14: Compositor de Cadenas de Operaciones
def componer_dos(f, g):
    return lambda x: f(g(x))

print("\nEjercicio 14:")
# Primero eleva al cuadrado, luego formatea
calc_area = componer_dos(lambda num: f"Area: {num} m2", lambda lado: lado * lado)
print(calc_area(4))

# Ejercicio 15: Decorador / Profiling
def auditar_ejecucion(fn_objetivo, fn_logger):
    def envoltura(*args):
        inicio = time.time()
        resultado = fn_objetivo(*args)
        fin = time.time()
        tiempo = fin - inicio
        fn_logger(f"Tardó {tiempo} segundos")
        return resultado
    return envoltura

print("\nEjercicio 15:")
def calculo_lento():
    suma = 0
    for i in range(100000):
        suma = suma + i
    return suma

auditor = auditar_ejecucion(calculo_lento, lambda log: print(f"[LOG] {log}"))
print("Resultado:", auditor())
