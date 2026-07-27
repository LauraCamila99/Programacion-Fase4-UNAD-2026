from models.asesoria import Asesoria

asesoria = Asesoria(
    id_entidad=3,
    nombre="Asesoría en Python",
    descripcion="Asesoría personalizada para desarrollo en Python.",
    costo_base=80000,
    especialidad="Python",
    horas=2.5
)

print(asesoria.mostrar_informacion())
print(asesoria.describir_servicio())
print(f"Costo: ${asesoria.calcular_costo():.2f}")