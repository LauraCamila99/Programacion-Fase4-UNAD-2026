from abc import ABC, abstractmethod
from datetime import datetime


class Entidad(ABC):
    """
    Clase abstracta base para todas las entidades del sistema.
    Contiene atributos y comportamientos comunes.
    """

    def __init__(self, id_entidad):
        self.id_entidad = id_entidad
        self.activo = True
        self.__fecha_creacion = datetime.now()

    # ---------- ID ----------

    @property
    def id_entidad(self):
        return self.__id

    @id_entidad.setter
    def id_entidad(self, valor):
        if not isinstance(valor, int):
            raise ValueError("El ID debe ser un número entero.")

        if valor <= 0:
            raise ValueError("El ID debe ser mayor que cero.")

        self.__id = valor

    # ---------- ACTIVO ----------

    @property
    def activo(self):
        return self.__activo

    @activo.setter
    def activo(self, valor):
        if not isinstance(valor, bool):
            raise ValueError("El estado activo debe ser True o False.")

        self.__activo = valor

    # ---------- FECHA ----------

    @property
    def fecha_creacion(self):
        return self.__fecha_creacion

    # ---------- MÉTODO ABSTRACTO ----------

    @abstractmethod
    def mostrar_informacion(self):
        """
        Este método deberá implementarse en todas las clases hijas.
        """
        pass