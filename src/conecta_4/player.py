from random import choice

from conecta_4.oracle import *
from conecta_4.square_board import *
from conecta_4.move import *
from conecta_4.settings import BOARD_LENGTH

class Player:
    def __init__(self, name, char = None, oracle = BaseOracle(), opponent = None):
        """
        Inicializa al jugador y prepara una lista vacía para almacenar
        los movimientos realizadas.
        """
        self.name = name
        self.char = char
        self._oracle = oracle
        self.opponent = opponent

        #Quiero guardar la tirada
        self.last_moves = []

    @property
    def opponent(self):
        """
        Da acceso completo del rival
        :return: Player
        """
        return self._opponent
    @opponent.setter
    def opponent(self, other):
        """
        Asigna al jugador rival como oponente
        """
        self._opponent = other
        if other is not None:
            other._opponent = self

    def play(self, board):
        """
        Elige la mejor columna donde jugar. Estas me las recomienda el oráculo
        """
        (best, recommendations) = self._ask_oracle(board)
        self._play_on(board, best.index, recommendations)

    def _play_on(self, board, position, recommendations ):
        """
        Jugamos en la pocisión elegida de las jugadas recomendadas
        """
        board.add(self.char, position)
        self.last_moves.insert(0, Move(position, board.as_code(),recommendations, self))
                                        #Lo haré con un insert en una tupla
    def _ask_oracle(self, board):
        """
        Pregunto al oráculo para que me de las posibles jugadas
        :param board: tablero
        :return: tupls
        """
        recommendations = self._oracle._get_recommendation(board, self)
        best = self._choose_a_recommendation(recommendations)
        return (best, recommendations)

    def _choose_a_recommendation(self, recommendations):
        """
        Elijo una de las recomendaciones que me da el oráculo
        :param recommendations: list
        :return: recomendacion optima
        """
        valid_recommendations = list(filter(lambda x:
                                            x.classification != ColumnClassification.FULL,
                                            recommendations))
        #Ordenamos la lista de mayor a menor
        valid_recommendations = sorted(valid_recommendations, key = lambda x : x.classification.value, reverse = True)
        if all_the_same_score(valid_recommendations):
            return choice(valid_recommendations)
        else:
            return valid_recommendations[0]
    #Hooks
    def _on_lose(self):
        """
        Notifica cuando el jugador pierde la partida.
        """
        pass


class HumanPlayer(Player):
    """
    Esta clase no se testea porque son valores introducidos por el usuario
    Testeamos los valores que introduce el usuario
    """
    def __init__(self, name, char = None):
        super().__init__(name, char)

    def _ask_oracle(self, board):
        """
        Mi oráculo es el jugador humano. Le pido que me de la posición a través de pantalla
        :param board: tablero
        :return: tupla
        """
        while True:
            position = input("Tu turno! Selecciona una columna: ")
            #Comprobaciones de entrada correcta
            if (HumanEntryVerifications._is_int(position) and
                HumanEntryVerifications._is_in_range(board,int(position)) and
                HumanEntryVerifications._is_not_full(board, int(position))):
                position = int(position)
                return (ColumnRecommendations(position,None), None)


class HumanEntryVerifications:
    @staticmethod
    def _is_int(cadena):
        """
        Comprueba si una cadena de texto representa un número entero válido.
        :param cadena: str
        :return: bool
        """
        try:
            num = int(cadena)
            return True
        except:
            return False

    @staticmethod
    def _is_not_full(board, col):
        """
        Comprueba si una columna esta disponible para jugar
        :param board: tablero
        :param col: int
        :return: bool
        """
        return not board._columns[col].is_full()

    @staticmethod
    def _is_in_range(board, col):
        """
        Comprueba los limites validos del tablero
        :param board: tablero
        :param col: int
        :return: bool
        """
        return 0 <= col < len(board)

class ReportingPlayer(Player):
    """
    Le pide al oraculo la mejor recomendación de su base de datos de recomendaciones
    """
    def _on_lose(self):
        """
        Aprende de la derrota enviando el historial de movimientos al oráculo.
        """
        self._oracle.back_track(self.last_moves)