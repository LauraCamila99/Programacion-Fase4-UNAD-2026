from models.servicio import Servicio


class Asesoria(Servicio):
    """
    Representa el servicio de asesoría especializada.
    """

    def __init__(
        self,
        id_entidad,
        nombre,
        descripcion,
        costo_base,
        especialidad,
        horas
    ):

        # Inicializa los atributos heredados de Servicio
        super().__init__(
            id_entidad,
            nombre,
            descripcion,
            costo_base
        )

        self.especialidad = especialidad
        self.horas = horas

    # -------------------------
    # Especialidad
    # -------------------------

    @property
    def especialidad(self):
        return self.__especialidad

    @especialidad.setter
    def especialidad(self, valor):

        if not isinstance(valor, str):
            raise ValueError("La especialidad debe ser un texto.")

        valor = valor.strip()

        if len(valor) < 3:
            raise ValueError("La especialidad debe tener al menos 3 caracteres.")

        self.__especialidad = valor

    # -------------------------
    # Horas
    # -------------------------

    @property
    def horas(self):
        return self.__horas

    @horas.setter
    def horas(self, valor):

        if not isinstance(valor, (int, float)):
            raise ValueError("Las horas deben ser un número.")

        if valor <= 0:
            raise ValueError("Las horas deben ser mayores que cero.")

        self.__horas = float(valor)

    # -------------------------
    # Polimorfismo
    # -------------------------

    def calcular_costo(self):
        return self.costo_base * self.horas

    def describir_servicio(self):
        return (
            f"Asesoría especializada en {self.especialidad} "
            f"con una duración de {self.horas} hora(s)."
        )

    def mostrar_informacion(self):
        return (
            f"Asesoria(ID: {self.id_entidad}, "
            f"Nombre: {self.nombre}, "
            f"Especialidad: {self.especialidad}, "
            f"Horas: {self.horas}, "
            f"Costo Base: ${self.costo_base:.2f}, "
            f"Costo Total: ${self.calcular_costo():.2f})"
        )
