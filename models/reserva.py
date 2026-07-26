import uuid
from datetime import datetime

# Importaciones de los módulos ubicados en exceptions/ y utils/
from exceptions.excepciones import (
    DatosInvalidosError, 
    ReservaError, 
    OperacionNoPermitidaError, 
    ServicioNoDisponibleError
)
from utils.logger_config import registrar_evento, registrar_error

class Reserva:
    """
    Clase que representa una Reserva en el sistema Software FJ.
    Integra cliente, servicio, duración y estado, e implementa
    confirmación, cancelación y procesamiento con manejo de excepciones.
    """
    def __init__(self, cliente, servicio, duracion_horas: int):
        self._id_reserva = str(uuid.uuid4())[:8].upper()
        self._cliente = cliente
        self._servicio = servicio
        self._duracion_horas = duracion_horas
        self._estado = "PENDIENTE"
        self._fecha_creacion = datetime.now()
        
        # Validar parámetros de entrada al instanciar
        self._validar_parametros()
        registrar_evento(f"Reserva {self._id_reserva} creada preliminarmente en estado PENDIENTE.")

    # Getters
    @property
    def id_reserva(self) -> str:
        return self._id_reserva

    @property
    def cliente(self):
        return self._cliente

    @property
    def servicio(self):
        return self._servicio

    @property
    def duracion_horas(self) -> int:
        return self._duracion_horas

    @property
    def estado(self) -> str:
        return self._estado

    def _validar_parametros(self):
        """Valida internamente que los datos de la reserva sean correctos."""
        if not self._cliente:
            raise DatosInvalidosError("La reserva debe tener un cliente asignado.")
        if not self._servicio:
            raise DatosInvalidosError("La reserva debe tener un servicio asignado.")
        if not isinstance(self._duracion_horas, (int, float)) or self._duracion_horas <= 0:
            raise DatosInvalidosError(f"Duración inválida: {self._duracion_horas}. Debe ser mayor a 0 horas.")

    # --- MÉTODOS DE CÁLCULO / SOBRECARGA Y POLIMORFISMO ---
    def calcular_costo_total(self, porcentaje_descuento: float = 0.0, porcentaje_impuesto: float = 0.19) -> float:
        """
        Calcula el costo total de la reserva con variaciones de descuentos e impuestos opcionales.
        Aplica polimorfismo invocando el método 'calcular_costo' del servicio asociado.
        """
        if porcentaje_descuento < 0 or porcentaje_descuento > 100:
            raise DatosInvalidosError(f"Porcentaje de descuento inválido: {porcentaje_descuento}%")
        
        costo_base = self._servicio.calcular_costo(self._duracion_horas)
        monto_descuento = costo_base * (porcentaje_descuento / 100.0)
        subtotal = costo_base - monto_descuento
        costo_total = subtotal * (1 + porcentaje_impuesto)
        return round(costo_total, 2)

    # --- MÉTODOS DE NEGOCIO CON MANEJO AVANZADO DE EXCEPCIONES ---
    def confirmar(self) -> bool:
        """
        Confirma la reserva aplicando la estructura try / except / else / finally 
        y encadenamiento de excepciones.
        """
        registrar_evento(f"Iniciando proceso de confirmación para la reserva {self._id_reserva}...")
        
        try:
            # 1. Validar estado actual
            if self._estado != "PENDIENTE":
                raise OperacionNoPermitidaError(
                    f"No se puede confirmar la reserva {self._id_reserva} porque se encuentra en estado '{self._estado}'."
                )
            
            # 2. Validar disponibilidad del servicio si el objeto servicio expone dicho atributo
            if hasattr(self._servicio, 'disponible') and not self._servicio.disponible:
                raise ServicioNoDisponibleError(
                    f"El servicio '{self._servicio.nombre}' no se encuentra disponible actualmente."
                )

        except (OperacionNoPermitidaError, ServicioNoDisponibleError) as err:
            # Encadenamiento de excepciones (raise ... from ...)
            error_reserva = ReservaError(f"Fallo en la confirmación de la reserva {self._id_reserva}.")
            registrar_error(f"Error procesando la confirmación de la reserva {self._id_reserva}", err)
            raise error_reserva from err

        else:
            # Se ejecuta solo si NO ocurrió ninguna excepción en el bloque try
            self._estado = "CONFIRMADA"
            mensaje_exito = f"Reserva {self._id_reserva} CONFIRMADA exitosamente para el cliente {self._cliente.nombre}."
            print(f"[ÉXITO] {mensaje_exito}")
            registrar_evento(mensaje_exito)
            return True

        finally:
            # Se ejecuta SIEMPRE para trazabilidad y auditoría
            registrar_evento(f"Finalizado procesamiento de confirmación para la reserva {self._id_reserva}. Estado actual: {self._estado}")

    def cancelar(self, motivo: str = "Sin especificar") -> bool:
        """
        Cancela la reserva registrando el motivo y validando el estado.
        Aplica estructura try / except / else / finally.
        """
        registrar_evento(f"Iniciando solicitud de cancelación para la reserva {self._id_reserva}...")
        
        try:
            if self._estado == "CANCELADA":
                raise OperacionNoPermitidaError(f"La reserva {self._id_reserva} ya se encuentra cancelada.")
            
            if not motivo or len(motivo.strip()) < 3:
                raise DatosInvalidosError("Debe proporcionar un motivo válido de cancelación (mínimo 3 caracteres).")

        except (OperacionNoPermitidaError, DatosInvalidosError) as err:
            registrar_error(f"Error cancelando reserva {self._id_reserva}", err)
            raise ReservaError(f"No fue posible cancelar la reserva {self._id_reserva}.") from err

        else:
            self._estado = "CANCELADA"
            msg = f"Reserva {self._id_reserva} CANCELADA. Motivo: {motivo}"
            print(f"[INFO] {msg}")
            registrar_evento(msg)
            return True

        finally:
            registrar_evento(f"Finalizado intento de cancelación de la reserva {self._id_reserva}.")

    def obtener_resumen(self) -> str:
        """Retorna una cadena con el resumen descriptivo de la reserva."""
        costo_estandar = self.calcular_costo_total()
        return (
            f"--- RESUMEN DE RESERVA [{self._id_reserva}] ---\n"
            f"Cliente: {self._cliente.nombre}\n"
            f"Servicio: {self._servicio.nombre}\n"
            f"Duración: {self._duracion_horas} hora(s)\n"
            f"Estado: {self._estado}\n"
            f"Costo Total (con IVA): ${costo_estandar:,.2f}"
        )
