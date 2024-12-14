
# Abrir el archivo en modo escritura
f = open('fichero', 'w')
f.write('el fichero abierto en modo escritura\n')
f.write('por defecto se trata como un fichero de texto')
f.close()

# Intentar leer el archivo (sin éxito debido a un error en el bucle for)
for line in f('fichero'):
    print(line)
