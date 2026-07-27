"""
Módulo de la clase Reserva - Sistema Software FJ
"""

from models.entidad import Entidad
from exceptions.excepciones import ReservaError, DatosInvalidosError
from utils.logger import registrar_evento, registrar_error


class Reserva(Entidad):
    def __init__(self, id_entidad: int, cliente, servicio, duracion_horas: float):
        super().__init__(id_entidad)
        
        if duracion_horas <= 0:
            raise DatosInvalidosError("La duración de la reserva debe ser mayor a 0 horas.")
            
        self.cliente = cliente
        self.servicio = servicio
        self.duracion_horas = duracion_horas
        self.estado = "PENDIENTE"

    def mostrar_informacion(self) -> str:
        """
        Implementación obligatoria del método abstracto de Entidad.
        """
        return self.obtener_resumen()

    def calcular_costo_total(self, porcentaje_descuento: float = 0.0) -> float:
        """Calcula el costo total aplicando costo base del servicio y horas."""
        costo_base = getattr(self.servicio, 'costo_base', 0)
        if hasattr(self.servicio, 'calcular_costo'):
            costo_base = self.servicio.calcular_costo()
            
        subtotal = costo_base * self.duracion_horas
        descuento = subtotal * (porcentaje_descuento / 100)
        return subtotal - descuento

    def confirmar(self):
        """Confirma la reserva si está pendiente."""
        if self.estado == "CONFIRMADA":
            raise ReservaError("La reserva ya ha sido confirmada previamente.")
        self.estado = "CONFIRMADA"
        registrar_evento(f"Reserva {self.id_entidad} confirmada con éxito.")

    def cancelar(self):
        """Cancela la reserva."""
        if self.estado == "CANCELADA":
            raise ReservaError("La reserva ya se encuentra cancelada.")
        self.estado = "CANCELADA"
        registrar_evento(f"Reserva {self.id_entidad} cancelada.")

    def obtener_resumen(self) -> str:
        nombre_cliente = getattr(self.cliente, 'nombre', 'Cliente General')
        nombre_servicio = getattr(self.servicio, 'nombre', 'Servicio General')
        return f"Reserva #{self.id_entidad} - Cliente: {nombre_cliente} | Servicio: {nombre_servicio} | Horas: {self.duracion_horas} | Estado: {self.estado}"
      
