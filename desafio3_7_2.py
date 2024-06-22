# Creamos una lista con los códigos de los libros
codigos_libros=[123,145,234,125,567,678]
# Luego usamos sorted() para ordenar en forma decreciente
codigos_libros_ordenados = sorted(codigos_libros, reverse=True) # en esta línea estamos creando la lista de códigos
#ordenados de manera decreciente usando la función sorted y ordenándole que los forme en reversa ("reverse")
#y que lo convierta en verdad (true)
print("Lista original:", codigos_libros) #pedimos que se muestre la lista de códigos inicial
print("Lista ordenada en orden decreciente:", codigos_libros_ordenados) #pedimos que se muestre la lista
#de códigos ordenados decrecientes.