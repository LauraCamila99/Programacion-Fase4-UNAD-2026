class SoftwareFJError(Exception):
    """
    Clase base para todas las excepciones del sistema Software FJ.
    Todas las excepciones personalizadas del proyecto heredan de esta clase.
    """
    pass

class DatosInvalidosError(SoftwareFJError):
    """
    Se lanza cuando los datos ingresados no cumplen con las validaciones 
    o parámetros estrictos del sistema (ej. duraciones negativas, campos vacíos, etc.).
    """
    pass

class ServicioNoDisponibleError(SoftwareFJError):
    """
    Se lanza cuando se intenta realizar una reserva sobre un servicio 
    que no está disponible actualmente.
    """
    pass

class ReservaError(SoftwareFJError):
    """
    Se lanza cuando ocurre un fallo general o de procesamiento 
    durante el ciclo de vida de una reserva.
    """
    pass

class OperacionNoPermitidaError(SoftwareFJError):
    """
    Se lanza al intentar realizar acciones no válidas según el estado actual 
    del objeto (ej. confirmar una reserva ya cancelada).
    """
    pass
