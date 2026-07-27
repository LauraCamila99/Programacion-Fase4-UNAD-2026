import os
import sys
from datetime import datetime

# ==========================================
# 1. MÓDULO DE LOGGING (Autónomo)
# ==========================================
LOG_FILE = "sistema_software_fj.log"

def registrar_evento(mensaje):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] [INFO]: {mensaje}\n"
    print(f"📌 [LOG]: {mensaje}")
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(log_entry)

def registrar_error(mensaje):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] [ERROR]: {mensaje}\n"
    print(f"❌ [LOG ERROR]: {mensaje}")
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(log_entry)

# ==========================================
# 2. JERARQUÍA DE EXCEPCIONES
# ==========================================
class SoftwareFJError(Exception):
    """Excepción base del sistema"""
    pass

class ReservaError(SoftwareFJError):
    """Errores en operaciones de reserva"""
    pass

class DatosInvalidosError(SoftwareFJError):
    """Errores de parámetros o datos de entrada"""
    pass

# ==========================================
# 3. CLASES BASE DE PRUEBA Y RESERVA
# ==========================================
class ClientePrueba:
    def __init__(self, identificacion, nombre, email):
        self.identificacion = identificacion
        self.nombre = nombre
        self.email = email

class ServicioPrueba:
    def __init__(self, codigo, nombre, precio_base):
        self.codigo = codigo
        self.nombre = nombre
        self.precio_base = precio_base

class Reserva:
    def __init__(self, cliente, servicio, duracion_horas):
        if duracion_horas <= 0:
            registrar_error(f"Intento de reserva con duración inválida: {duracion_horas} horas.")
            raise DatosInvalidosError("La duración de la reserva debe ser mayor a 0 horas.")
        
        self.cliente = cliente
        self.servicio = servicio
        self.duracion_horas = duracion_horas
        self.estado = "PENDIENTE"
        registrar_evento(f"Reserva creada para {cliente.nombre} - Servicio: {servicio.nombre}")

    def calcular_costo_total(self, porcentaje_descuento=0, incluir_iva=True):
        costo_base = self.servicio.precio_base * self.duracion_horas
        descuento = costo_base * (porcentaje_descuento / 100)
        subtotal = costo_base - descuento
        iva = subtotal * 0.19 if incluir_iva else 0
        return subtotal + iva

    def confirmar(self):
        if self.estado == "CONFIRMADA":
            registrar_error(f"Intento fallido: La reserva de {self.cliente.nombre} ya está confirmada.")
            raise ReservaError("La reserva ya se encuentra confirmada.")
        self.estado = "CONFIRMADA"
        registrar_evento(f"Reserva de {self.cliente.nombre} confirmada con éxito.")

    def obtener_resumen(self):
        return f"Reserva [{self.estado}] - Cliente: {self.cliente.nombre} | Servicio: {self.servicio.nombre} | Horas: {self.duracion_horas}"

# ==========================================
# 4. EJECUCIÓN DE SIMULACIÓN Y PRUEBAS
# ==========================================
def ejecutar_pruebas_sistema():
    print("\n==================================================")
    print("  SOFTWARE FJ - PRUEBAS INTEGRADAS Y LOGGING    ")
    print("==================================================\n")
    
    registrar_evento("Iniciando suite de pruebas de integración para el sistema...")

    cliente = ClientePrueba("101010", "Juan Felipe Ríos", "juan@example.com")
    servicio = ServicioPrueba("SERV-01", "Asesoría Técnica Especializada", 50000.0)

    # Caso 1: Creación correcta
    print("\n--> 1. Creando reserva válida...")
    try:
        reserva = Reserva(cliente=cliente, servicio=servicio, duracion_horas=2)
        print(f"    {reserva.obtener_resumen()}")
        costo = reserva.calcular_costo_total(porcentaje_descuento=10)
        print(f"    Costo total calculado (con IVA y 10% desc): ${costo:,.2f}")
    except SoftwareFJError as e:
        print(f"    [ERROR]: {e}")

    # Caso 2: Confirmación de reserva
    print("\n--> 2. Confirmando la reserva...")
    try:
        reserva.confirmar()
        print(f"    Estado final: {reserva.estado}")
    except ReservaError as e:
        print(f"    [ERROR]: {e}")

    # Caso 3: Manejo de excepción (Re-confirmación)
    print("\n--> 3. Probando excepción (Re-confirmación no permitida)...")
    try:
        reserva.confirmar()
    except ReservaError as e:
        print(f"    [EXCEPCIÓN CONTROLADA CAPTURADA]: {e}")

    # Caso 4: Manejo de excepción (Duración inválida)
    print("\n--> 4. Probando excepción (Duración inválida <= 0)...")
    try:
        reserva_invalida = Reserva(cliente=cliente, servicio=servicio, duracion_horas=-1)
    except DatosInvalidosError as e:
        print(f"    [EXCEPCIÓN CONTROLADA CAPTURADA]: {e}")

    print("\n==================================================")
    print("   PRUEBAS FINALIZADAS - AUDITORÍA GUARDADA EN LOG   ")
    print("==================================================\n")

if __name__ == "__main__":
    ejecutar_pruebas_sistema()
