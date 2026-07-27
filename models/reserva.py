from models.entidad import Entidad
from exceptions.excepciones import ReservaError, DatosInvalidosError
from utils.logger import registrar_evento, registrar_error

class Reserva(Entidad):
    def __init__(self, id_entidad, cliente, servicio, duracion_horas):
        super().__init__(id_entidad)
        
        if duracion_horas <= 0:
            raise DatosInvalidosError("La duración de la reserva debe ser mayor a 0 horas.")
            
        self.cliente = cliente
        self.servicio = servicio
        self.duracion_horas = duracion_horas
        self.estado = "Pendiente"

    def calcular_costo_total(self, porcentaje_descuento=0):
        costo_base = getattr(self.servicio, 'costo_base', 0)
        costo_bruto = costo_base * self.duracion_horas
        descuento = costo_bruto * (porcentaje_descuento / 100)
        return costo_bruto - descuento

    def confirmar(self):
        if self.estado == "Confirmada":
            raise ReservaError(f"La reserva {self.id_entidad} ya se encuentra confirmada.")
        
        self.estado = "Confirmada"
        registrar_evento(f"Reserva {self.id_entidad} confirmada con éxito.")

    def obtener_resumen(self):
        return f"Reserva {self.id_entidad} - Cliente: {self.cliente.nombre} | Servicio: {self.servicio.nombre} | Estado: {self.estado}"
        
      
