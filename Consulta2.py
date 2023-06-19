class Consulta:
    def __init__(self, nombre, correo, mensaje):
        self.nombre = nombre
        self.correo = correo
        self.mensaje = mensaje

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getCorreo(self):
        return self.correo

    def setCorreo(self, correo):
        self.correo = correo

    def getMensaje(self):
        return self.mensaje

    def setMensaje(self, mensaje):
        self.mensaje = mensaje

    def __str__(self):
        return f"Consulta{{nombre={self.nombre}, correo={self.correo}, mensaje={self.mensaje}}}"


class GestorConsultas:
    def __init__(self):
        self.cola = []

    def nuevaConsulta(self, c):
        self.cola.append(c)

    def atenderConsulta(self):
        if self.cola:
            consulta = self.cola.pop(0)
            print(consulta)
        else:
            print("No hay consultas pendientes")

    def consultasPendientes(self):
        return len(self.cola)


gestor = GestorConsultas()

for i in range(5):
    print("Ingresa tu nombre:")
    nombre = input()
    print("Ingresa tu correo:")
    correo = input()
    print("Ingresa el mensaje de tu consulta:")
    mensaje = input()
    consulta = Consulta(nombre, correo, mensaje)
    gestor.nuevaConsulta(consulta)

print("Existen:", gestor.consultasPendientes(), "consultas pendientes")

while gestor.consultasPendientes() > 0:
    print("Si desea atender a la consulta, presione 1:")
    bandera = input()
    if bandera == "1":
        gestor.atenderConsulta()
        print("Existen:", gestor.consultasPendientes(), "consultas pendientes")
