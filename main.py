import sys
from models.cliente import Cliente
from models.servicio import Servicio
from models.reserva import Reserva
from exceptions.excepciones import SoftwareFJError, ReservaError, DatosInvalidosError
from utils.logger_config import registrar_evento, registrar_error

def ejecutar_pruebas_reserva():
    print("==================================================")
    print("      INICIANDO PRUEBAS DEL MÓDULO RESERVA        ")
    print("==================================================\n")
    
    registrar_evento("Iniciando sesión de pruebas de integración para el módulo Reserva...")

    # 1. Crear objetos base para las pruebas
    cliente_prueba = Cliente("101010", "Juan Felipe Ríos", "juan@example.com")
    servicio_prueba = Servicio("SERV-01", "Asesoría Técnica", 50000.0)

    # 2. Prueba de creación exitosa de Reserva
    print("--> 1. Creando reserva válida...")
    try:
        reserva = Reserva(cliente=cliente_prueba, servicio=servicio_prueba, duracion_horas=2)
        print(reserva.obtener_resumen())
        print(f"Costo calculado (con IVA y 10% desc): ${reserva.calcular_costo_total(porcentaje_descuento=10):,.2f}\n")
    except SoftwareFJError as e:
        print(f"[ERROR INESPERADO]: {e}\n")

    # 3. Prueba de Confirmación
    print("--> 2. Confirmando la reserva...")
    try:
        reserva.confirmar()
        print(f"Estado tras confirmación: {reserva.estado}\n")
    except ReservaError as e:
        print(f"[ERROR AL CONFIRMAR]: {e}\n")

    # 4. Prueba de Excepción: Intentar confirmar una reserva ya confirmada
    print("--> 3. Probando excepción (Re-confirmación no permitida)...")
    try:
        reserva.confirmar()
    except ReservaError as e:
        print(f"[EXCEPCIÓN CAPTURADA CORRECTAMENTE]: {e}\n")

    # 5. Prueba de Excepción: Creación con parámetros inválidos
    print("--> 4. Probando excepción (Duración inválida <= 0)...")
    try:
        reserva_invalida = Reserva(cliente=cliente_prueba, servicio=servicio_prueba, duracion_horas=-1)
    except DatosInvalidosError as e:
        print(f"[EXCEPCIÓN CAPTURADA CORRECTAMENTE]: {e}\n")

    print("==================================================")
    print("   PRUEBAS FINALIZADAS - REVISAR LOGS GENERADOS   ")
    print("==================================================")

if __name__ == "__main__":
    ejecutar_pruebas_reserva()
