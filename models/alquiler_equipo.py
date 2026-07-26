from models.servicio import Servicio


class AlquilerEquipo(Servicio):
    """
    Representa el servicio de alquiler de equipos.
    """

    def __init__(
        self,
        id_entidad,
        nombre,
        descripcion,
        costo_base,
        tipo_equipo,
        cantidad,
        dias_alquiler
    ):

        # Inicializa los atributos heredados de Servicio
        super().__init__(
            id_entidad,
            nombre,
            descripcion,
            costo_base
        )

        self.tipo_equipo = tipo_equipo
        self.cantidad = cantidad
        self.dias_alquiler = dias_alquiler

    # -------------------------
    # Tipo de equipo
    # -------------------------

    @property
    def tipo_equipo(self):
        return self.__tipo_equipo

    @tipo_equipo.setter
    def tipo_equipo(self, valor):

        if not isinstance(valor, str):
            raise ValueError("El tipo de equipo debe ser un texto.")

        valor = valor.strip()

        if len(valor) < 3:
            raise ValueError("El tipo de equipo debe tener al menos 3 caracteres.")

        self.__tipo_equipo = valor

    # -------------------------
    # Cantidad
    # -------------------------

    @property
    def cantidad(self):
        return self.__cantidad

    @cantidad.setter
    def cantidad(self, valor):

        if not isinstance(valor, int):
            raise ValueError("La cantidad debe ser un número entero.")

        if valor <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")

        self.__cantidad = valor

    # -------------------------
    # Días de alquiler
    # -------------------------

    @property
    def dias_alquiler(self):
        return self.__dias_alquiler

    @dias_alquiler.setter
    def dias_alquiler(self, valor):

        if not isinstance(valor, (int, float)):
            raise ValueError("Los días de alquiler deben ser un número.")

        if valor <= 0:
            raise ValueError("Los días de alquiler deben ser mayores que cero.")

        self.__dias_alquiler = float(valor)

    # -------------------------
    # Polimorfismo
    # -------------------------

    def calcular_costo(self):
        return self.costo_base * self.cantidad * self.dias_alquiler

    def describir_servicio(self):
        return (
            f"Alquiler de {self.cantidad} "
            f"{self.tipo_equipo}(s) durante "
            f"{self.dias_alquiler} día(s)."
        )

    def mostrar_informacion(self):
        return (
            f"AlquilerEquipo(ID: {self.id_entidad}, "
            f"Nombre: {self.nombre}, "
            f"Equipo: {self.tipo_equipo}, "
            f"Cantidad: {self.cantidad}, "
            f"Días: {self.dias_alquiler}, "
            f"Costo Base: ${self.costo_base:.2f}, "
            f"Costo Total: ${self.calcular_costo():.2f})"
        )
