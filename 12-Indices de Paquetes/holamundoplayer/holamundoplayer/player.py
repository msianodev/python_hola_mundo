"""
Este es el modulo que incluye la clase de reproductor de musica
"""


class Player:
    """
    Esta clase crea un reproductor
    de musica
    """

    def play(self, song):
        """
        Reproduce la cancion que recibio
        en el constructor

        Parameters:
        song (str): Nombre de la cancion a reproducir

        Returns:
        int: Devuelve 1 si reproduce con exito,
        en caso de fracaso devuelve cero
        """
        print(f"Reproduciendo {song}")
        return 1
