from models.cliente import Cliente

cliente = Cliente(
    id_entidad=1,
    nombre="Laura Tiusabá",
    documento="CC123456",
    correo="laura@gmail.com",
    telefono="3143704859"
)

print(cliente.mostrar_informacion())