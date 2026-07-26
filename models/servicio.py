from abc import abstractmethod

from models.entidad import Entidad


class Servicio(Entidad):
    """
    Clase abstracta que representa un servicio ofrecido por Software FJ.
    Todas las clases de servicios heredarán de esta.
    """

    def __init__(self, id_entidad, nombre, descripcion, costo_base):

        # Inicializa los atributos heredados de Entidad
        super().__init__(id_entidad)

        self.nombre = nombre
        self.descripcion = descripcion
        self.costo_base = costo_base

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
    # Descripción
    # -------------------------

    @property
    def descripcion(self):
        return self.__descripcion

    @descripcion.setter
    def descripcion(self, valor):

        if not isinstance(valor, str):
            raise ValueError("La descripción debe ser un texto.")

        valor = valor.strip()

        if len(valor) < 10:
            raise ValueError(
                "La descripción debe tener al menos 10 caracteres."
            )

        self.__descripcion = valor

    # -------------------------
    # Costo Base
    # -------------------------

    @property
    def costo_base(self):
        return self.__costo_base

    @costo_base.setter
    def costo_base(self, valor):

        if not isinstance(valor, (int, float)):
            raise ValueError(
                "El costo base debe ser un número entero o decimal."
            )

        if valor <= 0:
            raise ValueError(
                "El costo base debe ser mayor que cero."
            )

        self.__costo_base = float(valor)

    # -------------------------
    # Información general
    # -------------------------

    def mostrar_informacion(self):

        return (
            f"Servicio(ID: {self.id_entidad}, "
            f"Nombre: {self.nombre}, "
            f"Costo Base: ${self.costo_base:.2f}, "
            f"Activo: {self.activo})"
        )

    # -------------------------
    # Métodos abstractos
    # -------------------------

    @abstractmethod
    def calcular_costo(self):
        """
        Calcula el costo final del servicio.
        """
        pass

    @abstractmethod
    def describir_servicio(self):
        """
        Describe el servicio ofrecido.
        """
        pass
