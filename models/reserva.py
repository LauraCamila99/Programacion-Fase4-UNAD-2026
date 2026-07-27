from models.entidad import Entidad
from exceptions.excepciones import ReservaError, DatosInvalidosError
from utils.logger import registrar_evento, registrar_error

class Reserva(Entidad):
    """
    Clase Reserva que gestiona la asignación de un Cliente a un Servicio.
    Hereda de la clase abstracta Entidad.
    """
    def __init__(self, id_entidad, cliente, servicio, duracion_horas):
        # 1. Inicializa la clase base Entidad con su ID único
        super().__init__(id_entidad)
        
        # 2. Validación de duración
        if duracion_horas <= 0:
            msg_error = f"Intento de creación de reserva {id_entidad} con duración inválida ({duracion_horas} horas)."
            registrar_error(msg_error)
            raise DatosInvalidosError("La duración de la reserva debe ser un valor estrictamente mayor a 0 horas.")
        
        # 3. Asignación de atributos
        self.cliente = cliente
        self.servicio = servicio
        self.duracion_horas = duracion_horas
        self.estado = "PENDIENTE"
        
        # Obtener nombre del cliente de manera segura (sea atributo o método)
        nombre_cliente = getattr(cliente, 'nombre', str(cliente))
        nombre_servicio = getattr(servicio, 'nombre', str(servicio))
        
        registrar_evento(f"Reserva ID [{self.id}] creada exitosamente para el cliente '{nombre_cliente}' en el servicio '{nombre_servicio}'.")

    def calcular_costo_total(self, porcentaje_descuento=0, incluir_iva=True):
        """
        Calcula el costo total haciendo uso del polimorfismo de la clase Servicio.
        """
        # Intentar llamar al método calcular_costo() propio del Servicio (Polimorfismo)
        if hasattr(self.servicio, 'calcular_costo') and callable(getattr(self.servicio, 'calcular_costo')):
            costo_base = self.servicio.calcular_costo() * self.duracion_horas
        elif hasattr(self.servicio, 'precio_base'):
            costo_base = self.servicio.precio_base * self.duracion_horas
        else:
            costo_base = 0.0

        # Aplicar descuento si existe
        descuento = costo_base * (porcentaje_descuento / 100.0)
        subtotal = costo_base - descuento
        
        # Aplicar IVA del 19%
        iva = subtotal * 0.19 if incluir_iva else 0.0
        
        return subtotal + iva

    def confirmar(self):
        """
        Confirma la reserva verificando que no esté previamente confirmada o cancelada.
        """
        if self.estado == "CONFIRMADA":
            msg = f"No se puede re-confirmar la Reserva ID [{self.id}]. Ya se encuentra CONFIRMADA."
            registrar_error(msg)
            raise ReservaError(msg)
        
        if self.estado == "CANCELADA":
            msg = f"No se puede confirmar la Reserva ID [{self.id}]. Se encuentra CANCELADA."
            registrar_error(msg)
            raise ReservaError(msg)

        self.estado = "CONFIRMADA"
        registrar_evento(f"Reserva ID [{self.id}] ha cambiado su estado a CONFIRMADA.")

    def cancelar(self):
        """
        Cancela la reserva.
        """
        if self.estado == "CANCELADA":
            msg = f"La Reserva ID [{self.id}] ya se encontraba cancelada anteriormente."
            registrar_error(msg)
            raise ReservaError(msg)

        self.estado = "CANCELADA"
        registrar_evento(f"Reserva ID [{self.id}] cancelada exitosamente.")

    def obtener_resumen(self):
        """
        Retorna la representación en texto formateado de la reserva.
        """
        nombre_cli = getattr(self.cliente, 'nombre', str(self.cliente))
        nombre_srv = getattr(self.servicio, 'nombre', str(self.servicio))
        return f"Reserva ID [{self.id}] | Estado: {self.estado} | Cliente: {nombre_cli} | Servicio: {nombre_srv} | Duración: {self.duracion_horas}h"
      
