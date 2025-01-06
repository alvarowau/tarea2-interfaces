"""
Módulo para gestionar usuarios con validación de NIF y NIE.

Este módulo incluye una clase `Usuario` que permite almacenar información básica de un usuario,
generar nombres de usuario a partir de su nombre y primer apellido, y validar NIF o NIE.

Clases:
    Usuario: Representa a un usuario con sus datos y métodos asociados.

Tests:
    Los ejemplos de uso están documentados al final de este archivo.

Autor: [Tu Nombre]
Fecha: [Fecha Actual]
"""

class Usuario:
    """
    Clase para almacenar y gestionar datos de un usuario.

    Atributos:
        nombre (str): Nombre del usuario.
        apellido1 (str): Primer apellido del usuario.
        apellido2 (str): Segundo apellido del usuario.
        usuario (str): Nombre de usuario generado.
        nif (str): Número de identificación fiscal (NIF/NIE).
    """
    def __init__(self, nombre: str, apellido1: str, apellido2: str):
        """
        Constructor de la clase Usuario.

        Args:
            nombre (str): Nombre del usuario.
            apellido1 (str): Primer apellido del usuario.
            apellido2 (str): Segundo apellido del usuario.
        """
        self.nombre = nombre
        self.apellido1 = apellido1
        self.apellido2 = apellido2
        self.usuario = self.gen_usuario()
        self.nif = '*'

    def gen_usuario(self) -> str:
        """
        Genera un nombre de usuario a partir de la inicial del nombre y el primer apellido.

        Returns:
            str: Nombre de usuario generado.
        """
        return f"{self.nombre[0].lower()}{self.apellido1.lower().replace(' ', '')}"

    def fnif(self, nif: str) -> bool:
        """
        Valida si la letra del NIF es correcta.

        Args:
            nif (str): NIF a validar.

        Returns:
            bool: True si el NIF es válido, False en caso contrario.
        """
        letras = "TRWAGMYFPDXBNJZSQVHLCKE"
        try:
            numero = int(nif[:-1])
            letra = nif[-1].upper()
            return letras[numero % 23] == letra
        except (ValueError, IndexError):
            return False

    def fnie(self, nie: str) -> bool:
        """
        Valida si la letra del NIE es correcta.

        Args:
            nie (str): NIE a validar.

        Returns:
            bool: True si el NIE es válido, False en caso contrario.
        """
        conversion = {'X': '0', 'Y': '1', 'Z': '2'}
        try:
            nie = conversion.get(nie[0], nie[0]) + nie[1:]
            return self.fnif(nie)
        except IndexError:
            return False

    def setnif(self, identificador: str):
        """
        Asigna un NIF o NIE al usuario si es válido.

        Args:
            identificador (str): NIF o NIE a asignar.

        """
        if self.fnif(identificador) or self.fnie(identificador):
            self.nif = identificador
        else:
            self.nif = '*'


# Tests y ejemplos de uso
if __name__ == "__main__":
    # Crear un usuario
    usuario = Usuario("Juan", "Pérez", "López")
    assert usuario.usuario == "jperez"

    # Validar NIF
    assert usuario.fnif("12345678Z") is True
    assert usuario.fnif("12345678A") is False

    # Validar NIE
    assert usuario.fnie("X1234567L") is True
    assert usuario.fnie("Y1234567L") is False

    # Asignar NIF o NIE
    usuario.setnif("12345678Z")
    assert usuario.nif == "12345678Z"

    usuario.setnif("Y1234567L")
    assert usuario.nif == "*"
