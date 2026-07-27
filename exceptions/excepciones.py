"""
Módulo de Excepciones Personalizadas - Sistema Software FJ
"""

class SoftwareFJError(Exception):
    """Excepción base para el sistema Software FJ."""
    def __init__(self, mensaje="Error general en el sistema Software FJ."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

    def __str__(self):
        return f"[{self.__class__.__name__}]: {self.mensaje}"


class DatosInvalidosError(SoftwareFJError):
    """Lanzada cuando los datos de entrada no son válidos (ej. duración <= 0)."""
    pass


class ReservaError(SoftwareFJError):
    """Lanzada ante operaciones no permitidas en la Reserva (ej. re-confirmación)."""
    pass


class ServicioNoDisponibleError(SoftwareFJError):
    """Lanzada cuando un servicio no está disponible."""
    pass


class ClienteNoEncontradoError(SoftwareFJError):
    """Lanzada cuando un cliente no se encuentra en el sistema."""
    pass
