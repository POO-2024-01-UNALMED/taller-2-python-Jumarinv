class Asiento ():

	def __init__ (self, color, precio, registro):

		self.color = color
		self.precio = precio
		self.registro = registro


	def cambiarColor (self, color):

		catalogo = ["amarillo", "verde", "azul", "negro", "blanco"]

		if color in catalogo:

			self.color = color


class Motor ():

	def __init__ (self, cilindros, tipe, registro):

		self.numeroCilindros = cilindros
		self.tipo = tipe
		self.registro = registro

	def cambiarRegistro (self, registro):

		self.registro = registro

	def asignarTipo (self, tipo):

		if tipo in ("gasolina", "electrico"):

			self.tipo = tipo

class Auto ():

	cantidadCreados = 0

	def __init__ (self, modelo, precio, asientos, marca, motor, registro):

		self.modelo = modelo
		self.precio = precio
		self.asientos = asientos
		self.marca = marca
		self.motor = motor
		self.registro = registro

	def cantidadAsientos (self):

		numAsientos = 0

		for i in self.asientos:

			if type(i) == Asiento:

				numAsientos += 1

		return numAsientos

	def verificarIntegridad (self):

		if self.registro != self.motor.registro:

			return ("Las piezas no son originales")

		for i in self.asientos:

			if type(i) == Asiento:

				if self.registro != i.registro:

					return ("Las piezas no son originales")


			


		return ("Auto original")

