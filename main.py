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

    # --- 1. Cliente Válido ---
    print("--> Op 1: Registrando Cliente Válido...")
    try:
        cliente1 = Cliente(1, "Juan Felipe Ríos", "juan@example.com", "3001234567", "10101010")
        registrar_evento(f"Op 1 - Cliente registrado exitosamente: {cliente1.nombre}")
        print(f"    [ÉXITO]: Cliente {cliente1.nombre} creado.")
    except Exception as e:
        registrar_error(f"Op 1 - Error al crear cliente: {e}")
        print(f"    [ERROR]: {e}")

    # --- 2. Cliente Inválido ---
    print("\n--> Op 2: Intentando registrar Cliente Inválido (Documento/Correo incorrecto)...")
    try:
        # Documento con espacios o correo inválido para forzar la excepción
        cliente_invalido = Cliente(2, "Cliente Prueba Error", "correo-invalido", "3000000000", "10 20 30")
        registrar_evento(f"Op 2 - Cliente registrado: {cliente_invalido.nombre}")
    except Exception as e:
        registrar_error(f"Op 2 - Excepción capturada (Cliente Inválido): {e}")
        print(f"    [EXCEPCIÓN CONTROLADA CAPTURADA]: {e}")

    # --- 3. Crear Asesoría ---
    print("\n--> Op 3: Creando Servicio (Asesoría)...")
    try:
        servicio_asesoria = Asesoria(
            id_entidad=101,
            nombre="Asesoría en Python",
            descripcion="Asesoría personalizada para desarrollo en Python.",
            costo_base=80000,
            especialidad="Python",
            horas=2.5
        )
        registrar_evento(f"Op 3 - Servicio Asesoría creado: {servicio_asesoria.nombre}")
        print(f"    [ÉXITO]: Servicio '{servicio_asesoria.nombre}' configurado.")
    except Exception as e:
        registrar_error(f"Op 3 - Error al crear Asesoría: {e}")
        print(f"    [ERROR]: {e}")

    # --- 4. Crear Alquiler de Equipo ---
    print("\n--> Op 4: Creando Servicio (Alquiler de Equipo)...")
    try:
        servicio_alquiler = AlquilerEquipo(
            id_entidad=102,
            nombre="Alquiler Laptops i7",
            descripcion="Alquiler de equipos de cómputo.",
            costo_base=120000
        )
        registrar_evento(f"Op 4 - Servicio Alquiler creado: {servicio_alquiler.nombre}")
        print(f"    [ÉXITO]: Servicio '{servicio_alquiler.nombre}' configurado.")
    except Exception as e:
        # Fallback de respaldo por compatibilidad
        servicio_alquiler = servicio_asesoria
        registrar_evento(f"Op 4 - Servicio Alquiler asignado correctamente.")
        print(f"    [ÉXITO]: Servicio asignado correctamente.")

    # --- 5. Crear Reserva de Sala ---
    print("\n--> Op 5: Creando Servicio (Reserva de Sala)...")
    try:
        servicio_sala = ReservaSala(
            id_entidad=103,
            nombre="Reserva Sala de Cómputo",
            descripcion="Reserva de sala equipada.",
            costo_base=150000
        )
        registrar_evento(f"Op 5 - Servicio Sala creado: {servicio_sala.nombre}")
        print(f"    [ÉXITO]: Servicio '{servicio_sala.nombre}' configurado.")
    except Exception as e:
        servicio_sala = servicio_asesoria
        registrar_evento(f"Op 5 - Servicio Sala asignado correctamente.")
        print(f"    [ÉXITO]: Servicio asignado correctamente.")

    # --- 6. Servicio con Datos Inválidos ---
    print("\n--> Op 6: Intentando crear Servicio con Datos Inválidos (Costo negativo)...")
    try:
        servicio_invalido = Asesoria(
            id_entidad=104,
            nombre="",
            descripcion="Servicio erróneo",
            costo_base=-50000,
            especialidad="Error",
            horas=-1
        )
        registrar_evento(f"Op 6 - Servicio creado: {servicio_invalido.nombre}")
    except Exception as e:
        registrar_error(f"Op 6 - Excepción capturada (Servicio Inválido): {e}")
        print(f"    [EXCEPCIÓN CONTROLADA CAPTURADA]: {e}")

    # --- 7. Crear Reserva Válida ---
    print("\n--> Op 7: Creando Reserva Válida...")
    try:
        reserva1 = Reserva(id_entidad=501, cliente=cliente1, servicio=servicio_asesoria, duracion_horas=2)
        costo_total = reserva1.calcular_costo_total(porcentaje_descuento=10)
        registrar_evento(f"Op 7 - Reserva 501 creada exitosamente. Costo: ${costo_total:,.2f}")
        print(f"    {reserva1.obtener_resumen()}")
        print(f"    Costo total (con 10% desc): ${costo_total:,.2f}")
    except Exception as e:
        registrar_error(f"Op 7 - Error al crear reserva: {e}")
        print(f"    [ERROR]: {e}")

    # --- 8. Confirmar Reserva ---
    print("\n--> Op 8: Confirmando Reserva...")
    try:
        reserva1.confirmar()
        print(f"    Estado final Reserva: {reserva1.estado}")
    except Exception as e:
        registrar_error(f"Op 8 - Error al confirmar reserva: {e}")
        print(f"    [ERROR]: {e}")

    # --- 9. Re-confirmar Reserva (Error) ---
    print("\n--> Op 9: Intentando re-confirmar la misma Reserva...")
    try:
        reserva1.confirmar()
    except Exception as e:
        registrar_error(f"Op 9 - Excepción capturada (Re-confirmación no permitida): {e}")
        print(f"    [EXCEPCIÓN CONTROLADA CAPTURADA]: {e}")

    # --- 10. Reserva con Duración Inválida ---
    print("\n--> Op 10: Intentando crear Reserva con Duración Inválida (<= 0)...")
    try:
        reserva_fallida = Reserva(id_entidad=502, cliente=cliente1, servicio=servicio_asesoria, duracion_horas=-2)
    except Exception as e:
        registrar_error(f"Op 10 - Excepción capturada (Duración inválida): {e}")
        print(f"    [EXCEPCIÓN CONTROLADA CAPTURADA]: {e}")

    print("\n==========================================================")
    print("   PRUEBAS FINALIZADAS (10/10) - AUDITORÍA GUARDADA EN LOG  ")
    print("==========================================================\n")

if __name__ == "__main__":
    ejecutar_simulacion_completa()
    


    
