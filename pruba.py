from models.alquiler_equipo import AlquilerEquipo

alquiler = AlquilerEquipo(
    id_entidad=2,
    nombre="Alquiler de Portátiles",
    descripcion="Servicio de alquiler de equipos portátiles.",
    costo_base=30000,
    tipo_equipo="Portátil",
    cantidad=5,
    dias_alquiler=2
)

print(alquiler.mostrar_informacion())
print(alquiler.describir_servicio())
print(f"Costo: ${alquiler.calcular_costo():.2f}")