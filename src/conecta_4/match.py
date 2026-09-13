class Match:
    def __init__(self, player1, player2):
        """
        Inicializa una nueva partida configurando los jugadores,
        sus fichas y el orden de los turnos.
        """
        #Asignamos los char a mano. Después se elegiran al azar.
        player1.char = 'o'
        player2.char = 'x'
        #Tenemos que fijar el oponente
        player1.opponent = player2

        self._players = {'o': player1, 'x': player2}
        self._round = [player1, player2]

    @property
    def get_next_player(self):
        """
        Mira el jugador. Empieza siempre en el primer
        :return: el jugador
        """
        next_player = self._round[0]
        self._round.reverse()
        #Devuelve el jugador que realiza el proximo movimiento
        return next_player

    def get_player(self, char):
        """
        Mira la ficha del jugador
        :param char: str
        :return: el jugador
        """
        #Devuelve el jugador que posee la fficha
        return self._players[char]

    def get_winner(self, board):
        """
        Evalúa el tablero para ver si algún jugador ha ganado la partida.
        :param board: tablero
        :return: El jugador que ha ganado la partida, o None si no hay ganador.
        """
        if board.is_victory('x'):
            return self.get_player('x')
        if board.is_victory('o'):
            return self.get_player('o')
        else:
            return None

    def get_loser(self, board):
        """
        Evalúa el tablero para ver qué jugador ha perdido la partida.
        :param board: tablero
        :return: El jugador que ha perdido, o None si no hay perdedor.
        """
        if board.is_victory('x'):
            return self.get_player('o')
        if board.is_victory('o'):
            return self.get_player('x')

    def play_more(self):
        """
        Pregunta al usuario si quiere jugar una partida más
        :return: bool
        """
        result = True
        while True:
            answer = input('¿Le apetece una partida más? S/N')
            if answer.lower() == 's':
                result = True
                break
            elif answer.lower() == 'n':
                result = False
                break
        #Devuelve True si el usuario quiere seguir jugando, False en caso contrario.
        return result
