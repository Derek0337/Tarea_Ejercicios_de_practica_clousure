
#Nombre: Baque Hernández Derek Damián

# ==========================================
# NIVEL 2: Estado Encapsulado Avanzado
# ==========================================

print(" NIVEL 2 Estado Encapsulado Avanzado")

# Ejercicio 6: Contador Ponderado
def crear_contador_paso(fn_paso):
    cuenta = 0
    def contador():
        nonlocal cuenta
        cuenta = fn_paso(cuenta)
        return cuenta
    return contador

print("\nEjercicio 6:")
contar_doble = crear_contador_paso(lambda c: c + 2 if c == 0 else c * 2)
print("Paso a paso:", contar_doble(), "->", contar_doble(), "->", contar_doble())

# Ejercicio 7: Acumulador con Filtro de Aceptación
def crear_acumulador_validado(criterio_lambda):
    total = 0
    def acumular(valor):
        nonlocal total
        if criterio_lambda(valor):
            total = total + valor
        return total
    return acumular

print("\nEjercicio 7:")
# Solo suma la memoria RAM si es de 8GB o más
instalar_ram = crear_acumulador_validado(lambda gb: gb >= 8)
print("Acumulado:", instalar_ram(8))  # Entra
print("Acumulado:", instalar_ram(4))  # No entra
print("Acumulado:", instalar_ram(16)) # Entra

# Ejercicio 8: Promediador con Eliminación de Valores Extremos
def crear_promediador_filtrado(filtro_lambda):
    datos = []
    def promediar(valor):
        nonlocal datos
        if not filtro_lambda(valor):
            datos.append(valor)
        if len(datos) == 0:
            return 0
        return sum(datos) / len(datos)
    return promediar

print("\nEjercicio 8:")
# Promedio de ping, ignorando si hay un lagazo mayor a 200
promedio_ping = crear_promediador_filtrado(lambda ping: ping > 200)
print("Ping 40:", promedio_ping(40))
print("Ping 300 (ignorado):", promedio_ping(300))
print("Ping 50:", promedio_ping(50))

# Ejercicio 9: Limitador de Tasa Inteligente
def crear_limitador_avanzado(max_intentos, fn_alerta):
    intentos = 0
    def ejecutar(fn_tarea):
        nonlocal intentos
        intentos = intentos + 1
        if intentos > max_intentos:
            return fn_alerta()
        return fn_tarea()
    return ejecutar

print("\nEjercicio 9:")
limite_login = crear_limitador_avanzado(2, lambda: "[BLOQUEADO] Exceso de intentos")
print(limite_login(lambda: "Login OK 1"))
print(limite_login(lambda: "Login OK 2"))
print(limite_login(lambda: "Login OK 3"))

# Ejercicio 10: Interruptor Múltiple (Máquina de Estados)
def crear_conmutador(lista_estados):
    indice = 0
    def alternar():
        nonlocal indice
        estado = lista_estados[indice]
        indice = indice + 1
        if indice >= len(lista_estados):
            indice = 0
        return estado
    return alternar

print("\nEjercicio 10:")
modos_juego = crear_conmutador(["Survival", "Creativo", "Aventura"])
print("Modo:", modos_juego(), "->", modos_juego(), "->", modos_juego(), "->", modos_juego())
