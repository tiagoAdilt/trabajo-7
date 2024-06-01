class Alumno:
    def __init__(self, nombre, apellido, dni, domicilio):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.domicilio = domicilio
        self.notas = []
        self.faltas = 0
        self.amonestaciones = 0

    def ingresar_nota(self, nota):
        self.notas.append(nota)
        print(f"Nota {nota} ingresada para {self.nombre} {self.apellido}.")

    def asignar_falta(self):
        self.faltas += 1
        print(f"Falta asignada a {self.nombre} {self.apellido}. Total de faltas: {self.faltas}.")

    def asignar_amonestacion(self):
        self.amonestaciones += 1
        print(f"Amonestación asignada a {self.nombre} {self.apellido}. Total de amonestaciones: {self.amonestaciones}.")

    def cambiar_domicilio(self, nuevo_domicilio):
        self.domicilio = nuevo_domicilio
        print(f"Domicilio de {self.nombre} {self.apellido} actualizado a {nuevo_domicilio}.")

    def __str__ (self):
        return (f"Alumno: {self.nombre} {self.apellido}, DNI: {self.dni}, Domicilio: {self.domicilio}, "
                f"Notas: {self.notas}, Faltas: {self.faltas}, Amonestaciones: {self.amonestaciones}")

# Ejemplo de uso
alumno1 = Alumno("Juan", "Perez", "12345678", "Calle sarmiento 123")
alumno1.ingresar_nota(8)
alumno1.asignar_falta()
alumno1.asignar_amonestacion()
alumno1.cambiar_domicilio("Calle belgrano 456")
print(alumno1)
alumno2=Alumno("Tiago","Enriquez","48413379","calle 25 de mayo 87")
alumno2.ingresar_nota(7)
alumno2.asignar_falta()
alumno2.asignar_amonestacion()
alumno2.cambiar_domicilio("av. peron 1339")
print(alumno2)
#__str__(): Método especial que retorna una representación en cadena del objeto para facilitar su impresión