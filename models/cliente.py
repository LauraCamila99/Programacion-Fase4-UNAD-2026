import re
# Se utiliza para validar patrones mediante expresiones regulares

from models.entidad import Entidad


class Cliente(Entidad):
    """
    Representa un cliente de la empresa Software FJ.
    Hereda de la clase abstracta Entidad.
    """

    def __init__(self, id_entidad, nombre, documento, correo, telefono):
        super().__init__(id_entidad)

        self.nombre = nombre
        self.documento = documento
        self.correo = correo
        self.telefono = telefono

    # -------------------------
    # Nombre
    # -------------------------

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        if not isinstance(valor, str):
            raise ValueError("El nombre debe ser un texto.")

        valor = valor.strip()

        if len(valor) < 3:
            raise ValueError("El nombre debe tener al menos 3 caracteres.")

        self.__nombre = valor

    # -------------------------
    # Documento
    # -------------------------

    @property
    def documento(self):
        return self.__documento

    @documento.setter
    def documento(self, valor):

        if not isinstance(valor, str):
            raise ValueError("El documento debe ser una cadena de texto.")

        valor = valor.strip()

        patron = r"^[A-Za-z0-9]+$"

        if not re.match(patron, valor):
            raise ValueError(
                "El documento solo puede contener letras y números, sin espacios ni símbolos."
            )

        if len(valor) < 6 or len(valor) > 15:
            raise ValueError(
                "El documento debe tener entre 6 y 15 caracteres."
            )

        self.__documento = valor

    # -------------------------
    # Correo
    # -------------------------

    @property
    def correo(self):
        return self.__correo

    @correo.setter
    def correo(self, valor):

        if not isinstance(valor, str):
            raise ValueError("El correo debe ser un texto.")

        valor = valor.strip()

        patron = r"^[\w\.-]+@[\w\.-]+\.\w+$"

        if not re.match(patron, valor):
            raise ValueError("El correo electrónico no es válido.")

        self.__correo = valor

    # -------------------------
    # Teléfono
    # -------------------------

    @property
    def telefono(self):
        return self.__telefono

    @telefono.setter
    def telefono(self, valor):

        if not isinstance(valor, str):
            raise ValueError("El teléfono debe ingresarse como una cadena de texto.")

        valor = valor.strip()

        if not valor.isdigit():
            raise ValueError("El teléfono solo puede contener números.")

        if len(valor) < 7 or len(valor) > 15:
            raise ValueError("El teléfono debe tener entre 7 y 15 dígitos.")

        self.__telefono = valor

    # -------------------------
    # Método abstracto implementado
    # -------------------------

    def mostrar_informacion(self):
        return (
            f"Cliente(ID: {self.id_entidad}, "
            f"Nombre: {self.nombre}, "
            f"Documento: {self.documento}, "
            f"Correo: {self.correo}, "
            f"Teléfono: {self.telefono}, "
            f"Activo: {self.activo})"
        )
