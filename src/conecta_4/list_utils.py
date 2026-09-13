def find_n(elements, needle, n):
    """
    Devuelve True si en elements hay n o más ocurrencias de needle
    :param elements: list
    :param needle: int
    :param n: int
    :return: bool
    """
    if n >= 0:
        index = 0
        count = 0
        while count < n and index < len(elements):
            if needle == elements[index]:
                count += 1
            index += 1
        return count >= n
    else:
        return False

def find_one(elements, needle):
    """
    Devuelve True si en elements hay una o mas ocurrencias de needle
    :param elements: list
    :param needle: int
    :return: bool
    """
    return find_n(elements, needle, 1)

def find_strike(elements, needle, n):
    """
    Devuelve True si en elements hay una racha de n o más ocurrencias consecutivas de needle.
    :param elements: list
    :param needle: int
    :param n: int
    :return: bool
    """
    if n >= 0:
        index = 0
        count = 0
        while count < n and index < len(elements):
            if needle == elements[index]:
                count += 1
            else:
                count = 0
            index += 1
        return count >= n
    else:
        return False

def make_list(length, filler):
    """
    Devuelve una lista de una longitud determinada rellena con un elemento específico.
    :param length: int
    :param filler: any
    :return: list
    """
    result = []
    index = 0
    while index < length:
        result.append(filler)
        index += 1
    return result

def index_first_element(elements, needle):
    """
    Obtiene el índice de la primera ocurrencia de un elemento determinado en una lista.
    :param elements: list
    :param needle: any
    :return: int / None
    """
    index = 0
    while index < len(elements):
        if needle == elements[index]:
            return index
        else:
            index += 1
    #Devuelve int si encuentra el elemento dentro de la lista y
    #por el contrario si recorre la lista y no lo encuentra devuelve None
    return None

def map_list(elements, transform):
    """
    Crea una lista nueva aplicando la funcion transform a cada elemento
    :param elements: list
    :param transform: callable
    :return: list
    """
    result = []
    for element in elements:
        result.append(transform(element))
    return result

def make_list_from_factory(length, factory):
    """
    Crea una lista de listas que son fabricadas por mi fábrica que es LinearBoard
    :param length: int
    :param factory: callable
    :return: list
    """
    result = []
    index = 0
    while index < length:
        result.append(factory())
        index += 1
    return result

def transpose(matrix):
    """
    Intercambia filas y columnas. Funciona con matrices no cuadradas.
    :param matrix: list (list)
    :return: list (list) transpuesta
    """

    if not matrix:
        return []
    height = len(matrix[0])
    result = []
    for i in range(height):
        sub_result = []
        for j in range(len(matrix)):
            sub_result.append(matrix[j][i])
        result.append(sub_result)
    return result

def displace(l, distancia, filler = None):
    """
    Desplaza los elementos de una lista una distancia determinada, rellenando los espacios vacíos.
    :param l: list
    :param distancia: int
    :param filler: any (por defecto None)
    :return: list
    """
    n = len(l)
    result = []
    for i in range(n):
        index = i - distancia
        if 0 <= index < n:
            result.append(l[index])
        else:
            result.append(filler)
    return result

def displace_matrix(matrix, filler = None):
    """
    Desplaza los elementos de cada fila progresivamente.
    :param matrix: list(list)
    :param filler: any (por defecto None)
    :return: list(list)
    """
    d = []
    for i in range(len(matrix)):
        d.append(displace(matrix[i], i - 1, filler))
    return d

def reverse_list(elements):
    """
    Devuelve una copia de la lista con sus elementos en orden inverso.
    :param elements: list
    :return: list
    """
    return elements[::-1]

def reverse_matrix(matrix):
    """
    Devuelve una nueva matriz invirtiendo el orden de los elementos de cada una de sus filas.
    :param matrix: list
    :return: list
    """
    result = []
    for col in matrix:
        result.append(reverse_list(col))
    return result

def all_the_same_score(elements):
    """
    Comprueba si todos los elementos de la lista son iguales. No controla lista vacía. De momento no pasa nada.
    :param elements: list
    :return: bool
    """
    if not elements:
        return True
    first_element = elements[0]
    result = True
    for element in elements:
        if element != first_element:
            result = False
    return result

def colpase_matrix(matrix, empty = '.', sep = '|'):
    """
    Convierte una matriz en una cadena de texto colapsando cada fila
    y uniéndolas con un separador.
    :param matrix: list(list)
    :param empty: str (por defecto '.')
    :param sep: str (por defecto '|')
    :return: str
    """
    result = ''
    for elt in matrix:
        result = result + sep + colapse_list(elt, empty)
    return result[1:]

def colapse_list(elements, empty = '.'):
    """
    Convierte una lista en una cadena de texto, reemplazando los valores None por un carácter de relleno.
    :param elements: list
    :param empty: str (por defecto '.'
    :return: str
    """
    result = ''
    for elt in elements:
        if elt is None:
            result = result + empty
        else:
            result = result + elt
    return result

def explode_list(list_of_strings): #['x..o', 'oxoo']
    """
    Convierte una lista de cadenas de texto en una lista de listas de caracteres.
    :param list_of_strings: list
    :return: list(list)
    """
    result = []
    for element in list_of_strings:
        result.append(list(element))
    return result

def replace_all(matrix, old, new):
    """
    Crea una nueva matriz reemplazando todas las ocurrencias de un elemento por otro nuevo.
    :param matrix: list(list)
    :param old: any (elemento a reemplazar)
    :param new: any (nuevo elemento)
    :return: list(list) modificada
    """
    new_matrix = []
    for element in matrix:
        new_matrix.append(replace_in_list(element, old, new))
    return new_matrix

def replace_in_list(elements, old, new):
    """
    Crea una nueva lista reemplazando todas las ocurrencias de un elemento por otro nuevo.
    :param elements: list
    :param old: any (elemento a reemplazar)
    :param new: any (nuevo elemento)
    :return: list(list) modificada
    """
    result = []
    for elt in elements:
        if elt == old:
            result.append(new)
        else:
            result.append(elt)
    return result