nombre_archivo = "archivo.txt"

with open(nombre_archivo, 'r') as archivo:
    contenido = archivo.read()

# Contar letras
cantidad_letras = sum(c.isalpha() for c in contenido)

# Contar espacios
cantidad_espacios = sum(c.isspace() for c in contenido)

# Imprimir el resumen
print("Cantidad de letras:", cantidad_letras)
print("Cantidad de espacios:", cantidad_espacios)

# Escribir el resumen en un archivo de texto
resumen = f"Cantidad de letras: {cantidad_letras}\nCantidad de espacios: {cantidad_espacios}"
with open('resumen.txt', 'w') as archivo_resumen:
    archivo_resumen.write(resumen)

print("Se ha generado un archivo 'resumen.txt' con el resumen de la cantidad de letras y espacios.")
