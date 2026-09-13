from conecta_4.settings import BOARD_LENGTH, VICTORY_STRIKE
from conecta_4.list_utils import find_strike, make_list, index_first_element

class LinearBoard:
    """
    Representamos una sola columna.
    Los jugadores son:
    - Jugador 1 : x
    - Jugador 2 : o
    - Las posiciones vacías van a ser None
    """
    @classmethod
    def from_list(cls, data):
        """
        Devuelve una nueva instancia del tablero utilizando una lista de columnas.
        :param data: list
        :return: Una nueva instancia con los datos recibidos
        """
        board = cls()
        board._columns = data
        return board

    #Dunders. Cosas que yo le puedo preguntar
    def __init__(self):
        """
        Inicializa una nueva instancia del tablero con sus columnas vacías.
        """
        self._columns = make_list(BOARD_LENGTH, None)
        # [None for i in range(BOARD_LENGTH)]

    def __eq__(self, other):
        """
        Comprueba si el objeto actual es igual a otro objeto basándose en el contenido de sus columnas.
        :param other: any
        :return: bool
        """
        if not isinstance(other, self.__class__):
            return False
        else:
            return self._columns == other._columns

    def __hash__(self):
        """
        Calcula y devuelve el valor hash único del objeto basándose en sus columnas.
        :return: int
        """
        return hash(tuple(self._columns))

    # Cosas que puede hacer
    def get_columns(self):
        """
        Devuelve la lista de columnas que componen el tablero.
        :return: list
        """
        return self._columns

    def is_full(self):
        """
        Comprueba si el tablero está lleno verificando si la última posición contiene un elemento.
        :return: bool
        """
        return self._columns[-1] is not None

    def add(self, char):
        """
        Añade un nuevo elemento o ficha en el primer espacio vacío disponible si el tablero no está lleno.
        :return: bool
        """
        if not self.is_full():
            i = index_first_element(self._columns, None)
            # i = self._column.index(None)
            self._columns[i] = char

    def is_victory(self, char):
        """
        Comprueba si un jugador ha ganado consiguiendo una racha de fichas consecutivas.
        :return: bool
        """
        return find_strike(self._columns, char, VICTORY_STRIKE)

    def is_tie(self, char_1, char_2):
        """
        Comprueba si la partida ha terminado en empate al no haber ganador para ningún jugador.
        :return: bool
        """
        return ((self.is_victory(char_1) == False) and
                (self.is_victory(char_2) == False))
