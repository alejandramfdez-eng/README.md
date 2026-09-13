from conecta_4.linear_board import LinearBoard
from conecta_4.settings import BOARD_LENGTH
from conecta_4.list_utils import *

class SquareBoard:
    @classmethod
    def from_list(cls, list_of_list):
        """
        Devuelve el tablero compuesto
        :param list_of_list: list(list)
        :return: un tablero completo
        """
        board = cls()
        board._columns = map_list(list_of_list, LinearBoard.from_list)
        return board

    @classmethod
    def from_str_board(cls, str_board):
        """
        Crea y devuelve un tablero a partir de una cadena de texto,
        procesando sus filas y convirtiendo los caracteres vacíos en None
        str -> LinearBoard -> SquareBoard
        :param str_board: str
        :return: tablero completo
        """
        #Tokenizamos
        list_of_strings = str_board.split('|')
        #Vamos a crear una lista de listas
        matrix = explode_list(list_of_strings)
        #Cambiamos '.' por None
        matrix = replace_all(matrix, '.', None)
        #Transformamos a SqureBoard
        return cls.from_list(matrix)

    @classmethod
    def from_board_code(cls, board_code):
        """
        Devuelve un tablero completo
        :param board_code: codigo del tablero
        :return: tablero
        """
        return cls.from_str_board(board_code.str_board)

    #Dunders. Que cosas le puede preguntar python
    def __init__(self):
        """
        Inicializa un nuevo tablero
        """
        self._columns = make_list_from_factory(BOARD_LENGTH, LinearBoard)

    def __repr__(self):
        """
        Devuelve una cadena de texto representativa del tablero y el estado de sus columnas.
        :return: str
        """
        return f'{self.__class__}:{self._columns}'

    def __len__(self):
        """
        Devuelve el número de columnas del tablero.
        :return: int
        """
        return len(self._columns)

    def __eq__(self, other):
        """
        Comprueba si el tablero es igual a otro basándose en sus columnas.
        :param other: el tablero a comparar
        :return: bool
        """
        if not isinstance(other, self.__class__):
            return False
        else:
            return self._columns == other._columns

    def __hash__(self):
        """
        Calcula el valor hash del tablero a partir de sus columnas.
        :return: int
        """
        return hash(tuple(self._columns))

    #Metodos. Qué cosas puede hacer mi clase

    def is_full(self):
        """
        Comprueba si las columnas estan llenas
        :return: bool
        """
        result = True
        for linear_board in self._columns:
            result = result and linear_board.is_full()
        return result

    def add(self, char, column):
        """
        Añade una ficha en una columna específica del tablero
        :param char: ficha a añadir
        :param column: int (indice de la columna seleccionada)
        :return: resultado devuelto por la columna
        """
        result = self._columns[column].add(char)
        return result

    def as_matrix(self):
        """
        Devuelve el estado del tablero en forma de matriz
        :return: list(list)
        """
        result = []
        for column in self._columns:
            result.append(column._columns)
        #devuelve los datos en bruto de las columnas
        return result

    def as_code(self):
        """
        Devuelve el código identificador del tablero actual en BoardCode.
        :return: BoardCode
        """
        return BoardCode(self)

    def is_victory(self, char):
        """
        Comprueba si un jugador ha ganado la partida.
        :param char: ficha
        :return: bool
        """
        # devuelve True si hay victoria en alguna dirección, False en caso contrario
        return (self._any_vertical_victory(char) or
                self._any_descending_diagonal(char) or
                self._any_ascending_diagonal(char) or
                self._any_horizontal_victory(char))

    def _any_vertical_victory(self, char):
        """
        Comprueba si el jugador tiene una línea ganadora en las columnas verticales.
        :param char: ficha
        :return: bool
        """
        result = False
        for linear_board in self._columns:
            result = result or linear_board.is_victory(char)
        #devuelve True si hay victoria vertical, False en caso contrario
        return result

    def _any_horizontal_victory(self, char):
        """
        Comprueba si el jugador tiene una línea ganadora en las filas horizontales.
        :param char: ficha
        :return: bool
        """
        transpose_matrix = transpose(self.as_matrix())
        transpose_board = SquareBoard.from_list(transpose_matrix)
        # devuelve True si hay victoria horizontal, False en caso contrario
        return transpose_board._any_vertical_victory(char)

    def _any_descending_diagonal(self, char):
        """
        Comprueba si hay una victoria en diagonal descendente.
        :param char: ficha
        :return: bool
        """
        matrix = self.as_matrix()
        dm = displace_matrix(matrix)
        displace_board = SquareBoard.from_list(dm)
        #devuelve True si hay victoria diagonal descendente, False en caso contrario
        return displace_board._any_horizontal_victory(char)

    def _any_ascending_diagonal(self, char):
        """
        Comprueba si hay una victoria en diagonal ascendente.
        :param char: ficha
        :return: bool
        """
        matrix = self.as_matrix()
        rm = reverse_matrix(matrix)
        reverse_board = SquareBoard.from_list(rm)
        #devuelve True si hay victoria diagonal ascendente, False en caso contrario
        return reverse_board._any_descending_diagonal(char)

class BoardCode:
    def __init__(self, board):
        """
        Inicializa el codigo convirtiendo el tablero en una cadena de texto.
        :param board: tablero
        """
        self._str_board = colpase_matrix(board.as_matrix())

    @property

    def str_board(self):
        """
        Devuelve la cadena de texto con el tablero codificado.
        :return: str
        """
        return self._str_board

    def __eq__(self, other):
        """
        Comprueba si dos códigos de tablero son iguales
        :param other: el objeto a comparar
        :return: bool
        """
        if not isinstance(other, self.__class__):
            return False
        else:
            return self._str_board == other.str_board

    def __hash__(self):
        """
        Calcula el valor hash a partir de la cadena de texto del tablero.
        :return: int
        """
        return hash(self._str_board)

    def __repr__(self):
        """
        Devuelve el texto del código y el nombre de la clase.
        :return: str
        """
        return f'{self._str_board}:{self.__class__}'