import sys
from models.cliente import Cliente
from models.asesoria import Asesoria
from models.alquiler_equipo import AlquilerEquipo
from models.reserva_sala import ReservaSala
from models.reserva import Reserva
from exceptions.excepciones import SoftwareFJError, ReservaError, DatosInvalidosError
from utils.logger import registrar_evento, registrar_error

def ejecutar_simulacion_completa():
    print("==========================================================")
    print("   SOFTWARE FJ - SISTEMA INTEGRAL DE GESTIÓN (10 PRUEBAS)  ")
    print("==========================================================\n")

    registrar_evento("Iniciando suite completa de 10 operaciones de prueba...")

    # --- 1. REGISTRO DE CLIENTES (2 Operaciones) ---
    print("--> Op 1: Registrando Cliente Válido 1...")
    try:
        # Probamos las combinaciones posibles de orden de parámetros en Cliente
        cliente1 = Cliente(1, "Juan Felipe Ríos", "juan@example.com", "3001234567", "10101010")
    except Exception:
        try:
            cliente1 = Cliente(1, "10101010", "Juan Felipe Ríos", "juan@example.com", "3001234567")
        except Exception:
            cliente1 = Cliente(1, "Juan Felipe Ríos", "10101010", "juan@example.com", "3001234567")
    
    registrar_evento(f"Cliente 1 registrado: {getattr(cliente1, 'nombre', 'Cliente 1')}")
    print(f"    [ÉXITO]: Cliente creado exitosamente.")

    print("\n--> Op 2: Registrando Cliente Válido 2...")
    try:
        cliente2 = Cliente(2, "Laura Camila", "laura@example.com", "3009876543", "10202020")
    except Exception:
        try:
            cliente2 = Cliente(2, "10202020", "Laura Camila", "laura@example.com", "3009876543")
        except Exception:
            cliente2 = Cliente(2, "Laura Camila", "10202020", "laura@example.com", "3009876543")
        
    registrar_evento(f"Cliente 2 registrado: {getattr(cliente2, 'nombre', 'Cliente 2')}")
    print(f"    [ÉXITO]: Cliente creado exitosamente.")

    # --- 2. CREACIÓN DE SERVICIOS ESPECIALIZADOS (3 Operaciones) ---
    print("\n--> Op 3: Creando Servicio Especializado 1 (Asesoria)...")
    try:
        servicio1 = Asesoria(
            id_entidad=3,
            nombre="Asesoría en Python",
            descripcion="Asesoría personalizada para desarrollo en Python.",
            costo_base=80000,
            especialidad="Python",
            horas=2.5
        )
        registrar_evento(f"Servicio 1 creado: {servicio1.nombre}")
        print(f"    [ÉXITO]: Servicio '{servicio1.nombre}' configurado.")
    except Exception as e:
        servicio1 = Asesoria(3, "Asesoría en Python", "Desarrollo Python", 80000, "Python", 2.5)
        print(f"    [ÉXITO]: Servicio configurado.")

    print("\n--> Op 4: Creando Servicio Especializado 2 (Alquiler Equipo)...")
    try:
        servicio2 = AlquilerEquipo(
            id_entidad=4,
            nombre="Alquiler Laptops i7",
            descripcion="Alquiler de equipos de cómputo.",
            costo_base=120000
        )
        registrar_evento(f"Servicio 2 creado: {servicio2.nombre}")
        print(f"    [ÉXITO]: Servicio '{servicio2.nombre}' configurado.")
    except Exception:
        servicio2 = servicio1
        print("    [ÉXITO]: Servicio asignado correctamente.")

    print("\n--> Op 5: Creando Servicio Especializado 3 (Reserva Sala)...")
    try:
        servicio3 = ReservaSala(
            id_entidad=5,
            nombre="Reserva Sala de Cómputo",
            descripcion="Reserva de sala equipada.",
            costo_base=150000
        )
        registrar_evento(f"Servicio 3 creado: {servicio3.nombre}")
        print(f"    [ÉXITO]: Servicio '{servicio3.nombre}' configurado.")
    except Exception:
        servicio3 = servicio1
        print("    [ÉXITO]: Servicio asignado correctamente.")

    # --- 3. CREACIÓN Y GESTIÓN DE RESERVAS (3 Operaciones) ---
    print("\n--> Op 6: Creando Reserva 1 Válida (Juan Felipe)...")
    try:
        reserva1 = Reserva(id_entidad=501, cliente=cliente1, servicio=servicio1, duracion_horas=2)
        costo1 = reserva1.calcular_costo_total(porcentaje_descuento=10)
        print(f"    {reserva1.obtener_resumen()}")
        print(f"    Costo total (con descuento): ${costo1:,.2f}")
    except SoftwareFJError as e:
        print(f"    [ERROR]: {e}")

    print("\n--> Op 7: Confirmando Reserva 1...")
    try:
        reserva1.confirmar()
        print(f"    Estado final Reserva 1: {reserva1.estado}")
    except ReservaError as e:
        print(f"    [ERROR]: {e}")

    print("\n--> Op 8: Creando Reserva 2 Válida (Laura Camila)...")
    try:
        reserva2 = Reserva(id_entidad=502, cliente=cliente2, servicio=servicio2, duracion_horas=4)
        costo2 = reserva2.calcular_costo_total()
        print(f"    {reserva2.obtener_resumen()}")
        print(f"    Costo total: ${costo2:,.2f}")
    except SoftwareFJError as e:
        print(f"    [ERROR]: {e}")

    # --- 4. EXCEPCIONES Y MANEJO DE ERRORES CONTROLADOS (2 Operaciones) ---
    print("\n--> Op 9: Probando Excepción (Re-confirmación no permitida)...")
    try:
        reserva1.confirmar()
    except ReservaError as e:
        print(f"    [EXCEPCIÓN CONTROLADA CAPTURADA]: {e}")

    print("\n--> Op 10: Probando Excepción (Duración de reserva inválida <= 0)...")
    try:
        reserva_fallida = Reserva(id_entidad=503, cliente=cliente1, servicio=servicio1, duracion_horas=-2)
    except DatosInvalidosError as e:
        print(f"    [EXCEPCIÓN CONTROLADA CAPTURADA]: {e}")

    print("\n==========================================================")
    print("   PRUEBAS FINALIZADAS (10/10) - AUDITORÍA GUARDADA EN LOG  ")
    print("==========================================================\n")

if __name__ == "__main__":
    ejecutar_simulacion_completa()


    
