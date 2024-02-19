class Asiento ():

	def __init__ (self):

		self.color = None
		self.precio = 0
		self.registro = 0


	def cambiarColor (self, color):

		catalogo = ["amarillo", "verde", "azul", "negro", "blanco"]

		if color in catalogo:

			self.color = color


class Motor ():

	def __init__ (self):

		self.numeroCilindros = 0
		self.tipo = None
		self.registro = 0

	def cambiarRegistro (self, registro):

		self.registro = registro

	def asignarTipo (self, tipo):

		if tipo == ("gasolina" or "electrico"):

			self.tipo = tipo

class Auto ():

	cantidadCreados = 0

	def __init__ (self):

		self.modelo = None
		self.precio = 0
		self.asientos = []
		self.marca = None
		self.motor = None
		self.registro = 0

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

			if self.registro != i.registro:

				return ("Las piezas no son originales")


		return ("Auto original")

