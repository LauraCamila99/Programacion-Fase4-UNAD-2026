from models.servicio import Servicio


class ReservaSala(Servicio):
    """
    Representa el servicio de reserva de una sala.
    """

    def __init__(
        self,
        id_entidad,
        nombre,
        descripcion,
        costo_base,
        numero_sala,
        capacidad,
        horas_reserva
    ):

        # Inicializa los atributos heredados de Servicio
        super().__init__(
            id_entidad,
            nombre,
            descripcion,
            costo_base
        )

        self.numero_sala = numero_sala
        self.capacidad = capacidad
        self.horas_reserva = horas_reserva

    # -------------------------
    # Número de sala
    # -------------------------

    @property
    def numero_sala(self):
        return self.__numero_sala

    @numero_sala.setter
    def numero_sala(self, valor):

        if not isinstance(valor, int):
            raise ValueError("El número de sala debe ser un número entero.")

        if valor <= 0:
            raise ValueError("El número de sala debe ser mayor que cero.")

        self.__numero_sala = valor

    # -------------------------
    # Capacidad
    # -------------------------

    @property
    def capacidad(self):
        return self.__capacidad

    @capacidad.setter
    def capacidad(self, valor):

        if not isinstance(valor, int):
            raise ValueError("La capacidad debe ser un número entero.")

        if valor <= 0:
            raise ValueError("La capacidad debe ser mayor que cero.")

        self.__capacidad = valor

    # -------------------------
    # Horas de reserva
    # -------------------------

    @property
    def horas_reserva(self):
        return self.__horas_reserva

    @horas_reserva.setter
    def horas_reserva(self, valor):

        if not isinstance(valor, (int, float)):
            raise ValueError("Las horas deben ser un número.")

        if valor <= 0:
            raise ValueError("Las horas deben ser mayores que cero.")

        self.__horas_reserva = float(valor)

    # -------------------------
    # Polimorfismo
    # -------------------------

    def calcular_costo(self):
        return self.costo_base * self.horas_reserva

    def describir_servicio(self):
        return (
            f"Reserva de la sala {self.numero_sala} "
            f"con capacidad para {self.capacidad} personas."
        )

    def mostrar_informacion(self):
        return (
            f"ReservaSala(ID: {self.id_entidad}, "
            f"Nombre: {self.nombre}, "
            f"Sala: {self.numero_sala}, "
            f"Capacidad: {self.capacidad}, "
            f"Horas: {self.horas_reserva}, "
            f"Costo Base: ${self.costo_base:.2f}, "
            f"Costo Total: ${self.calcular_costo():.2f})"
        )
