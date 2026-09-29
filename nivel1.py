
#Nombre: Baque Hernández Derek Damián

# ==========================================
# NIVEL 1: Closures con Inyección de Comportamiento
# ==========================================

print("NIVEL 1 Closures con Inyección de Comportamiento")

# Ejercicio 1: Generador de Formateadores con Transformación
def crear_formateador(prefijo, fn_transformacion):
    return lambda texto: f"{prefijo}{fn_transformacion(texto)}"

print("\nEjercicio 1:")
formato_alerta = crear_formateador("[ALERTA] -> ", lambda txt: txt.upper())
print(formato_alerta("falla en la conexion"))

# Ejercicio 2: Multiplicador Paramétrico con Mapeo
def crear_operador(factor, operacion_lambda):
    return lambda numero: operacion_lambda(numero, factor)

print("\nEjercicio 2:")
potencia = crear_operador(3, lambda base, exp: base ** exp)
print(f"2 elevado a la 3 es: {potencia(2)}")

# Ejercicio 3: Calculador de Descuentos con Regla Dinámica
def crear_descuento_dinamico(regla_lambda):
    def aplicar(precio, descuento):
        if regla_lambda(precio) == True:
            return precio - descuento
        return precio
    return aplicar

print("\nEjercicio 3:")
promocion = crear_descuento_dinamico(lambda p: p >= 50)
print(f"Compra $60 (menos $10): ${promocion(60, 10)}")
print(f"Compra $30 (menos $10): ${promocion(30, 10)}")

# Ejercicio 4: Generador de Seriales / Nombres Únicos
def crear_generador_sufijos(patron_lambda):
    return lambda nombre: f"{nombre}_{patron_lambda()}"

print("\nEjercicio 4:")
generar_backup = crear_generador_sufijos(lambda: "backup_final")
print("Archivo:", generar_backup("base_datos"))

# Ejercicio 5: Conversor de Divisas con Margen
def crear_conversor(tasa, margen_lambda):
    return lambda monto: (monto * tasa) + ((monto * tasa) * margen_lambda(monto))

print("\nEjercicio 5:")

cambio_euro = crear_conversor(0.92, lambda m: 0.02 if m > 1000 else 0.05)
print(f"Cambiar $500: {cambio_euro(500)} euros")
print("------------------------------------------\n")