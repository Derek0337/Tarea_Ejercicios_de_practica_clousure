#nombre: Baque Hernández Derek Damián


# ==========================================
# NIVEL 4: Patrones Avanzados
# ==========================================

print(" NIVEL 4 Patrones Avanzados")

# Ejercicio 16: Validador Compuesto de Reglas
def crear_validador_multiple(*lambdas_criterios):
    def validar(objeto):
        for regla in lambdas_criterios:
            if regla(objeto) == False:
                return False
        return True
    return validar

print("\nEjercicio 16:")
# Clave: mas de 8 letras, y que no empiece con un numero
validador_clave = crear_validador_multiple(
    lambda s: len(s) >= 8,
    lambda s: s[0].isalpha()
)
print("Validar 'admin123':", validador_clave("admin123"))
print("Validar '123admin':", validador_clave("123admin"))

# Ejercicio 17: Caché con Expiración (Tamaño Máximo)
def memoizar_avanzado(fn_costosa, max_items):
    memoria = {}
    orden_llegada = []
    
    def cache(parametro):
        if parametro in memoria:
            return f"De cache: {memoria[parametro]}"
            
        if len(memoria) >= max_items:
            viejo = orden_llegada[0]
            orden_llegada.pop(0)
            del memoria[viejo]
            
        resultado = fn_costosa(parametro)
        memoria[parametro] = resultado
        orden_llegada.append(parametro)
        return f"Calculado: {resultado}"
        
    return cache

print("\nEjercicio 17:")
consulta = memoizar_avanzado(lambda id: f"Datos {id}", 2)
print(consulta(1))
print(consulta(2))
print(consulta(1)) # Sale de la memoria
print(consulta(3)) # Expulsa al 2

# Ejercicio 18: Motor de Pipeline Secuencial
def crear_pipeline(*funciones):
    def procesar(dato):
        for fn in funciones:
            dato = fn(dato)
        return dato
    return procesar

print("\nEjercicio 18:")
limpiar_texto = crear_pipeline(
    lambda txt: txt.strip(),
    lambda txt: txt.lower(),
    lambda txt: txt.replace(" ", "_")
)
print("Pipeline string:", limpiar_texto("  Mi Archivo Final  "))

# Ejercicio 19: Sistema Pub/Sub (Eventos)
def crear_sistema_eventos():
    eventos = {}
    def gestor(accion, nombre, param=None):
        if accion == "suscribir":
            if nombre not in eventos:
                eventos[nombre] = []
            eventos[nombre].append(param) # param aqui es la funcion
        elif accion == "emitir":
            if nombre in eventos:
                for funcion in eventos[nombre]:
                    funcion(param) # param aqui es el dato
    return gestor

print("\nEjercicio 19:")
sistema = crear_sistema_eventos()
sistema("suscribir", "alerta", lambda msj: print(f"Recibido en pantalla: {msj}"))
print("Emitiendo...", end=" ")
sistema("emitir", "alerta", "Batería baja")

# Ejercicio 20: Mini-Query Engine sobre Listas
def crear_consultor(campo):
    def buscar(lista, filtro_lambda):
        resultados = []
        for obj in lista:
            if campo in obj and filtro_lambda(obj[campo]) == True:
                resultados.append(obj)
        return resultados
    return buscar

print("\nEjercicio 20:")
cuadros = [
    {"producto": "Cuadro A4", "stock": 5},
    {"producto": "Sticker", "stock": 1},
    {"producto": "Cuadro 10x15", "stock": 0}
]
buscar_stock = crear_consultor("stock")
print("Bajo stock (menos de 2):", buscar_stock(cuadros, lambda s: s < 2))
