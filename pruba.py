from models.reserva_sala import ReservaSala

reserva = ReservaSala(
    id_entidad=1,
    nombre="Sala de Juntas",
    descripcion="Reserva de sala para reuniones empresariales.",
    costo_base=50000,
    numero_sala=101,
    capacidad=20,
    horas_reserva=3
)

print(reserva.mostrar_informacion())
print(reserva.describir_servicio())
print(f"Costo: ${reserva.calcular_costo():.2f}")